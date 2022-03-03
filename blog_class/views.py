from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)


class PostListView(ListView):
    queryset = Post.objects.all()


class PostDetailView(DetailView):
    queryset = Post.objects.all()

    def get_object(self):                        # otherwise specify pk in url instead of id
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)  


class PostCreateView(CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = '../blog'

    def form_valid(self, form):
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = '../'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)


class PostDeleteView(DeleteView):
    queryset = Post.objects.all()
    template_name = 'blog/post_delete.html'
    success_url = '../'

    def get_object(self):                        # otherwise specify pk in url instead of id
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)  
