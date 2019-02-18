from rest_framework import generics

from .models import Category, Tag, Article
from .serializers import CategorySerializer, TagSerializer, ArticleSerializer, ArticlePOSTSerializer


class CategoryListAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=True)

class CategoryDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=True)


class TagListAPIView(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.filter(status=True)

class TagDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.filter(status=True)



class ArticleListAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.filter()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ArticlePOSTSerializer

        return ArticleSerializer


class ArticleDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleSerializer

        return ArticlePOSTSerializer