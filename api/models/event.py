from google.appengine.ext import ndb

class Event(ndb.Model):
	name = ndb.StringProperty()
	description = ndb.TextProperty()
	place = ndb.StringProperty()
	date = ndb.DateTimeProperty()
	attend = ndb.KeyProperty()
	interest = ndb.KeyProperty()
	absence = ndb.KeyProperty()
