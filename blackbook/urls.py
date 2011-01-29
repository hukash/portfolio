from django.conf.urls.defaults import *

urlpatterns = patterns('blackbook.views',
	(r'^$', 'index'),
	(r'^detail/(?P<slug>[-\w]+)/$', 'detail'),
    (r'^category/(?P<slug>[-\w]+)/$', 'show_category'),
)
