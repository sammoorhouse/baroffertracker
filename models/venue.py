import cgi
import urllib
import webapp2

from google.appengine.ext import ndb

class Venue(ndb.Model):
	name = ndb.StringProperty()
	address = ndb.StringProperty()
	location = ndb.GeoPtProperty()
	staff = ndb.KeyProperty(kind=Person, repeated=True)
