from django.conf.urls import patterns, url
from api.views import EventsView, EventView, UsersView, UserView

urlpatterns = patterns('',
	url(r'^api/v1/events/(?P<id>\d+)', EventView.as_view()),
	url(r'^api/v1/events', EventsView.as_view()),
	url(r'^api/v1/users/(?P<id>\d+)', UserView.as_view()),
	url(r'^api/v1/users', UsersView.as_view()),
	url(r'^api/v1/', 'api.views.home'),
    url(r'^$', 'api.hello.views.home'),
)
