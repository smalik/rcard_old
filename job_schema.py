from datetime import datetime

from ming.odm import ThreadLocalODMSession, Mapper, FieldProperty, ForeignIdProperty, RelationProperty
from ming import create_datastore
from ming import collection, Field, Session
from ming import schema

from ming.odm.declarative import MappedClass

bind = create_datastore('odm_tutorial')
doc_session = Session(bind)
sesion = ThreadLocalODMSession(doc_session=doc_session)
