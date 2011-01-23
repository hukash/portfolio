from django.conf.urls.defaults import *

urlpatterns = patterns('blackbook.views',
	(r'^$', 'index'),
	(r'^(?P<slug>[-\w]+)/$', 'detail'),
)
