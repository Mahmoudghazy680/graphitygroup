from django.shortcuts import render , get_object_or_404 
from django.http import HttpResponse
from .models import *

# Create your views here.

def post_list(request):
   post_list = Post.objects.all()  
   context = {"posts" : post_list}
   return render(request , 'post/post_list.html' , context) 


def post_detail(request, id):
   post_detail = Post.objects.get(id=id)
   context = {'post' : post_detail}
   return render(request , 'post/post_detail.html' , context) 