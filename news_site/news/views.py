from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

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
    context = {}
    if request.method == "POST":
        title = request.POST.get("title")
        slug = request.POST.get("slug")
        content = request.POST.get("content")
        article_object = Post.objects.create(title=title, slug=slug, content=content)
        context['object'] = article_object
        context['created'] = True
        return render(request, "articles/create.html", context=context)


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

