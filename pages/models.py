from django.db import models
from accounts.models import CustomUser
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=CASCADE)
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
            return self.content[0].title() + self.content[1:100] + '...'
        else:
            return self.content[0].title() + self.content[1:]
    
    @property
    def get_content(self):
        return self.content[0].title() + self.content[1:]