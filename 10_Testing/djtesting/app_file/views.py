from _csv import reader
from django.shortcuts import render
from blog.models import Post
from app_file.forms import UploadPostForm
from django.shortcuts import redirect


def update_posts(request):
    if request.method == 'POST':
        upload_file_form = UploadPostForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            post_file = upload_file_form.cleaned_data['file'].read()
            post_str = post_file.decode('utf-8').split('\n')
            csv_reader = reader(post_str, delimiter=',', quotechar='"')
            for row in csv_reader:
                if row:
                    Post.objects.create(title=row[0], slug=row[1], article=row[2], published=True)
            upload_file_form.save()
            return redirect('blog_list')
    else:
        upload_file_form = UploadPostForm

    context = {
        'form': upload_file_form
    }
    return render(request, 'posts/upload_post_file.html', context=context)








