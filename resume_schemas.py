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

    def getSocial():
        social = {self.network : {self.uname : self.url}}
        return social

class VolunteerDetail:
    def __init__(self):
        self.org        = None
        self.title      = None
        self.startDt    = None
        self.endDt      = None
        self.url        = None
        self.impact     = None
        self.highlights = []

    def push_highlight(self, text):
        self.highlights.append(text)

class WorkDetail:
    def __init__(self):
        self.company    = None
        self.startDt    = None
        self.endDt      = None
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

class EduDetail:
    def __init__(self):
        self.school = None
        self.degree = None
        self.major  = None
        self.startDt= None
        self.gradDt = None
        self.gpa    = None
        self.courses= []

    def push_course(self, course):
        self.courses.append(course)

class AwardItems:
    def __init__(self):
        self.title  = None
        self.date   = None
        self.issuer = None
        self.desc   = None
        self.url    = None
        return None

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

class Volunteer(MappedClass):
    class __mongometa__:
        name    = 'volunteer'
        session = self.session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty(Resume)

    parent      = RelationProperty(Resume)

    items       = FieldProperty(list)

class Education(MappedClass):
    class __mongometa__:
        name    = 'education'
        session = self.session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty(Resume)

    parent      = RelationProperty(Resume)

    items       = FieldProperty(list)

class Awards(MappedClass):
    class __mongometa__:
        name    = 'awards'
        session = self.session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty(Resume)

    items       = FieldProperty(list)

class Publications(MappedClass):
    class __mongometa__:
        name    = 'publications'
        session = self.session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty(Resume)

    items       = FieldProperty(list)

class Interests(MappedClass):
    class __mongometa__:
        name    = 'interests'
        session = self.session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty(Resume)

    items       = FieldProperty(list)

class Languages(MappedClass):
    class __mongometa__:
        name    = 'languages'
        session = self.session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty(Resume)

    items       = FieldProperty(list)

class Skills(MappedClass):
    class __mongometa__:
        name    = 'skills'
        session = self.session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty(Resume)
    exp_id      = ForeignIdProperty(Experience)

    parent      = RelationProperty(Resume)
    exp         = ForeignIdProperty(Experience)

    items       = FieldProperty(list)

    def getAllSkills(self, exp_id, exp):
        return None
