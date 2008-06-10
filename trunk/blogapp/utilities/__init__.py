from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponseNotFound
from django.core.urlresolvers import reverse

from blogapp.models import *
from blogapp.utilities import friends

def blog_processor(request):
    context = {
        'options': options(),
        'tags': tag_list(),
        #'archive': archive(),
        'friends': friends.get_list(),
    }
    return context

def not_found(request, title='Error 404', message='Page not found'):
    t = get_template("service/404_message.html")
    c = RequestContext({'err_title': title, 'err_message': message})
    html = t.render(c)
    return HttpResponseNotFound(html)

def options():
    """Returns a dictionary of options."""
    opt_list = [(opt.name, opt.value) for opt in Option.objects.all()]
    options = dict(opt_list)
    return options

def tag_list():
    """Returns a list of dictionaries containing:
        tag.title
        tag.name
        tag.uri
        tag.size (for tag cloud)
        tag.post_count
    """
    max_size = int(options()['tag_cloud_font_size_max'])
    min_size = int(options()['tag_cloud_font_size_min'])

    tags = Tag.objects.all()
    popular = max([tag.post_set.count() for tag in tags])
    cloud = []

    for tag in tags:
        post_count = tag.post_set.count()
        #only add tags with posts
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