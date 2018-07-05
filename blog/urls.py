from django.urls import path

from .views import Blog, PostDetail, PostList, SinglePost

app_name = 'blog'

urlpatterns = [
        path('', Blog.as_view(), name='blog'),
        path('api/post/<slug:slug>', SinglePost.as_view(), name='single_post_api'),
        path('api/post', PostList.as_view(), name='api-postlist'),
        path('<slug:slug>/', PostDetail.as_view(), name='post')
        ]
