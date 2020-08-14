from django.dispatch import receiver
from django.db.models.signals import pre_save
from posts.models import Post

@receiver(pre_save, sender=Post)
def add_author_to_post(sender):