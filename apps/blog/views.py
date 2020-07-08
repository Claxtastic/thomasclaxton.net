from django.shortcuts import render
from apps.blog.models import Post, Comment
from apps.blog.forms import CommentForm
# from .forms import CommentForm

# blog mini view, ordered by most recent
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts" : posts,
    }

    return render(request, "blog_index.html", context)

# get all posts in a given category
def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        'category' : category,
        'posts' : posts
    }

    return render(request, 'blog_category.html', context)

# view full post given post index pk
def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    
    # check for new comments on this post
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
        # form received is valid, create a comment
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    # get the comment for this post
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form" : form,
    }

    return render(request, "blog_detail.html", context)
