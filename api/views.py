# coding: utf-8
import json
from django.middleware.csrf import get_token
from django.http import HttpResponse
from api.models.event import Event

def home(request):
    return HttpResponse('Hello World2!')

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

def events_list(request):
	'''全てのイベントを帰す'''
	events = []
	for event in Event.query():
		event_dict = [
			('id', event.id),
			('name', event.name),
			('description', event.description),
			]
		events.append(event_dict)

	data = {'events': events}
	return render_json_response(request, data)
