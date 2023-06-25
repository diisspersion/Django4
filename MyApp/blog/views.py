from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)


    context = {'post': post}
    return render(request, 'blog/index.html', context=context)


