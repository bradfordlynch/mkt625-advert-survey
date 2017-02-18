#!/usr/bin/env python

# MKT625 - Survey of Ad Tech
# Bradford Lynch, 2017
# Ann Arbor, MI

# [START imports]
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import app_identity

import jinja2
import webapp2
import numpy as np
import pickle

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

# Data Models
class Participant(ndb.Model):
    """Sub model for representing an author."""
    date = ndb.DateTimeProperty(auto_now_add=True)
    ad_cats = ndb.StringProperty(indexed=False)
    products = ndb.StringProperty(indexed=False)
    ad = ndb.StringProperty(indexed=False)
    ad_type = ndb.StringProperty(indexed=False)
    primed = ndb.BooleanProperty(indexed=False)
    browser_size = ndb.StringProperty(indexed=False)
    mouse_x_pos = ndb.TextProperty()
    mouse_y_pos = ndb.TextProperty()
    result = ndb.StringProperty(indexed=False)
    follow_up = ndb.StringProperty(indexed=False)
    profile = ndb.StringProperty(indexed=False)

# Globals
ad_categories = ['Air Travel', 'Food and Drinks', 'TV Shows', 'None of the above']
products = ['Eyewear', 'Headphones', "Women's Fashion", "Men's Fashion", 'Soda', 'None of these products']
ads = {
    'Air Travel':'delta',
    'Food and Drinks':'pepsi',
    'TV Shows':'tbbt'
}

scale = {1:'1 - Not at all', 2:'2', 3:'3 - Somewhat', 4:'4', 5:'5 - Very'}

t_show = 100
t_hide = 2500

# Helper functions
def pickAd(interests):
    if (len(interests) == 0) or (ad_categories[-1] in interests):
        cats = [cat for cat in ad_categories if 'None' not in cat]
        ad_cat = cats[np.random.randint(0,len(cats))]
    else:
        cats = [cat for cat in interests if 'None' not in cat]
        ad_cat = cats[np.random.randint(0,len(cats))]

    ad_type = np.random.rand()
    if ad_type > 0.3333333:
        ad_type = 'new'
    else:
        ad_type = 'old'

    primed = np.random.rand()
    if primed > 0.5:
        primed = True
    else:
        primed = False

    return ad_cat, ad_type, primed


# [START main_page]
class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())

class IntroQues(webapp2.RequestHandler):

    def get(self):
        template_values = {
            'ad_cats':ad_categories,
            'products':products
        }
        template = JINJA_ENVIRONMENT.get_template('intro_questions.html')
        self.response.write(template.render(template_values))

    def post(self):
        sub_ad_cats = {}
        sub_prods = {}
        interests = []

        for cat in ad_categories:
            val = self.request.get(cat)
            if val == 'on':
                sub_ad_cats[cat] = True
                interests.append(cat)
            else:
                sub_ad_cats[cat] = False

        for prod in products:
            val = self.request.get(prod)
            if val == 'on':
                sub_prods[prod] = True
            else:
                sub_prods[prod] = False


        abDecisions = pickAd(interests)
        ad = ads[abDecisions[0]]
        surveyRes = Participant()
        surveyRes.ad_cats = str(sub_ad_cats)
        surveyRes.products = str(sub_prods)
        surveyRes.ad, surveyRes.ad_type, surveyRes.primed = abDecisions
        surveyResKey = surveyRes.put()

        #test = Participant.query(ancestor=foo).fetch()

        template_values = {
            'user':surveyResKey,
            'user_id':surveyResKey.urlsafe(),
            'ad':ad,
            'ad_type':abDecisions[1],
            'sub_ad_timing':'{"show":%d, "hide":%d}' % (t_show, t_hide)
        }

        # Send them to the intro if they should be primed about the tech
        if abDecisions[2]:
            template = JINJA_ENVIRONMENT.get_template('intro_to_tech.html')
        else:
            template = JINJA_ENVIRONMENT.get_template(ad + '.html')

        self.response.write(template.render(template_values))


# [END main_page]

class ShowAd(webapp2.RequestHandler):

    def post(self):
        user_id = self.request.get('user_id')
        ad = self.request.get('ad')
        ad_type = self.request.get('ad_type')

        template_values = {
            'user_id':user_id,
            'ad_type':ad_type,
            'sub_ad_timing':'{"show":%d, "hide":%d}' % (t_show, t_hide)
        }

        template = JINJA_ENVIRONMENT.get_template(ad + '.html')
        self.response.write(template.render(template_values))

class Click(webapp2.RequestHandler):

    def post(self):
        user_id = self.request.get('user_id')
        mouse_x_pos = self.request.get('xs')
        mouse_y_pos = self.request.get('ys')
        click = self.request.get('click')
        browser = self.request.get('browser_size')

        # Get user data object from ndb
        user_key = ndb.Key(urlsafe=user_id)
        user = user_key.get()

        # Save ad survey results
        user.browser_size = browser
        user.mouse_x_pos = mouse_x_pos
        user.mouse_y_pos = mouse_y_pos
        user.result = click
        user.put()

        template_values = {
            'user_id':user_id,
            'scale':scale
        }

        template = JINJA_ENVIRONMENT.get_template('follow_up_questions.html')
        self.response.write(template.render(template_values))

class FollowUpQues(webapp2.RequestHandler):

    def post(self):
        user_id = self.request.get('user_id')
        follow_up_res = self.request.get('responses')

        # Get user data object from ndb
        user_key = ndb.Key(urlsafe=user_id)
        user = user_key.get()

        # Save ad survey results
        user.follow_up = follow_up_res
        user.put()

        template_values = {
            'user_id':user_id,
            'scale':scale
        }

        template = JINJA_ENVIRONMENT.get_template('final_questions.html')
        self.response.write(template.render(template_values))


class FinalQues(webapp2.RequestHandler):

    def post(self):
        user_id = self.request.get('user_id')
        profile_res = self.request.get('responses')

        # Get user data object from ndb
        user_key = ndb.Key(urlsafe=user_id)
        user = user_key.get()

        # Save ad survey results
        user.profile = profile_res
        user.put()

        template_values = {
            'user_id':user_id,
            'code':user_id + '153624'
        }

        template = JINJA_ENVIRONMENT.get_template('complete.html')
        self.response.write(template.render(template_values))

class AdTech(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('intro_to_tech.html')
        self.response.write(template.render())

class DumpData(webapp2.RequestHandler):

    def get(self):
        qry = Participant.query().fetch()
        pickledData = pickle.dumps(qry)
        self.response.write(pickledData)

class Delta(webapp2.RequestHandler):

    def get(self):
        template_values = {
            'user_id':000,
            'ad_type':'new',
            'sub_ad_timing':'{"show":%d, "hide":%d}' % (t_show, t_hide)
        }

        template = JINJA_ENVIRONMENT.get_template('delta.html')
        self.response.write(template.render(template_values))

class Pepsi(webapp2.RequestHandler):

    def get(self):
        template_values = {
            'user_id':000,
            'ad_type':'new',
            'sub_ad_timing':'{"show":%d, "hide":%d}' % (t_show, t_hide)
        }

        template = JINJA_ENVIRONMENT.get_template('pepsi.html')
        self.response.write(template.render(template_values))

class TBBT(webapp2.RequestHandler):

    def get(self):
        template_values = {
            'user_id':000,
            'ad_type':'new',
            'sub_ad_timing':'{"show":%d, "hide":%d}' % (t_show, t_hide)
        }

        template = JINJA_ENVIRONMENT.get_template('tbbt.html')
        self.response.write(template.render(template_values))


# [START app]
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/intro', IntroQues),
    ('/submit', ShowAd),
    ('/intro_to_tech', AdTech),
    ('/click', Click),
    ('/delta', Delta),
    ('/pepsi', Pepsi),
    ('/tbbt', TBBT),
    ('/follow_up', FollowUpQues),
    ('/final', FinalQues),
    ('/dumpData', DumpData),
], debug=True)
# [END app]
