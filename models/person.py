import cgi
import urllib
import webapp2

from google.appengine.ext import ndb

class Person(ndb.Model):
	givenName = ndb.StringProperty()
	familyName = ndb.StringProperty()
	acceptedOffers = ndb.KeyProperty(kind=Offer, repeated=True)
	
	@classmethod
	def query_users(cls, ancestor_key):
		return cls.query(ancestor=ancestor_key).order(-cls.familyName)

