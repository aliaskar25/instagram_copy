from rest_framework import serializers

from .models import (
    Post,
    PostImage, 
)


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('id', 'image', )


class PostSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'images', 'pub_date')

    def create(self, validated_data):
        user = self.context.get('request').user
        if user.is_anonymous:
            raise serializers.ValidationError({'error': 'you must login'})
        post = Post.objects.create(
            title=validated_data.get('title'),
            description=validated_data.get('description'),
            user=user
        )
        post.save()

        files = self.context.get('request').FILES
        for k, v in files.items():
            PostImage.objects.create(image=v, post=post)

        return post

    def update(self, instance, validated_data):
        user = self.context.get('request').user
        if user.is_anonymous or user.id != instance.user_id:
            raise serializers.ValidationError({'error': 'you must login or its not your post'})
        return super().update(instance, validated_data)
