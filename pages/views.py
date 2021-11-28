from django.core import paginator
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': posts, 'page_obj': page_obj}
    return render(request, 'home.html', context)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'post_detail.html', context)
