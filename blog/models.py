from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
from django.utils.text import Truncator
from markdown import markdown

class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=256)
    category = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        truncated_message = Truncator(self.text)
        return truncated_message.chars(200)
    
    def get_message_as_markdown(self):
        return mark_safe(markdown(self.text, safe_mode='escape'))

# Create your models here.
