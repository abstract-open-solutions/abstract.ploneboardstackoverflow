# -*- coding: utf-8 -*-

from plone import api
from Products.Five import BrowserView
from plone.batching import Batch

MAX_TEXT_SIZE = 600

class AllQuestionsView(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request
        request.set('disable_border', True)

    def results(self):
        bsize = self.request.get('bsize') or 20
        b_start = self.request.get('b_start') or 0
        catalog = api.portal.get_tool('portal_catalog')
        results = catalog(portal_type='PloneboardComment',
                          is_main_comment=True,
                          sort_on='created', sort_order='reverse')
        return Batch(results, bsize, start=b_start, end=b_start + bsize)

    def total_comments(self, question):
        # conversation = question.getObject().aq_parent
        # return conversation.getNumberOfComments()
        catalog = api.portal.get_tool('portal_catalog')
        comments = catalog(
            portal_type="PloneboardComment",
            path='/'.join(question.getPath().split('/')[:-1]),
            is_main_comment=False,
            in_reply_to=None
        )
        return len(comments)

    def username(self, userid):
        user = api.user.get(username=userid)
        fullname = user.getProperty('fullname') if user else None
        return fullname or userid

    def limit_text(self, text):
        if len(text) < MAX_TEXT_SIZE:
            return text
        return text[:MAX_TEXT_SIZE - 1] + "…"
