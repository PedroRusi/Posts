from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    post = Post.objects.filter(publicate=True)
    return render(request, 'index.html', {'posts': post})


def formCreate(request):
    return render(request, 'formCreate.html')


def formEdit(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'formEdit.html', {'id': id, 'post': post})


def create(request):
    post = Post()
    post.name = request.POST.get('name')
    post.text = request.POST.get('text')
    post.category = request.POST.get('category')
    post.image_url = request.POST.get('image_url')
    post.save()
    return HttpResponseRedirect("/")


def edit(request, id):
    post = Post.objects.get(id=id)
    post.name = request.POST.get('name')
    post.text = request.POST.get('text')
    post.category = request.POST.get('category')
    post.image_url = request.POST.get('image_url')
    post.save()
    return HttpResponseRedirect("/")


def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect("/")