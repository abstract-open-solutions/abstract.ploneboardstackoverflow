# -*- coding: utf-8 -*-


from Products.Five import BrowserView

from ..extenders import get_checked
from ..extenders import set_checked


class CheckedSnippetView(BrowserView):

    def is_checked(self):
        return get_checked(self.context)


class CheckedAjax(BrowserView):

    def __call__(self):
        self.update_checked()

    def update_checked(self):
        """ update checked status on comments
        """
        checked_uid = self.request.form.get('comment_uid')
        if not checked_uid:
            return self._answer()
        checked_on = self.request.form['is_checked'] == 'true'
        conversation = self.context
        for comment in conversation.objectValues():
            is_checked = get_checked(comment)
            # our trigger comment
            if comment.UID() == checked_uid:
                # set checked
                if checked_on and not is_checked:
                    set_checked(comment, True)
                    self._reindex(comment)
                    # print 'updated True', comment.absolute_url_path()
                elif not checked_on and is_checked:
                    set_checked(comment, False)
                    self._reindex(comment)
                    # print 'updated False', comment.absolute_url_path()
                # done here, go on
                continue
            # set all the others as not check
            # and reindex them only if the value changed
            if checked_on and is_checked:
                set_checked(comment, False)
                self._reindex(comment)
                # print 'updated False', comment.absolute_url_path()
        return self._answer()

    def _reindex(self, comment):
        comment.reindexObject(idxs=['comment_is_checked'])

    def _answer(self):
        self.request.response.setStatus(204)
        return ' '
