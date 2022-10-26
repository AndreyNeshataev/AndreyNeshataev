from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='blog_list'),
    path('post/add_post/', AddPost.as_view(), name='add_post_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update_post', UpdatePost.as_view(), name='update_post_url'),
    path('tags/', TagList.as_view(), name='tags_list'),
    path('tags/add_tag/', AddTag.as_view(), name='add_tag_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('<int:pk>/photo_delete', ImageDelete.as_view(), name='photo_delete_url'),
]
