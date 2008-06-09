# -*- coding: UTF-8 -*-

from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponseNotFound
from django.core.urlresolvers import reverse

import pickle
from os.path import dirname

from blogapp.models import *

def blog_processor(request):
    context = {
        'options': options(),
        'tags': tag_list(),
        #'archive': archive(),
        'friends': friends(),
    }
    return context

def not_found(request, title='Error 404', message='Page not found'):
    t = get_template("service/404_message.html")
    c = RequestContext({'err_title': title, 'err_message': message})
    html = t.render(c)
    return HttpResponseNotFound(html)

def options():
    opt_list = [(opt.name, opt.value) for opt in Option.objects.all()]
    options = dict(opt_list)
    return options

def tag_list():
    max_size = int(options()['tag_cloud_font_size_max'])
    min_size = int(options()['tag_cloud_font_size_min'])

    tags = Tag.objects.all()
    popular = max([tag.post_set.count() for tag in tags])
    cloud = []

    for tag in tags:
        post_count = tag.post_set.count()
        #only add tags with posts
        #generates a list of dictionaries for easy usage in templates
        if post_count:
            size = max_size * post_count / popular
            #sets size to min_size if size < min_size
            size = (size < min_size) and min_size or size
            t = {}
            t['title'] = tag.title
            t['name'] = tag.name
            t['uri'] = reverse('blogapp.views.posts_by_tag', args=[tag.name])
            t['size'] = size
            t['post_count'] = post_count
            cloud.append(t)
    return cloud

def friends():
    f = open(dirname(__file__)+'/friends')
    friends = pickle.load(f)
    f.close()
    return friends
