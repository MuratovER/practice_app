import re
from loguru import logger
from twelvedata import TDClient
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from rest_framework.utils import json

from mainsite.forms import PostForm, CommentForm
from mainsite.models import Post, Comment, LikeDislike, CodeExamples, EulerProblem, Stock
from mainsite.services.services_code_example import check_for_project_list


def apps_list(request):
    return render(request, 'app_list.html')


def blog_page(request):
    posts = Post.objects.all()

    return render(request, 'blog/main_blog.html', {"posts": posts})


def programming(request):
    return render(request, 'programming/main_code.html')


def euler_problems(request):
    problems = EulerProblem.objects.all()
    return render(request, 'programming/euler_problems.html', {'problems': problems})


def code_examples(request):
    check_for_project_list()
    projects = CodeExamples.objects.all()
    return render(request, 'programming/code_examples.html', {'projects': projects})


def main_invest(request):
    # td = TDClient(apikey="c7d2d67226394eafb42704f30600f740")
    #
    #
    #
    # ts = td.time_series(symbol='AAPL,MSFT', interval="1min", outputsize=3)
    # df = ts.with_macd().with_macd(fast_period=10).with_stoch().as_pandas()

    # print(df)

    return render(request, 'investment/main_invest.html')


def home_page(request):
    return redirect('blog_page')


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    ctx = {
        'post': post,
        'form': form
    }

    return render(request, 'blog/post_detail.html', ctx)


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog_page')


def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()

    return redirect('post_detail', pk=comment.post.pk)


def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', comment.post.pk)


def comment_edit(request, pk):
    commment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = commment.post
            comment.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/post_edit.html', {'form': form})


class VotesView(View):
    model = None  # Модель данных - Статьи или Комментарии
    vote_type = None  # Тип комментария Like/Dislike

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        # GenericForeignKey не поддерживает метод get_or_create
        try:
            likedislike = LikeDislike.objects.get(content_type=ContentType.objects.get_for_model(obj),
                                                  object_id=obj.id, user=request.user)
            if likedislike.vote is not self.vote_type:
                likedislike.vote = self.vote_type
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except LikeDislike.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            result = True

        return HttpResponse(
            json.dumps({
                "result": result,
                "like_count": obj.votes.likes().count(),
                "dislike_count": obj.votes.dislikes().count(),
                "sum_rating": obj.votes.sum_rating()
            }),
            content_type="application/json"
        )
