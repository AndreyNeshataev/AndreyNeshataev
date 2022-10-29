from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from .forms import PostForm
from .models import Post, PostImage


class ObjectPostMixin(View):
    model = None
    model_form = None
    template = None

    def post(self, request, *args, **kwargs):
        obj = self.get_form()
        files = request.FILES.getlist('photos')
        if obj.is_valid():
            if request.path.endswith('/update_post'):
                post_obj = Post.objects.get(slug=kwargs['slug'])
                post_obj.title = obj.cleaned_data['title']
                post_obj.article = obj.cleaned_data['article']
                post_obj.published = obj.cleaned_data['published']
                tag_list = obj.cleaned_data['tags']
                post_obj.tags.set(tag_list)
                post_obj.save()
                if files:
                    for fs in files:
                        PostImage.objects.create(post=post_obj, photo=fs)
                return redirect(post_obj)
            post_obj = obj.save()
            post_obj.author = request.user
            post_obj = obj.save()
            for fs in files:
                PostImage.objects.create(post=post_obj, photo=fs)
            return redirect(post_obj)
        return render(request, self.template, {'form': obj})






