from django.urls import path
from posts.views import (
    posts_home, PostDetailView, 
    category_view, login_view, 
    register_view, logout_view, 
    update_view, PostCreateView
)                        


urlpatterns = [
    path('', posts_home, name='home'),
    path('posts/create/', PostCreateView.as_view(), name='post-update'),
    path('security/', category_view, name='category'),
    path('login/', login_view, name="user-login"),
    path('register/', register_view, name="user-register"),
    path('logout/', logout_view, name="user-logout"),
    path('posts/<slug:slug>/edit', update_view, name='post-update'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]