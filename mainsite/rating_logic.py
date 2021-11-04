from django.db.models import Avg

from mainsite.models import UserPostRelation


def set_rating(book):
    rating = UserPostRelation.objects.filter(book=book).aggregate(rating=Avg('rate')).get('rating')
    book.rating = rating
    book.save()