from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path

from mainsite import views
from mainsite.models import Comment, Post, LikeDislike


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('apps_list', views.apps_list, name='apps_list'),
    path('apps_list/blog', views.blog_page, name='blog_page'),

    path('apps_list/blog/post_new', views.post_new, name='post_new'),
    path('apps_list/blog/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('apps_list/blog/post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('apps_list/blog/post/<pk>/remove/', views.post_remove, name='post_remove'),

    path('apps_list/blog/comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('apps_list/blog/comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('apps_list/blog/comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),

    path('apps_list/programming/', views.programming, name='programming'),
    path('apps_list/programming/code_examples/', views.code_examples, name='code_examples'),
    path('apps_list/programming/euler_problems/', views.euler_problems, name='euler_problems'),

    # path('apps_list/blog/post/<int:pk>/like/$',login_required(views.VotesView.as_view(model=Post, vote_type=LikeDislike.LIKE)),
    #     name='post_like'),
    # path('apps_list/blog/post/<int:pk>/dislike/$',login_required(views.VotesView.as_view(model=Post, vote_type=LikeDislike.DISLIKE)),
    #     name='post_dislike'),
    # path('apps_list/blog/post/(?P<pk>\d+)/like/$',login_required(views.VotesView.as_view(model=Post, vote_type=LikeDislike.LIKE)),
    #     name='article_like'),
    # path('apps_list/blog/post/(?P<pk>\d+)/like/$',login_required(views.VotesView.as_view(model=Post, vote_type=LikeDislike.LIKE)),
    #     name='article_like'),

    url(r'^post/(?P<pk>\d+)/like/$',
        login_required(views.VotesView.as_view(model=Post, vote_type=LikeDislike.LIKE)),
        name='post_like'),
    url(r'^post/(?P<pk>\d+)/dislike/$',
        login_required(views.VotesView.as_view(model=Post, vote_type=LikeDislike.DISLIKE)),
        name='post_dislike'),
    url(r'^post/(?P<pk>\d+)/like/$',
        login_required(views.VotesView.as_view(model=Comment, vote_type=LikeDislike.LIKE)),
        name='comment_like'),
    url(r'^post/(?P<pk>\d+)/dislike/$',
        login_required(views.VotesView.as_view(model=Comment, vote_type=LikeDislike.DISLIKE)),
        name='comment_dislike'),

]
