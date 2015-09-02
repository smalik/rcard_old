from datetime import datetime

from ming.odm import ThreadLocalODMSession, Mapper, FieldProperty, ForeignIdProperty, RelationProperty
from ming import create_datastore
from ming import collection, Field, Session
from ming import schema

from ming.odm.declarative import MappedClass

"""
Job description Data model behaves as follows:
    1.  Company Name
    2.  Job Title
    3.  Paid position (Yes or No)
    4.  Pay range (min, max)
    5.  Skills requested
    6.  Job Description
    7.  Quaifications
    8.  Start Date (date, ASAP)
    9.  Location
    10. Work Remotely (Yes or No)
    11. Benefits (as tags)
"""

class JobDescription(MappedClass):
    class __mongometa__:
        session = session
        name = 'job_description'
        unique_indexes = [('_id',),]

    _id         = FieldProperty(schema.ObjectId)

    companyName = FieldProperty(str)
    title       = FieldProperty(str)
    isPaid      = FieldProperty(schema.Bool)
    minPay      = FieldProperty(schema.Float)
    maxPay      = FieldProperty(schema.Float)
    skills      = FieldProperty(schema.Float(str))
    description = FieldProperty(str)
    quals       = FieldProperty(str)
    startDt     = FieldProperty(schema.DateTime)
    isRemote    = FieldProperty(schema.Bool)
    benefits    = FieldProperty(schema.Float(str))
    skills      = FieldProperty(schema.Float(str))

Mapper.compile_all()
