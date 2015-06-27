from django import forms

class EventForm(forms.Form):
	name = forms.CharField()
	organizer = forms.CharField()
	description = forms.CharField(required=False)
	place = forms.CharField(required=False)
	date = forms.DateTimeField(required=False)
	attend = forms.CharField(required=False)
	interest = forms.CharField(required=False)
	absence = forms.CharField(required=False)

class UserForm(forms.Form):
	name = forms.CharField()
	email = forms.CharField()
	twitter_id = forms.CharField(required=False)
	google_id = forms.CharField(required=False)
	future_events = forms.CharField(required=False)
	past_events = forms.CharField(required=False)
