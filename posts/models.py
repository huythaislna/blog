from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from ckeditor.fields import RichTextField

from core.utils import generate_slug
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
    slug = models.SlugField(unique=True, max_length=255)
    category = models.CharField(choices=CATEGORIES, max_length=12)
    image = models.ImageField()
    title = models.CharField(max_length=255)
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={ "slug" : self.slug})

    def save(self, *args, **kwargs):
        generate_slug(self)
        return super().save(*args, **kwargs)