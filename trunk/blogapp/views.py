from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

from blogapp.models import *
from blogapp.utilities import not_found

def homepage(request):
    posts = Post.objects.all()[:5]
    template = get_template('blog.html')
    html = template.render(Context({'posts': posts,}))
    return HttpResponse(html)

def post_by_name(request, post_name, fragment_identifier):
    try:
        post = Post.objects.get(name=post_name)
        comments = post.comment_set.all()
        template = get_template('blog.html')

        context = Context({
            'posts': [post],
            'comments': comments,
            'title': post.title + " // ",
            })
        html = template.render(context)
        return HttpResponse(html)
    except:
        return not_found(request, message="Sorry, the requested post does not exist.")

def posts_by_tag(request, tag_name):
    try:
        tag = Tag.objects.get(name=tag_name)
        posts = tag.post_set.all()[:5]
        template = get_template('blog.html')
        html = template.render(Context({'posts': posts,}))
        return HttpResponse(html)
    except:
        return not_found(request, message="Sorry, the tag you are searching for does not exist.")

def posts_by_date(request, year, month):
    posts = Post.objects.filter(date__year=year, date__month=month)[:5]
    if not posts:
        return not_found(request, message="Sorry, there are no posts written that month.")
    template = get_template('blog.html')
    html = template.render(Context({'posts': posts,}))
    return HttpResponse(html)
