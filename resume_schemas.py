from datetime import datetime

from ming.odm import ThreadLocalODMSession, Mapper, FieldProperty, ForeignIdProperty, RelationProperty
from ming import create_datastore
from ming import collection, Field, Session
from ming import schema

from ming.odm.declarative import MappedClass

bind = create_datastore('odm_tutorial')
doc_session = Session(bind)
sesion = ThreadLocalODMSession(doc_session=doc_session)


class SocialMediaID:
    def __init__(self, network, uname, url):
        self.network    = network
        self.uname      = uname
        self.url        = url
        return None

    def getSocial:
        social = {self.network : {self.uname : self.url}}
        return social

class WorkDetail:
    def __init__(self):
        self.company    = None
        self.startDate  = None
        self.position   = None
        self.url        = None
        self.impact     = None
        self.highlights = []
        self.skills     = []
        return None

    def set_company(self, name):
        self.company = name

    def set_position(self, position):
        self.position = position

    def set_dates(self, start, end):
        self.startDate  = start
        self.endDate    = end
        tenure          = self.endDate - self.startDate

    def set_url(self, url):
        self.url = url

    def set_impact(self, text):
        self.impact = text

    def push_highlight(self, text):
        self.highlights.append(text)

    def push_skill(self, tag):
        self.skills.append(tag)

class Resume(MappedClass):

    class __mongometa__:
        session = session
        name = 'resume'

    _id         = FieldProperty(schema.ObjectId)

    info        = RelationProperty('Personal')
    experience  = RelationProperty('Experience')
    volunteer   = RelationProperty('Volunteer')
    education   = RelationProperty('Education')
    skills      = RelationProperty('Skills')
    awards      = RelationProperty('Awards')
    pubs        = RelationProperty('Publications')
    interests   = RelationProperty('Interests')
    languages   = RelationProperty('Languages')


class Personal(MappedClass):
    class __mongometa__:
        name    = 'personal'
        session = self.session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty(Resume)
    location_id = ForeignIdProperty('Location')
    social_id   = ForeignIdProperty('SocialProfile')

    parent      = RelationProperty(Resume)
    location    = RelationProperty('Location')
    profiles    = RelationProperty('SocialProfile')

    firstName   = FieldProperty(str)
    lastName    = FieldProperty(str)
    middleName  = FieldProperty(str)
    headline    = FieldProperty(str)
    picture     = FieldProperty(str)
    email       = FieldProperty(str)
    phone       = FieldProperty(str)
    url         = FieldProperty(str)
    summary     = FieldProperty(str)



class Location(MappedClass):
    class __mongometa__:
        name    = 'location'
        session = self.session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty(Personal)

    parent      = RelationProperty(Personal)

    address1    = FieldProperty(str)
    address2    = FieldProperty(str)
    zipcode     = FieldProperty(str)
    city        = FieldProperty(str)
    countryUS   = FieldProperty(str)
    region      = FeildProperty(str)

class SocialProfile(MappedClass):
    class __mongometa__:
        name    = 'social_profile'
        session = self.session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty(Personal)

    parent      = RelationProperty(Personal)

    hooks       = FieldProperty(list)


class Experience(MappedClass):
    class __mongometa__:
        name    = 'experience'
        session = self.session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty(Resume)

    parent      = RelationProperty(Resume)

    items       = FieldProperty(list)

class Skills:
    class __mongometa__:
        name    = 'skills'
        session = self.session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty(Resume)

    parent      = RelationProperty(Resume)

    items       = FieldProperty(list)

    def getAllSkills(self):
        return None
