from django.conf.urls.defaults import *

urlpatterns = patterns('root',
    (r'^', include('blogapp.urls')),
    (r'^admin/', include('django.contrib.admin.urls')),
)