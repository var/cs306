import webapp2
import datetime
import logging
from webapp2_extras import jinja2
from dataaccess import *

class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **context):
        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)


class HomeHandler(BaseHandler):
	""" Just handles the home page """
	def get(self):
		self.render_response('home.html', nodes = getNodes())

class PostNodeHandler(BaseHandler):
	def post(self):
		stub = self.request.get('stub')
		raddr = self.request.remote_addr

		setNode(stub, raddr)

		self.redirect('/', True)
		

def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Oops! I could swear this page was here!')
    response.set_status(404)

def handle_500(request, response, exception):
    logging.exception(exception)
    response.write('Hey - looks like there is a problem. Can you please start over?')
    response.set_status(500)