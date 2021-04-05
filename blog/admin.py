from django.contrib import admin
from . import models
# Register your models here.

from .models import User
from .models import Category
from .models import Post


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','hashtag',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('owner', 'category', 'title')


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post,PostAdmin)


