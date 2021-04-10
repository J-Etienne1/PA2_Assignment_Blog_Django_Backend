from django.shortcuts import render, get_object_or_404
from .models import User
from .models import Category
from .models import Post

# Create your views here.

def bloghomepage(request):
    all_Users = User.objects.all()
    all_Category = Category.objects.all()
    all_Post = Post.objects.all()


    return render(request, 'index.html', {'post': all_Post, 'users': all_Users, 'category': all_Category})


#causing issues

#def post_single(request, post):
#    post = get_object_or_404(Post, Title=post)
#    return render(request, 'single.html', {'post': post})
