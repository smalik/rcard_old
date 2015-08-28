from ming import Session
from ming import create_datastore
from ming.odm import ThreadLocalODMSession

from ming import schema
from ming.odm import FieldProperty, ForeignIdProperty, RelationProperty
from ming.odm import Mapper
from ming.odm.declarative import MappedClass


class CoreComment(MappedClass):

    author      = FieldProperty(schema.ObjectId)
    createDt    = FieldProperty(schema.DateTime)
    topic       = FieldProperty(str)
    likes       = FieldProperty(schema.Int)
    payload     = FieldProperty(str)


class Commenting(CoreComment):
    class __mongometa__:
        session = session
        name = 'commenting'
        unique_indexes = [('_id',),]

    _id         = FieldProperty(schema.ObjectId)
    parent_id   = ForeignIdProperty(Resume)

    parent      = RelationProperty(Resume)
    children    = FieldProperty(schema.Array(list))
    siblings    = FieldProperty(schema.Array(list))
