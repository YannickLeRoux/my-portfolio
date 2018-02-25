from django.utils import timezone
from .models import Post
from django.views.generic import ListView

class Blog(ListView):
    model = Post
    template_name = 'portfolio/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_posts'] = Post.objects.order_by('-published_date')
        return context
