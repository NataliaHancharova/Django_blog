from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import UserRegistrationForm, CommentForm, PostForm
from django.contrib.auth import login
from django import forms
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method =='Post':
       form = UserRegistrationForm(request.Post)
       if form.is_valid():
           user = form.save()
           login(request, user)
           return redirect('post_list')
    else: 
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})    

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.post)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment_author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog_app/post_form.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog_app/post_form.html', {'form': form, 'post': post})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request,'blog_app/post_confrim_delete.html', {'post': post} )

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog_app/post_form.html', {'form': form})