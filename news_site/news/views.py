from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post, PostImage


def news_view(request):
    posts = Post.objects.all()
    photos = PostImage.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
        'photos': photos,
    })


def post_details(request, id):
    post = get_object_or_404(Post, id)
    photos = PostImage.objects.filter(post=post)
    print(post, photos)
    return render(request, 'post_detail.html', {
        'posts': post,
        'photos': photos,
    })


@login_required
def post_create_view(request):
    form = PostForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        post_object = form.save()
        context['form'] = PostForm()
        return redirect(post_object.get_absolute_url())
    return render(request, "news/create.html", context=context)

# from django.views import generic
# from .models import Post, PostImage
#
#
# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'
#
#
# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     # queryset = PostImage.objects.all()
#     template_name = 'index.html'
#     print(queryset)

