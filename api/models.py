from google.appengine.ext import ndb
from pprint import pprint

class Event(ndb.Model):
	name = ndb.StringProperty(required=True)
	organizer = ndb.KeyProperty(required=True, kind='User')
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

		user = User.get_by_pk(organizer)

		pprint(user)

		event = Event(
			name = name,
			organizer = user.key,
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
			'organizer': self.organizer.id(),
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

	@classmethod
	def get_by_pk(cls, id, **ctx_options):
		return ndb.Key(cls, int(id)).get(**ctx_options)

	@classmethod
	def create(cls, **kwargs):
		name = kwargs.get('name', '')
		email = kwargs.get('organizer', '')
		twitter_id = kwargs.get('description', '')
		google_id = kwargs.get('place', '')
		future_events = kwargs.get('date', None)
		past_events = kwargs.get('attend', None)

		user = User(
			name = name,
			email = email,
			twitter_id = twitter_id,
			google_id = google_id,
			future_events = future_events,
			past_events = past_events,
		)
		user.put()
		return user

	@classmethod
	def update(cls, id, kwargs):
		user = cls.get_by_pk(id)
		if user:
			user.populate(
				name= kwargs['name'],
				email= kwargs['email'],
				twitter_id= kwargs['twitter_id'],
				google_id= kwargs['google_id'],
				future_events= kwargs['future_events'],
				past_events= kwargs['past_events'],
			)
		user.put()
		return user

	def delete(self):
		id = self.key.id()
		self.key.delete()
		return id

	def to_dict(self):
		return {
			'id': str(self.key.id()),
			'name': self.name,
			'email': self.email,
			'twitter_id': self.twitter_id,
			'google_id': self.google_id,
			'future_users': str(self.future_events),
			'past_events': str(self.past_events),
		}
