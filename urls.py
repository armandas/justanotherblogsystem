from django.conf.urls.defaults import *

urlpatterns = patterns('trunk',
    (r'^google0338e6835e33fa63.html$', 'dummy.verification'),
    (r'^', include('blogapp.urls')),
)

urlpatterns += patterns('trunk',
    #(r'admin/friends/([0-9]+/)?$', 'blogapp.views.admin.manage_friends'),
    (r'^admin/', include('django.contrib.admin.urls')),
)