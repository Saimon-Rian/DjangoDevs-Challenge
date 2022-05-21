from django.contrib import admin
from django.urls import path, include
from challenge.views import ArticleViewSets, AuthorViewSets, Register
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings


route = DefaultRouter()
route.register('authors', AuthorViewSets, basename='authors')
route.register('articles', ArticleViewSets, basename='articles')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin/register/', Register.as_view(), name='register'),
    path('api/admin/login/', TokenObtainPairView.as_view()),
    path('api/admin/login/refresh/', TokenRefreshView.as_view()),
    path('api/admin/', include(route.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
