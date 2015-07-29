# -*- coding: utf-8 -*-

from zope.component import adapts
from zope.interface import implements

from Products.Archetypes import atapi

from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender

from Products.Ploneboard.interfaces import IComment

from .interfaces import ILayer
from . import _

CHECKED_FIELDNAME = "checked"


def get_checked(obj):
    field = obj.getField(CHECKED_FIELDNAME)
    return field and field.get(obj)


def set_checked(obj, value):
    field = obj.getField(CHECKED_FIELDNAME)
    return field and field.set(obj, value)


class _ExtensionBooleanField(ExtensionField, atapi.BooleanField):
    pass


class CommentExtender(object):
    adapts(IComment)
    implements(IOrderableSchemaExtender,
               IBrowserLayerAwareExtender,
               ISchemaModifier)

    layer = ILayer

    fields = [
        _ExtensionBooleanField(
            CHECKED_FIELDNAME,
            widget=atapi.BooleanWidget(
                label=_(u"Is checked?"),
                description=_(u"Marked as correct answer."),
                visible={'view': 'invisible', 'edit': 'invisible'},
            ),
        ),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self): # noqa
        return self.fields

    def getOrder(self, original): # noqa
        """
        'original' is a dictionary where the keys are the names of
        schemata and the values are lists of field names, in order.
        """
        return original

    # def fiddle(object, schema):
    #     return schema
