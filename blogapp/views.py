from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.utils.html import escape
from django.core.paginator import Paginator, InvalidPage
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

from blogapp.models import *
from blogapp.utilities import *
from blogapp.forms import CommentForm

from datetime import datetime

BLOG_TPL = 'blog.html'
P_LIMIT = int(options('posts_per_page'))

def homepage(request):
    pg = Paginator(Post.objects.all(), P_LIMIT)
    page_q = int(request.GET.get('page', 0)) or 1
    try:
        p = pg.page(page_q)
        posts = p.object_list
    except InvalidPage:
        return not_found(request, message=_("Sorry, the page does not exist."))
    context = {'posts': posts, 'page': p}
    return render_to_response(BLOG_TPL, context, context_instance=RequestContext(request))

def post_by_name(request, post_name):
    try:
        post = Post.objects.get(name=post_name)
    except ObjectDoesNotExist:
        return not_found(request, message=_("Sorry, the requested post does not exist."))

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            p = Comment(author_name=form.cleaned_data['author_name'],
                        author_email=form.cleaned_data['author_email'],
                        author_website=form.cleaned_data.get('author_website', ''),
                        content=escape(form.cleaned_data['comment']),
                        date=datetime.now(),
                        author_ip=request.META['REMOTE_ADDR'],
                        post=post
                        )
            p.save()
            return HttpResponseRedirect(reverse('blogapp.views.post_by_name', args=[post.name]))
    else:
        form = CommentForm()

    comments = post.comment_set.all()
    context = {
        'posts': [post],
        'comments': comments,
        'title': post.title,
        'comment_form': form,
        }
    return render_to_response(BLOG_TPL, context, context_instance=RequestContext(request))

def posts_by_tag(request, tag_name):
    try:
        tag = Tag.objects.get(name=tag_name)
        pg = Paginator(tag.post_set.all(), P_LIMIT)
        page_q = int(request.GET.get('page', 0)) or 1
        try:
            p = pg.page(page_q)
            posts = p.object_list
        except InvalidPage:
            return not_found(request, message=_("Sorry, the page does not exist."))
        context = {'posts': posts, 'page': p}
        return render_to_response(BLOG_TPL, context, context_instance=RequestContext(request))
    except ObjectDoesNotExist:
        return not_found(request, message=_("Sorry, the tag you are searching for does not exist."))

def posts_by_date(request, year, month):
    posts = Post.objects.filter(date__year=year, date__month=month)
    if posts:
        pg = Paginator(posts, P_LIMIT)
        page_q = int(request.GET.get('page', 0)) or 1
        try:
            p = pg.page(page_q)
            posts = p.object_list
        except InvalidPage:
            return not_found(request, message=_("Sorry, the page does not exist."))
        context = {'posts': posts, 'page': p}
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
