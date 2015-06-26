from google.appengine.ext import ndb
import pprint

class Event(ndb.Model):
	name = ndb.StringProperty()
	organizer = ndb.StringProperty()
	description = ndb.TextProperty()
	place = ndb.StringProperty()
	date = ndb.DateTimeProperty()
	attend = ndb.StringProperty()
	interest = ndb.StringProperty()
	absence = ndb.StringProperty()

	@classmethod
	def get_by_pk(cls, id, **ctx_options):
		return ndb.Key(cls, int(id)).get(**ctx_options)

	@classmethod
	def create(cls, **kwargs):
		name = kwargs.get('name', '')
		organizer = kwargs.get('organizer', '')
		description = kwargs.get('description', '')
		place = kwargs.get('place', '')
		date = kwargs.get('date', None)
		attend = kwargs.get('attend', None)
		interest = kwargs.get('interest', None)
		absence = kwargs.get('absence', None)

		event = Event(
			name = name,
			organizer = organizer,
			description = description,
			place = place,
			date = date,
			attend = attend,
			interest = interest,
			absence = absence,
		)
		event.put()
		return event

	@classmethod
	def update(cls, id, kwargs):
		event = cls.get_by_pk(id)
		if event:
			event.populate(
				name= kwargs['name'],
				organizer= kwargs['organizer'],
				description= kwargs['description'],
				place= kwargs['place'],
				date= kwargs['date'],
				attend= kwargs['attend'],
				interest= kwargs['interest'],
				absence= kwargs['absence']
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
			'organizer': self.organizer,
			'description': self.description,
			'place': self.place,
			'date': str(self.date),
			'attend': str(self.attend),
			'interest': str(self.interest),
			'absence': str(self.absence),
		}
		return dict

class User(ndb.Model):
	name = ndb.StringProperty()
	email = ndb.StringProperty()
	twitter_id = ndb.StringProperty()
	google_id = ndb.StringProperty()
	future_events = ndb.KeyProperty()
	past_events = ndb.KeyProperty()
