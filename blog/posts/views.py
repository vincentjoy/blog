from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404, HttpResponseRedirect
from django.template import loader
from .models import Post, Tag
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def home(request):
    all_posts = Post.objects.all().order_by('-id')
    paginator = Paginator(all_posts, 4, orphans=2)
    page_number = request.GET.get('p', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/index.html', {'posts': page_obj, 'total': all_posts.count()})

class HomeView(ListView):
    model = Post
    template_name = 'posts/index.html'
    ordering = ['-id']
    context_object_name = 'posts'

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

class PostView(DetailView):
    model = Post
    template_name = 'posts/post.html'
    context_object_name = 'post_dict'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        context['comments'] = self.object.comment_set.all()
        return context

    def post(self, request, pk):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            posturl = reverse('post', args=[self.object.id])
            return HttpResponseRedirect(posturl)

def tags(request, id):
    tag = Tag.objects.get(id=id)
    return render(request, 'posts/tags.html', {'tags': tag.post_set.all()})

def search(request):
    query = request.GET.get('query', None)
    page_number = request.GET.get('p', 1)
    posts = Post.objects.filter(Q(post_title__icontains=query) | Q(post_content__icontains=query)).order_by('-id')
    paginator = Paginator(post, 4)
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/search.html', {'posts': page_obj, 'query': query, 'total': posts.count()})