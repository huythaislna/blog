from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    CATEGORIES = (
        ('security', 'Security'),
        ('programming', 'Programming'),
        ('network', 'Network'),
        ('news', 'News'),
        ('ebook', 'Ebook'),
        ('database', 'Database')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.CharField(choices=CATEGORIES, max_length=12)
    image = models.ImageField()
    title = models.CharField(max_length=255)
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={ "pk" : self.pk})

    @staticmethod
    def get_hot_post():
        return Post.objects.all()[:3]
