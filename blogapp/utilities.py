from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponseNotFound
from django.shortcuts import render_to_response

from blogapp.models import *

def not_found(request, title='Error 404', message='Page not found'):
    t = get_template("service/404_message.html")
    c = Context({'title': title, 'message': message})
    html = t.render(c)
    return HttpResponseNotFound(html)

def feed(request, feed_type):
    posts = Post.objects.all()[:10]
    template = "feeds/%s.xml" % feed_type
    mimetype = "application/%s+xml" % feed_type
    updated = posts[0].date #used by atom

    return render_to_response(template, {'posts': posts, 'updated': updated})#, mimetype=mimetype)