from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
from django.http import HttpResponse


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
    #return render(request,'blog/index.html',context={
     #   'title':'我的博客首页',
      #  'welcome':'欢迎访问我的博客首页'
   # })


def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html',context={'post': post})