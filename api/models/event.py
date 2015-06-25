from google.appengine.ext import ndb
import pprint

class Event(ndb.Model):
	name = ndb.StringProperty()
	description = ndb.TextProperty()
	place = ndb.StringProperty()
	date = ndb.DateTimeProperty()
	attend = ndb.KeyProperty()
	interest = ndb.KeyProperty()
	absence = ndb.KeyProperty()

	@classmethod
	def get_by_pk(cls, id, **ctx_options):
		return ndb.Key(cls, int(id)).get(**ctx_options)

	@classmethod
	def create(cls, **kwargs):
		name = kwargs.get('name', '')
		description = kwargs.get('description', '')
		place = kwargs.get('place', '')
		date = kwargs.get('date', None)
		attend = kwargs.get('attend', None)
		interest = kwargs.get('interest', None)
		absence = kwargs.get('absence', None)

		event = Event(
			name = name,
			description = description,
			place = place,
			date = date,
			attend = attend,
			interest = interest,
			absence = absence,
		)
		event.put()
		return event

	def delete(self):
		id = self.key.id()
		self.key.delete()
		return id

	def to_dict(self):
		dict = {
			'id': str(self.key.id()),
			'name': self.name,
			'description': self.description,
			'place': self.place,
			'date': str(self.date),
			'attend': str(self.attend),
			'interest': str(self.interest),
			'absence': str(self.absence),
		}
		return dict
