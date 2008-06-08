from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponseNotFound
from django.core.urlresolvers import reverse

from blogapp.models import *

def blog_processor(request):
    context = {
        'options': options(),
        'tags': tag_cloud(),
        #'archive': archive(),
        #'friends': friends(),
    }
    return context

def not_found(request, title='Error 404', message='Page not found'):
    t = get_template("service/404_message.html")
    c = RequestContext({'err_title': title, 'err_message': message})
    html = t.render(c)
    return HttpResponseNotFound(html)

def options():
    options = {}
    opts = Option.objects.all()
    for opt in opts:
        options[opt.name] = opt.value
    return options

def tag_cloud():
    max_size = 20
    min_size = 10
    pattern = '<a href="%s" style="font-size: %dpx" title="(%d)">%s</a>'

    tags = Tag.objects.all()
    popular = max([tag.post_set.count() for tag in tags])
    cloud = []

    for tag in tags:
        url = reverse('blogapp.views.posts_by_tag', args=[tag.name])
        posts = tag.post_set.count()
        size = max_size * posts / popular
        #sets size to min_size if size < min_size
        size = (size < min_size) and min_size or size
        cloud.append(pattern % (url, size, posts, tag.title))
    return cloud