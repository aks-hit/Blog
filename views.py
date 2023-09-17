from django.shortcuts import render ,get_object_or_404
from blogs.models import Post
# Create your views here.
def allpost(request):
    post=Post.objects
    return render(request,'posts.html',{'post':post})
def detail(request,blogs_id):
    detail = get_object_or_404(Post,pk = blogs_id)
    return render(request, 'details.html' ,{'post':detail})