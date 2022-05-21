import uuid
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import Article, Author
from .serializers import GenericArticleSerializer, AuthorSerializer, ArticleAnonSerializer, LoggedArticleSerializer, \
    RegisterSerializer
from rest_framework.permissions import IsAuthenticated


class AuthorViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class ArticleViewSets(viewsets.ModelViewSet):
    serializer_class = GenericArticleSerializer
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return LoggedArticleSerializer
        else:
            return ArticleAnonSerializer


class Register(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",

                "User": serializer.data}, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
