from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

    def posts(self):
        return self.get_queryset().filter(content_type__model='post').order_by('-posts__publication_date')

    def comments(self):
        return self.get_queryset().filter(content_type__model='comment').order_by('-comments__created_date')


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )

    vote = models.SmallIntegerField(verbose_name="Голос", choices=VOTES)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.TextField()
    publication_date = models.DateField(default=timezone.now)
    votes = GenericRelation(LikeDislike, related_query_name='posts')

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return '{}|{}'.format(self.title, self.author)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    votes = GenericRelation(LikeDislike, related_query_name='posts')

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class CodeExamples(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class EulerProblem(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    code_lines = models.IntegerField()
    description = models.TextField()
    solution = models.TextField()

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    capital = models.FloatField(default=0)
    assets = models.IntegerField(default=0)
    chart = models.ImageField(blank=True, null=True)
    profitability = models.FloatField(default=0)
    profit = models.FloatField(default=0)
    standartandpoor = models.ImageField(blank=True, null=True)
    revenue_image = models.ImageField(blank=True, null=True)


class Stock(models.Model):
    id = models.IntegerField(primary_key=True)
    symbol = models.CharField(max_length=100)
    title = models.CharField(max_length=100, null=True, blank=True)
    exchange = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    buy_price = models.FloatField(default=0)
    curent_price = models.FloatField(null=True, blank=True)
    dividend = models.FloatField(null=True, blank=True )
    poe = models.FloatField(default=1)
    amount = models.IntegerField(default=1)
    share = models.FloatField(null=True, blank=True)
    invested = models.FloatField(null=True, blank=True)
    end_value = models.FloatField(null=True, blank=True)
    profit = models.FloatField(default=0)

    def __str__(self):
        return self.symbol
