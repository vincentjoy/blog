from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404, HttpResponseRedirect
from django.template import loader
from .models import Post, Tag
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    all_posts = Post.objects.all().order_by('-id')
    paginator = Paginator(all_posts, 4, orphans=2)
    page_number = request.GET.get('p', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/index.html', {'posts': page_obj})

def post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            posturl = reverse('post', args=[id])
            return HttpResponseRedirect(posturl)
    form = CommentForm()
    return render(request, 'posts/post.html', {'post_dict': post, 'form': form, 'comments': post.comment_set.all()})

def tags(request, id):
    tag = Tag.objects.get(id=id)
    return render(request, 'posts/tags.html', {'tags': tag.post_set.all()})

def search(request):
    query = request.GET.get('query', None)
    posts = Post.objects.filter(post_title__icontains=query)
    return render(request, 'posts/search.html', {'posts': posts})