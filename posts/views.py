from django.shortcuts import render
from django.views.generic import DetailView, UpdateView
from posts.models import Post
from posts.forms import UserModelForm, UserRegisterForm, PostUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
# Create your views here.

#@login_required(login_url='/login/')
def posts_home(request):
    hot_posts = Post.get_hot_post()
    posts = Post.objects.all()
    recent_posts = posts[:4]
    context = { 
        "hot_posts" : hot_posts,
        'recent_posts': recent_posts,
    }
    return render(request, 'index.html', context)

class PostUpdateView(UpdateView):
    model = Post
    #form_class = PostUpdateForm
    template_name = "update.html"
    fields = "__all__"


class PostDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
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


def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.set_password(form.cleaned_data.get('password'))
        instance.save()
        return redirect('/login/')
    return render(request, "login.html", { "form" : form })


def login_view(request):
    form = UserModelForm(request.POST or None)
    error = form.errors.as_text()[12:]
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")
    return render(request, "login.html", { "form": form, "error": error })