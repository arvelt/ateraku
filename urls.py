from django.conf.urls import patterns, include, url
from api.views.events import EventsView

urlpatterns = patterns('',
	url(r'^api/v1/events/(?P<id>\d+)', EventsView.as_view()),
	url(r'^api/v1/events', 'api.views.events_list'),
	url(r'^api/v1/', 'api.views.home'),
    url(r'^$', 'api.hello.views.home'),
)
