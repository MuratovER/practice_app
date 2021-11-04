from rest_framework.serializers import ModelSerializer

from mainsite.models import Post, UserPostRelation


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

