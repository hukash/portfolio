from django.conf.urls.defaults import *

urlpatterns = patterns('blackbook.views',
	(r'^$', 'index'),
	(r'^detail/(?P<slug>[-\w]+)/$', 'detail'),
	(r'^video/(?P<slug>[-\w]+)/$', 'show_video'),
    (r'^category/(?P<slug>[-\w]+)/$', 'show_category'),
)
