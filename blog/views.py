from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone

from .models import Post
from .forms import PostForm



def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    context = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)


@staff_member_required
def post_create(request):
    form = PostForm()
    if request.method == "POST":  
        form = PostForm(request.POST or None)
        print(form)
        if form.is_valid():  
            form.save()  
            return redirect('post_list')
        else:
            print('form is_valid failed')
            print(form.errors) 
    context = {
        'form':form
        }
    return render(request, 'blog/post_create.html', context)


@staff_member_required
def post_update(request, id):  
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance = post)  
    if form.is_valid():  
        form.save()  
        return redirect("post_list")  
    context = {
        'form': form
    }
    return render(request, 'blog/post_create.html', context)  


@staff_member_required
def post_delete(request, id):
    context ={}
 
    obj = get_object_or_404(Post, id = id)
 
 
    if request.method =="POST":
        obj.delete()
        return redirect("post_list")
 
    return render(request, "blog/post_delete.html", context)



def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {"post": post}
    return render(request, 'blog/post_detail.html', context) 