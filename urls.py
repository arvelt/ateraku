from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^api/v1/events/(?P<id>\d+)', 'api.views.events'),
	url(r'^api/v1/events', 'api.views.events_list'),
	url(r'^api/v1/', 'api.views.home'),
    url(r'^$', 'api.hello.views.home'),
)
