from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.bloghomepage, name='bloghomepage'),

    #causing issues
    
    #path('<title:post>/', views.post_single, name='post_single'),

]

 #Test Blog Post