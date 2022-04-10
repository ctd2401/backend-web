from rest_framework import serializers
from django.db import models
from blog.models import Article
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author', 'date' ]
    