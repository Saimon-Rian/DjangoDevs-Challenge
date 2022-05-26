from django.contrib import admin
from django.urls import path, include
from challenge.views import ArticleViewSets, AuthorViewSets, Register, AnonymousArticlesViewSets
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings


route = DefaultRouter()
route.register('api/admin/authors', AuthorViewSets, basename='authors')
route.register('api/admin/articles', ArticleViewSets, basename='articles')
route.register('api/articles', AnonymousArticlesViewSets, basename='AnonymousArticles')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/login/refresh/', TokenRefreshView.as_view()),
    path('api/sign-up/', Register.as_view(), name='sign-up'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
