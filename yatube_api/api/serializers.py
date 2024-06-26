from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from posts.models import Post, Group, Comment, Follow

User = get_user_model()


class AuthorMixin(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )


class PostSerializer(AuthorMixin, serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description',)


class CommentSerializer(AuthorMixin, serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate(self, attrs):
        validated_data = super(FollowSerializer, self).validate(attrs)

        if self.context['request'].user.following.filter(
            following__username=validated_data['following']
        ).exists():
            raise ValidationError('You are already following this user!')

        if (self.context['request'].user.username
                == validated_data['following'].username):
            raise ValidationError('You can not follow yourself!')

        return validated_data
