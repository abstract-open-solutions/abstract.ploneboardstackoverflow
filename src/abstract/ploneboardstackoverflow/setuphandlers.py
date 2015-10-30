# -*- coding: utf-8 -*-

import logging
from Products.CMFCore.utils import getToolByName


logger = logging.getLogger('abstract.ploneboardstackoverflow')


def isNotCurrentProfile(context):
    return context.readDataFile('abstractploneboardstackoverflow_marker.txt') is None


def post_install(context):
    """Post install script"""
    if isNotCurrentProfile(context):
        return
    # Do something during the installation of this package


def addKeyToCatalog(portal, new_indexes):
    '''Takes portal_catalog and adds a key to it
    @param portal: context providing portal_catalog
    @indexes: a sequence on infedex data  like (('index_name', 'index_type'), [])
    '''

    catalog = getToolByName(portal, 'portal_catalog')
    indexes = catalog.indexes()
    # Specify the indexes you want, with ('index_name', 'index_type')

    indexables = []

    for name, meta_type in new_indexes:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info("Added %s for field %s.", meta_type, name)
    if len(indexables) > 0:
        logger.info("Indexing new index: %s.", ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)


def migrateTo1010(context):
    # now let's apply the is_main_comment=True to all first comments
    catalog = getToolByName(context, 'portal_catalog')
    logger.info('Marking all first comment as main ones')
    conversations = catalog(portal_type='PloneboardConversation')
    for brain in conversations:
        conversation = brain.getObject()
        for x, comment in enumerate(conversation.getComments(limit=999)):
            if x == 0:
                comment.getField('is_main_comment').set(comment, True)
            else:
                comment.getField('is_main_comment').set(comment, False)
            logger.info("Updated %s to %s value" % (comment.absolute_url_path(),
                                                    x == 0 and 'True' or 'False'))
    logger.info('First comments updated')
    logger.info('Adding new is_main_comment index')
    addKeyToCatalog(context, (('is_main_comment', 'BooleanIndex'),))
    logger.info('New index added')
    logger.info('Migrated to version 0.2')


def migrateTo1020(context):
    logger.info('Migrated to version 0.3')
    setup = getToolByName(context, 'portal_setup')
    logger.info('Change conversation default view')
    setup.runImportStepFromProfile('profile-abstract.ploneboardstackoverflow:default', 'typeinfo')
    catalog = getToolByName(context, 'portal_catalog')
    logger.info('Change conversation view to all contents')
    conversations = catalog(portal_type='PloneboardConversation')
    for brain in conversations:
        obj = brain.getObject()
        obj.setLayout('threaded_conversation_view')
    logger.info('Migrated to version 0.3')

