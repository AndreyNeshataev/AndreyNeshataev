from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
# from django.views.generic.edit import DeleteView
from datetime import timedelta, date
from django.shortcuts import redirect
from .utils import ObjectPostMixin
from django.urls import reverse

from .forms import PostForm, TagForm
from .models import Tag, Post, PostImage


# Create your views here.

class PostList(ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(published=True)


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = PostImage.objects.filter(post_id=self.get_object().id)
        context['photos'] = photos
        return context


class AddPost(LoginRequiredMixin, ObjectPostMixin, CreateView):
    form_class = PostForm
    template_name = 'blog/add_post.html'
    raise_exception = True


class UpdatePost(LoginRequiredMixin, ObjectPostMixin, UpdateView):
    form_class = PostForm
    template_name = 'blog/update_post.html'
    queryset = Post.objects
    raise_exception = True

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = PostImage.objects.filter(post_id=self.get_object().id)
        context['photos'] = photos
        return context


class TagList(ListView):
    model = Tag
    template_name = 'blog/tags_list.html'
    context_object_name = 'tags'


class TagDetail(DetailView):
    model = Tag
    template_name = 'blog/tag_detail.html'
    context_object_name = 'tag'


class AddTag(LoginRequiredMixin, CreateView):
    form_class = TagForm
    template_name = 'blog/add_tag.html'
    success_url = reverse_lazy('tags_list')
    raise_exception = True


class ImageDelete(DeleteView):
    model = PostImage
    template_name = 'blog/delete.html'

    def post(self, *args, **kwargs):
        photo = PostImage.objects.filter(id=self.get_object().id)
        post = Post.objects.get(id=self.get_object().post_id)
        photo.delete()
        return redirect(post)







