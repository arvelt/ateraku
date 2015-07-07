from django import forms
from django.core.exceptions import ValidationError

class MultiIntegerField(forms.IntegerField):
	# Need a widget for this type of multi-field
	# (e.g. A widget of variable number of input fields)
	hidden_widget = forms.widgets.MultipleHiddenInput
	widget = forms.widgets.SelectMultiple

	def to_python(self, value):
		res = []
		if isinstance(value, (list, tuple)):
			for val in value:
				val2 = super(MultiIntegerField, self).to_python(val)
				res.append(val2)
		return res


class StructuredField(forms.Field):
	def __init__(self, form_class, *args, **kwargs):
		self.form_class = form_class
		super(StructuredField, self).__init__(*args, **kwargs)

	def to_python(self, value):
		if value in ('', None):
			return None
		elif not isinstance(value, dict):
			raise ValidationError()

		form = self.form_class(value)
		if form.is_valid():
			return form.cleaned_data
		else:
			raise ValidationError()


class EventForm(forms.Form):
	name = forms.CharField()
	organizer = forms.IntegerField()
	description = forms.CharField(required=False)
	place = forms.CharField(required=False)
	date = forms.DateTimeField(required=False)
	attend = MultiIntegerField(required=False)
	interest = MultiIntegerField(required=False)
	absence = MultiIntegerField(required=False)


class AuthForm(forms.Form):
	user_id = forms.IntegerField(required=False)
	token = forms.CharField(required=False)
	secret = forms.CharField(required=False)


class UserForm(forms.Form):
	name = forms.CharField()
	email = forms.CharField(required=False)
	twitter = StructuredField(AuthForm, required=False)
	future_events = MultiIntegerField(required=False)
	past_events = MultiIntegerField(required=False)
