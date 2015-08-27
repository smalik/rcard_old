from ming import Session
from ming import create_datastore
from ming.odm import ThreadLocalODMSession

from ming import schema
from ming.odm import FieldProperty, ForeignIdProperty, RelationProperty
from ming.odm import Mapper
from ming.odm.declarative import MappedClass


bind = create_datastore('odm_tutorial')
doc_session = Session(bind)
session = ThreadLocalODMSession(doc_session=doc_session)

class WikiPage(MappedClass):

    class __mongometa__:
        session = session
        name = 'wiki_page'

    _id = FieldProperty(schema.ObjectId)
    title = FieldProperty(str)
    text = FieldProperty(str)

    comments=RelationProperty('WikiComment')

class WikiComment(MappedClass):

    class __mongometa__:
        session = session
        name = 'wiki_comment'

    _id = FieldProperty(schema.ObjectId)
    page_id = ForeignIdProperty('WikiPage')
    text=FieldProperty(str, if_missing='')

    page=RelationProperty('WikiPage')

Mapper.compile_all()
