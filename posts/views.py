from django.shortcuts import render
from django.views.generic import DetailView
from posts.models import Post
# Create your views here.


def posts_home(request):
    hot_posts = Post.get_hot_post()
    posts = Post.objects.all()
    recent_posts = posts[:4]
    context = { 
        "hot_posts" : hot_posts,
        'recent_posts': recent_posts,
    }
    return render(request, 'index.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

def category_view(request):
    posts = Post.objects.all().order_by("-created_at")
    hot_post = Post.objects.first()
    recent_posts = posts[:4]
    context = { 
        'recent_posts': recent_posts,
        'hot_post': hot_post
    }
    return render(request, 'category.html', context)