from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def all_blogs(request):

    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-pub_date')
   
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})
