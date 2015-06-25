# coding: utf-8
import json
from django.middleware.csrf import get_token
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from api.models.event import Event

def render_json_response(request, data, status=None):
	'''response を JSON で返却'''
	json_str = json.dumps(data, ensure_ascii=False, indent=2)
	callback = request.GET.get('callback')
	if not callback:
		callback = request.REQUEST.get('callback')  # POSTでJSONPの場合
	if callback:
		json_str = "%s(%s)" % (callback, json_str)
		response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
	else:
		response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
	return response

class EventView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(EventView, self).dispatch(*args, **kwargs)

	def get(self, request, *args, **kwargs):
		csrf_token = get_token(request)
		id = kwargs.get('id')
		event = Event.get_by_pk(id)
		if event is None:
			data = {'event': {}, 'csrf_token': csrf_token}
		else:
			data = {'event': event.to_dict(), 'csrf_token': csrf_token}
		return render_json_response(request, data)

	def put(self, request, *args, **kwargs):
		id = kwargs.get('id')
		data = {}
		return render_json_response(request, data)

	def delete(self, request, *args, **kwargs):
		id = kwargs.get('id')
		event = Event.get_by_pk(id)
		event.delete()
		data = {'event': {}}
		return render_json_response(request, data)

class EventsView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(EventsView, self).dispatch(*args, **kwargs)

	def get(self, request, *args, **kwargs):
		csrf_token = get_token(request)

		dict_events = []
		events = Event.query()
		for event in events:
			dict_events.append(event.to_dict())
		data = {'events': dict_events, 'csrf_token': csrf_token}
		return render_json_response(request, data)

	def post(self, request, *args, **kwargs):
		event = Event.create(**kwargs)
		data = {'event': event.to_dict()}
		return render_json_response(request, data)
