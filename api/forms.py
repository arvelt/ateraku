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
