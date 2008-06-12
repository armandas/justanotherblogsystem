from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils.translation import ugettext as _

from blogapp.models import *
from blogapp.utilities import *
#from blogapp.forms import CommentForm

BLOG_TPL = 'blog.html'

#def comment(request):
    #form = CommentForm()
    #return render_to_response('blank.html', {'source': form.as_p()}, context_instance=RequestContext(request))

def homepage(request):
    posts = Post.objects.all()[:5]
    context = {'posts': posts,}
    return render_to_response(BLOG_TPL, context, context_instance=RequestContext(request))

def post_by_name(request, post_name):
    try:
        post = Post.objects.get(name=post_name)
        comments = post.comment_set.all()
        context = {
            'posts': [post],
            'comments': comments,
            'title': post.title,
            }
        return render_to_response(BLOG_TPL, context, context_instance=RequestContext(request))
    except:
        return not_found(request, message=_("Sorry, the requested post does not exist."))

def posts_by_tag(request, tag_name):
    try:
        tag = Tag.objects.get(name=tag_name)
        posts = tag.post_set.all()[:5]
        context = {'posts': posts,}
        return render_to_response(BLOG_TPL, context, context_instance=RequestContext(request))
    except:
        return not_found(request, message=_("Sorry, the tag you are searching for does not exist."))

def posts_by_date(request, year, month):
    posts = Post.objects.filter(date__year=year, date__month=month)[:5]
    if posts:
        context = {'posts': posts,}
        return render_to_response(BLOG_TPL, context, context_instance=RequestContext(request))
    else:
        return not_found(request, message=_("Sorry, there are no posts written that month."))

def feed(request, feed_type):
    posts = Post.objects.all()[:10]
    template = "feeds/%s.xml" % feed_type
    m_type = "application/xml"#"application/%s+xml" % feed_type
    updated = posts[0].date #used by atom
    context = {
        'posts': posts,
        'updated': updated,
        'options': options(),
        }
    return render_to_response(template, context, mimetype=m_type)
