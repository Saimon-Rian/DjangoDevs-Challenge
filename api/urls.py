from django.contrib import admin
from django.urls import path, include
from challenge.views import ArticleViewSets, AuthorViewSets
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register('authors', AuthorViewSets, basename='authors')
route.register('articles', ArticleViewSets, basename='article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
]
