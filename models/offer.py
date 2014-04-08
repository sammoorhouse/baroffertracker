import cgi
import urllib
import webapp2

from google.appengine.ext import ndb

class Offer(ndb.Model):
	description: ndb.StringProperty()
	expiry: ndb.DateTimeProperty()
	venueKey: ndb.KeyProperty(kind=Venue)
