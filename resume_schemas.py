from datetime import datetime

from ming.odm import ThreadLocalODMSession, Mapper, FieldProperty, ForeignIdProperty, RelationProperty
from ming import create_datastore
from ming import collection, Field, Session
from ming import schema

from ming.odm.declarative import MappedClass

bind = create_datastore('odm_tutorial')
doc_session = Session(bind)
session = ThreadLocalODMSession(doc_session=doc_session)


class SocialMediaID:
    def __init__(self, network=None, uname=None, url=None):
        self.network    = network
        self.uname      = uname
        self.url        = url
        return None

    def getSocial(self):
        # social = {self.network : {self.uname : self.url}}
        social = [self.network, self.uname, self.url]
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

class Personal(MappedClass):
    class __mongometa__:
        name    = 'personal'
        session = session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty('Resume')
    location_id = ForeignIdProperty('Location')
    social_id   = ForeignIdProperty('SocialProfile')

    parent      = RelationProperty('Resume')
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
        session = session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty(Personal)

    parent      = RelationProperty(Personal)

    address1    = FieldProperty(str)
    address2    = FieldProperty(str)
    zipcode     = FieldProperty(str)
    city        = FieldProperty(str)
    country   = FieldProperty(str)
    region      = FieldProperty(str)

class SocialProfile(MappedClass):
    class __mongometa__:
        name    = 'social_profile'
        session = session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty(Personal)

    parent      = RelationProperty(Personal)

    hooks       = FieldProperty(schema.Array(list))


class Experience(MappedClass):
    class __mongometa__:
        name    = 'experience'
        session = session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty('Resume')

    parent      = RelationProperty('Resume')

    items       = FieldProperty(schema.Array(str))

class Volunteer(MappedClass):
    class __mongometa__:
        name    = 'volunteer'
        session = session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty('Resume')

    parent      = RelationProperty('Resume')

    items       = FieldProperty(schema.Array(str))

class Education(MappedClass):
    class __mongometa__:
        name    = 'education'
        session = session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty('Resume')
    parent      = RelationProperty('Resume')

    items       = FieldProperty(schema.Array(str))

class Awards(MappedClass):
    class __mongometa__:
        name    = 'awards'
        session = session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty('Resume')
    parent      = RelationProperty('Resume')

    items       = FieldProperty(schema.Array(str))

class Publications(MappedClass):
    class __mongometa__:
        name    = 'publications'
        session = session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty('Resume')
    parent      = RelationProperty('Resume')

    items       = FieldProperty(schema.Array(str))

class Interests(MappedClass):
    class __mongometa__:
        name    = 'interests'
        session = session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty('Resume')
    parent      = RelationProperty('Resume')

    items       = FieldProperty(schema.Array(str))

class Languages(MappedClass):
    class __mongometa__:
        name    = 'languages'
        session = session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty('Resume')
    parent      = RelationProperty('Resume')

    items       = FieldProperty(schema.Array(str))

class Skills(MappedClass):
    class __mongometa__:
        name    = 'skills'
        session = session

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty('Resume')
    exp_id      = ForeignIdProperty(Experience)

    parent      = RelationProperty('Resume')
    exp         = ForeignIdProperty(Experience)

    items       = FieldProperty(schema.Array(str))

    def getAllSkills(self, exp_id, exp):
        return None

class Resume(MappedClass):

    class __mongometa__:
        session = session
        name = 'resume'
        unique_indexes = [('_id',),]

    _id         = FieldProperty(schema.ObjectId)


    info_id     = ForeignIdProperty(Personal)
    info        = RelationProperty(Personal)

    experience_id= ForeignIdProperty(Experience)
    experience  = RelationProperty(Experience)

    volunteer_id= ForeignIdProperty(Volunteer)
    volunteer   = RelationProperty(Volunteer)

    education_id= ForeignIdProperty(Education)
    education   = RelationProperty(Education)

    skills_id   = ForeignIdProperty(Skills)
    skills      = RelationProperty(Skills)

    awards_id   = ForeignIdProperty(Awards)
    awards      = RelationProperty(Awards)

    pubs_id     = ForeignIdProperty(Publications)
    pubs        = RelationProperty(Publications)

    interests_id= ForeignIdProperty(Interests)
    interests   = RelationProperty(Interests)

    languages_id= ForeignIdProperty(Languages)
    languages   = RelationProperty(Languages)

    version     = FieldProperty(schema.Int)
    numEdits    = FieldProperty(schema.Int)
    editDt      = FieldProperty(schema.Array(schema.DateTime))

Mapper.compile_all()
