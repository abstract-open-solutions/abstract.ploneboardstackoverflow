# -*- coding: utf-8 -*-

from plone.indexer import indexer
from zope.interface import Interface
from Products.Ploneboard.interfaces import IComment

from .extenders import get_checked


@indexer(IComment)
def comment_is_checked(obj):
    return get_checked(obj)


@indexer(Interface)
def comment_is_checked_others(obj):
    """ avoid indexing for any other content
    """
    raise AttributeError()
