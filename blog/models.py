from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password





class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # email = first_name + '.' + last_name + '@tudublin.ie'
    # email = models.CharField(first_name + '.' + last_name + '@tudublin.ie')
    # token =
    # password =
    is_admin = models.BooleanField(default=False, blank=True, null=True)
    created = models.DateField(default=timezone.now)
    updated = models.DateField(default=timezone.now)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.first_name + ' ' + self.last_name





class Category(models.Model):
    name = models.CharField(max_length=50)
    hashtag = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateField(default=timezone.now)
    updated = models.DateField(default=timezone.now)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    created = models.DateField(default=timezone.now)
    updated = models.DateField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title
