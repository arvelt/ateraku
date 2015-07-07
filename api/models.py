from google.appengine.ext import ndb
from pprint import pprint

class Event(ndb.Model):
	name = ndb.StringProperty(required=True)
	organizer = ndb.KeyProperty(required=True, kind='User')
	description = ndb.TextProperty()
	place = ndb.StringProperty()
	date = ndb.DateTimeProperty()
	attend = ndb.KeyProperty(kind='User', repeated=True)
	interest = ndb.KeyProperty(kind='User', repeated=True)
	absence = ndb.KeyProperty(kind='User', repeated=True)

	@classmethod
	def get_by_pk(cls, id, **ctx_options):
		return ndb.Key(cls, int(id)).get(**ctx_options)

	@classmethod
	def create(cls, **kwargs):
		name = kwargs.get('name', '')
		organizer = kwargs.get('organizer', None)
		description = kwargs.get('description', '')
		place = kwargs.get('place', '')
		date = kwargs.get('date', None)
		attend = kwargs.get('attend', [])
		interest = kwargs.get('interest', [])
		absence = kwargs.get('absence', [])

		user = User.get_by_pk(organizer)
		if user is None:
			raise ValueError()

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
		organizer = User.get_by_pk(kwargs['organizer'])
		if organizer is None:
			raise ValueError()

		attends = []
		params_attends = kwargs.get('attend', [])
		for user_pk in params_attends:
			user = User.get_by_pk(user_pk)
			attends.append(user.key)

		interests = []
		params_interests = kwargs.get('interest', [])
		for user_pk in params_interests:
			user = User.get_by_pk(user_pk)
			interests.append(user.key)

		absences = []
		params_absences = kwargs.get('absence', [])
		for user_pk in params_absences:
			user = User.get_by_pk(user_pk)
			absences.append(user.key)

		if event:
			event.populate(
				name= kwargs['name'],
				organizer= organizer.key,
				description= kwargs['description'],
				place= kwargs['place'],
				date= kwargs['date'],
				attend= attends,
				interest= interests,
				absence= absences
			)
		event.put()
		return event

	def delete(self):
		id = self.key.id()
		self.key.delete()
		return id

	def to_dict(self):
		attends = []
		for user in self.attend:
			attends.append(user.id())

		interests = []
		for user_pk in self.interest:
			interests.append(user.id())

		absences = []
		for user_pk in self.absence:
			absences.append(user.id())

		dict = {
			'id': int(self.key.id()),
			'name': self.name,
			'organizer': self.organizer.id(),
			'description': self.description,
			'place': self.place,
			'date': self.date,
			'attend': attends,
			'interest': interests,
			'absence': absences,
		}
		return dict


class AuthToken(ndb.Model):
	user_id = ndb.IntegerProperty(required=False)
	token = ndb.StringProperty(required=False)
	secret = ndb.StringProperty(required=False)


class User(ndb.Model):
	name = ndb.StringProperty()
	email = ndb.StringProperty(required=False)
	twitter = ndb.StructuredProperty(AuthToken, required=False)
	future_events = ndb.KeyProperty(kind='Event', repeated=True, required=False)
	past_events = ndb.KeyProperty(kind='Event', repeated=True, required=False)

	@classmethod
	def get_by_pk(cls, id, **ctx_options):
		return ndb.Key(cls, int(id)).get(**ctx_options)

	@classmethod
	def create(cls, **kwargs):
		name = kwargs.get('name', '')
		email = kwargs.get('email', '')
		twitter = kwargs.get('twitter', None)
		if twitter is None:
			twitter = {}

		future_events = []
		params_future_events = kwargs.get('future_events', [])
		for event_pk in params_future_events:
			event = Event.get_by_pk(event_pk)
			future_events.append(event.key)

		past_events = []
		params_past_events = kwargs.get('past_events', [])
		for event_pk in params_past_events:
			event = Event.get_by_pk(event_pk)
			past_events.append(event.key)

		user = User(
			name = name,
			email = email,
			twitter = AuthToken(
				user_id = twitter.get('userId', 0),
				token = twitter.get('token', ''),
				secret = twitter.get('secret', ''),
			),
			future_events = future_events,
			past_events = past_events,
		)
		user.put()
		return user

	@classmethod
	def update(cls, id, kwargs):
		user = cls.get_by_pk(id)
		if user:
			twitter = kwargs.get('twitter', None)
			if twitter is None:
				twitter = {}
			twitter_user_id = twitter.get('user_id', 0)
			twitter_token = twitter.get('token', '')
			twitter_secret = twitter.get('secret', '')

			future_events = []
			params_future_events = kwargs.get('future_events', [])
			for event_pk in params_future_events:
				event = Event.get_by_pk(event_pk)
				future_events.append(event.key)

			past_events = []
			params_past_events = kwargs.get('past_events', [])
			for event_pk in params_past_events:
				event = Event.get_by_pk(event_pk)
				past_events.append(event.key)

			user.populate(
				name= kwargs['name'],
				email= kwargs['email'],
				twitter= AuthToken(
					user_id = twitter_user_id,
					token = twitter_token,
					secret = twitter_secret,
				),
				future_events= future_events,
				past_events= past_events,
			)
		user.put()
		return user

	def delete(self):
		id = self.key.id()
		self.key.delete()
		return id

	def to_dict(self):
		future_events = []
		for user in self.future_events:
			future_events.append(user.id())

		past_events = []
		for user in self.past_events:
			past_events.append(user.id())

		return {
			'id': int(self.key.id()),
			'name': self.name,
			'email': self.email,
			'twitter': {
				'id': int(self.twitter.user_id),
				'token': self.twitter.token,
				'secret': self.twitter.secret,
			},
			'future_events': future_events,
			'past_events': past_events,
		}
