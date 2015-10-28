# -*- coding: utf-8 -*-

from plone.indexer import indexer
from zope.interface import Interface
from Products.Ploneboard.interfaces import IComment
from cioppino.twothumbs import rate

from .extenders import get_checked


@indexer(IComment)
def comment_is_checked(obj):
    return get_checked(obj)


@indexer(IComment)
def in_reply_to(obj):
    return obj._in_reply_to


@indexer(Interface)
def comment_is_checked_others(obj):
    """ avoid indexing for any other content
    """
    raise AttributeError()


@indexer(IComment)
def positive_ratings(obj, **kw):
    return rate.getTotalPositiveRatings(obj)
