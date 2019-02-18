from rest_framework import serializers
from .models import Category, Tag, Article


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )
        read_only_fields = (
            'id',
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
        )
        read_only_fields = (
            'id',
        )

class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'body',
            'category',
            'tags',
        )
        read_only_fields = (
            'id',
        )


class ArticlePOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'body',
            'category',
            'tags',
        )
        read_only_fields = (
            'id',
        )