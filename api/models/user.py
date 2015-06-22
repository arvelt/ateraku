from google.appengine.ext import ndb

class User(ndb.Model):
	name = ndb.StringProperty()
	email = ndb.StringProperty()
	twitter_id = ndb.StringProperty()
	google_id = ndb.StringProperty()
	future_events = ndb.KeyProperty()
	past_events = ndb.KeyProperty()
