from django.urls import path

from .views import Blog, PostDetail, PostList

app_name = 'blog'

urlpatterns = [
        path('', Blog.as_view(), name='blog'),
        path('api/post', PostList.as_view(), name='api-postlist'),
        path('<slug:slug>/', PostDetail.as_view(), name='post')
        ]
