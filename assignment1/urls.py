import webapp2

from handlers import *

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/post', PostNodeHandler)
], debug=True)

app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500