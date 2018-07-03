from django.utils import timezone
from .models import Post
from django.views.generic import ListView, DetailView
from .serializers import PostSerializer
from rest_framework import generics

class Blog(ListView):
    model = Post
    template_name = 'portfolio/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_posts'] = Post.objects.order_by('-published_date')
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'portfolio/post.html'
    slug_url_kwarg = 'slug'

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
