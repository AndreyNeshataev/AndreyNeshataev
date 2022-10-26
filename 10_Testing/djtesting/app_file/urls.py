from django.urls import path
from app_file.views import update_posts


urlpatterns = [
    path('update_posts/', update_posts, name='update_posts_url'),
]