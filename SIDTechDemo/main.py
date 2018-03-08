from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import logging
import webapp2
import os

import datetime
from datetime import date
from decimal import Decimal

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class Sprint(ndb.Model):
    projectName = ndb.StringProperty()
    projectOwner = ndb.StringProperty()
    scrumMaster = ndb.StringProperty()
    team = ndb.StringProperty()
    sprintNum = ndb.IntegerProperty()
    sprintPlanDate = ndb.DateTimeProperty()
    sprintRevDate = ndb.DateTimeProperty()
    sprintRetroDate = ndb.DateTimeProperty()
    scrumMeetDate = ndb.DateTimeProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # get info
        current_user = users.get_current_user()


        if current_user:
            logout_url = users.CreateLogoutURL('/')
            email = current_user.email()
            username = email.split('@')[0]

            current_users = User.query(User.email == email).fetch()

            if not current_users:
                user = User(username=username, email=email)
                user.put()
            else:
                user = User.query(User.username == username).get()

            sprints = Sprint.query(Sprint.user_key == user.key).fetch()
            if sprints:
                template = jinja_environment.get_template('main.html')

                template_vals = {'user':user, #'sprints':sprint,
                'logout_url':logout_url}
                self.response.write(template.render(template_vals))
            else:
                self.redirect('/getProject')
        else:
            login_url = users.CreateLoginURL('/')
            template = jinja_environment.get_template('main.html')
            template_vals = {'login_url':login_url}
            self.response.write(template.render(template_vals))

    def post(self):
        # get info
        current_user = users.get_current_user()
        email = current_user.email()

        user = User.query(User.email == email).get()

        sprint = Sprint.query(Sprint.user_key == user.key).get()
        # sprint.put()
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
