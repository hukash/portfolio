from django.conf.urls.defaults import *

urlpatterns = patterns('blackbook.views',
	(r'^$', 'index'),
	(r'^videos/$', 'show_video'),
	(r'^video/(?P<slug>[-\w]+)/$', 'show_video'),
    (r'^category/(?P<slug>[-\w]+)/$', 'show_category'),
)
