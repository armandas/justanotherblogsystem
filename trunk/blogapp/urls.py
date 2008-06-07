from django.conf.urls.defaults import *

urlpatterns = patterns('blogapp.views',
    (r'^$', 'homepage'),
    (r'^([a-z0-9-]+).html(#[a-z]+)?$', 'post_by_name'),
    (r'^tags/([a-z0-9-]+)/$', 'posts_by_tag'),
    (r'^archive/([0-9]{4})/([0-9]{2})/$', 'posts_by_date'),
)

urlpatterns += patterns('blogapp.utilities',
    (r'feed/(rss|atom)/$', 'feed'),
)