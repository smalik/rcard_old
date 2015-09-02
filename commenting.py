from ming import Session
from ming import create_datastore
from ming.odm import ThreadLocalODMSession

from ming import schema
from ming.odm import FieldProperty, ForeignIdProperty, RelationProperty
from ming.odm import Mapper
from ming.odm.declarative import MappedClass

"""
Comments behave as follows:
     1. Click on a comment button on the card.
     2. A comment card pops up with:
         i.      commenter pic
         ii.     commenter username
         iii.    comment text area
         iv.     like button
         v.      downvote button
         vi.     submit button (optional)
     3. User adds their comment text (limited to 240 chars)
     4. Threaded to one level
"""

"""
Base comment class that other commenting classes inherit.  We want to capture the comment author, likes, downvotes, comment text, comment date, and what topic the comment is about
"""
class CoreComment(MappedClass):

    # user ID from Person class of contributor
    author      = FieldProperty(schema.ObjectId)
    createDt    = FieldProperty(schema.DateTime)

    # Topic of comment (e.g.  grammar, clarity, etc...)
    topic       = FieldProperty(str)

    # Section this comment is bound to
    section     = FieldProperty(str)
    section_id  = FieldProperty(schema.ObjectId)

    # how many people upvoted/downvoted the comment posted in payload
    upvote       = FieldProperty(schema.Int)
    downvote     = FieldProperty(schema.Int)

    # actual comment
    payload     = FieldProperty(str)


"""
Comment container for each comment and pointers of comments it is associated with
"""
class Commenting(CoreComment):
    class __mongometa__:
        session = session
        name = 'commenting'
        unique_indexes = [('_id',),]

    def __init__(self, user):
        author  = user

    _id         = FieldProperty(schema.ObjectId)

    parent_id   = ForeignIdProperty(Person)
    parent      = RelationProperty(Person)

    children    = FieldProperty(schema.Array(schema.ObjectId))
    siblings    = FieldProperty(schema.Array(schema.ObjectId))

    def comment_count(self):
        return len(self.siblings)

    def thread_count(self):
        return len(self.children)

Mapper.compile_all()
