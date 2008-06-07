from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

from blogapp.models import *
from blogapp.utilities import not_found

#fetch blog options
options = {}
opts = Option.objects.all()
for opt in opts:
    options[opt.name] = opt.value

def homepage(request):
    posts = Post.objects.all()[:5]
    return render_to_response('blog.html', {'posts': posts, 'options': options,})

def post_by_name(request, post_name):
    try:
        post = Post.objects.get(name=post_name)
        comments = post.comment_set.all()
        context = {
            'posts': [post],
            'comments': comments,
            'title': post.title + " // ",
            'options': options,
            }
        return render_to_response('blog.html', context)
    except:
        return not_found(request, message="Sorry, the requested post does not exist.")

def posts_by_tag(request, tag_name):
    try:
        tag = Tag.objects.get(name=tag_name)
        posts = tag.post_set.all()[:5]
        return render_to_response('blog.html', {'posts': posts, 'options': options,})
    except:
        return not_found(request, message="Sorry, the tag you are searching for does not exist.")

def posts_by_date(request, year, month):
    posts = Post.objects.filter(date__year=year, date__month=month)[:5]
    if posts:
        return render_to_response('blog.html', {'posts': posts, 'options': options,})
    else:
        return not_found(request, message="Sorry, there are no posts written that month.")

def feed(request, feed_type):
    posts = Post.objects.all()[:10]
    template = "feeds/%s.xml" % feed_type
    mimetype = "application/%s+xml" % feed_type
    updated = posts[0].date #used by atom
    context = {
        'posts': posts,
        'updated': updated,
        'options': options,
        }

    return render_to_response(template, context)#, mimetype=mimetype)
