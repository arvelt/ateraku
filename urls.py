from django.conf.urls import patterns, include, url
from api.views.events import EventView, EventsView

urlpatterns = patterns('',
	url(r'^api/v1/events/(?P<id>\d+)', EventView.as_view()),
	url(r'^api/v1/events', EventsView.as_view()),
	url(r'^api/v1/', 'api.views.home'),
    url(r'^$', 'api.hello.views.home'),
)
