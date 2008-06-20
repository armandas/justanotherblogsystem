from django.conf.urls.defaults import *
import this as th

urlpatterns = patterns('trunk',
    (r'^google0338e6835e33fa63.html$', 'dummy.verification'),
    (r'^', include('blogapp.urls')),
    (r'^admin/', include('django.contrib.admin.urls')),
)