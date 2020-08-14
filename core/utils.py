from django.utils.text import slugify
import string
import random

def generate_slug(instance):
    alphas = string.ascii_lowercase + string.digits
    length = 6
    random_string = "".join([random.choice(alphas) for _ in range(length)])
    slug = slugify(instance.title)
    model = type(instance)
    if model.objects.filter(slug=slug).exists() and not slug == instance.slug:
        slug += random_string
    instance.slug = slug