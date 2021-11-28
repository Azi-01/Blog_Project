from django.db import models
from django.db.models.fields.related import ForeignKey
from accounts.models import CustomUser
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.title) > 100:
            return self.title[0].title() + self.title[1:50] + '...'
        else:
            return self.title[0].title() + self.title[1:]
    
    def get_absolute_url(self):
        reverse('posts/', kwargs={'id': self.id})
    
    @property
    def content_thumb(self):
        if len(self.content) > 100:
            return self.content[0].title() + self.content[1:300] + '...'
        else:
            return self.content[0].title() + self.content[1:]
    
    @property
    def get_content(self):
        return self.content[0].title() + self.content[1:]


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)