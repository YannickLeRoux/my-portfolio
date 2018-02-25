from django.urls import path

from .views import Blog

app_name = 'blog'

urlpatterns = [
        path('', Blog.as_view(), name='blog'),
        ]
