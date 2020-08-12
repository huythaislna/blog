from django.urls import path
from posts.views import posts_home, PostDetailView, category_view


urlpatterns = [
    path('', posts_home, name='home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('security/', category_view, name='category'),

]