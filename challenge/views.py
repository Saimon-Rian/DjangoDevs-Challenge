from rest_framework import viewsets
from .models import Article, Author
from .serializers import ArticleSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticated


class AuthorViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class ArticleViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
