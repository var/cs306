from google.appengine.ext import ndb

class Node(ndb.Model):
	stub = ndb.TextProperty()
	postedOn = ndb.DateTimeProperty(auto_now_add=True)
	remoteaddrs = ndb.StringProperty()