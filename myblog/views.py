from django.shortcuts import render, get_object_or_404


def post_list(request):
    """Display all posts."""
    posts = Post.published.all()
    return render(request, 'myblog/list.html', {'posts': posts})


def post_detail(request):
    """Display a specific post."""
    post = get_object_or_404(Post, slug=post, status='published',
                             publish_year=year, publish_month=month, publish_day=day)
    return render(request, 'myblog/detail.html', {'post': post})
