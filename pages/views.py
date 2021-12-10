from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import CommentForm, PostForm

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
    comments = Comment.objects.all()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    context = {'post': post, 'comments': comments, 'form': comment_form}
    return render(request, 'post_detail.html', context)

def create_post(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect(f'/posts/{new_post.id}')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'create_post.html', context)


def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/')


def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    if comment.user == request.user:
        comment.delete()
    
    return redirect(f'/posts/{comment.post.id}')