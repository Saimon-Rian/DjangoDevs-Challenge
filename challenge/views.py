from rest_framework import viewsets
from .models import Article, Author
from .serializers import ArticleSerializer, AuthorSerializer


class AuthorViewSets(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class ArticleViewSets(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
