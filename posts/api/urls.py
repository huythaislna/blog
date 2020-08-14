from rest_framework.routers import DefaultRouter
from posts.api.views import PostViewSet, ImageUpdateAPIView
from django.urls import path, include


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='api-post')


urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/image', ImageUpdateAPIView.as_view())
]