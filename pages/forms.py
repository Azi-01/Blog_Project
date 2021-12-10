from django.forms import ModelForm
from .models import Comment, Post

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': ''}

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {'content': ''}