from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Place, Post, Vocal, Comment

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'full_name', 'phone', 'city', 'neighborhood')
        read_only_fields = ('id',)

class PlaceSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Place
        fields = '__all__'
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')

class VocalSerializer(serializers.ModelSerializer):
    uploaded_by = UserSerializer(read_only=True)
    file = serializers.FileField(write_only=True)

    class Meta:
        model = Vocal
        fields = ('id', 'uploaded_by', 'file', 'duration_seconds', 'created_at')
        read_only_fields = ('id', 'uploaded_by', 'created_at')

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'content', 'created_at')
        read_only_fields = ('id', 'author', 'created_at')

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    audio = VocalSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'content', 'place', 'audio', 'is_public', 'created_at', 'updated_at', 'comments')
        read_only_fields = ('id', 'author', 'created_at', 'updated_at', 'comments')
