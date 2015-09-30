

def addConversation(self, title, text=None, creator=None, files=None,
                    conversation_type='PloneboardConversation',
                    **kwargs):
    """Adds a new conversation to the forum.

    XXX should be possible to parameterise the exact type that is being
    added.
    """
    conv = self._old_addConversation(title, text=text,
                                     creator=creator, files=files,
                                     conversation_type=conversation_type,
                                     **kwargs)
    first_comment = conv.getFirstComment()
    if first_comment:
        first_comment.getField('is_main_comment').set(first_comment, True)
        first_comment.reindexObject(idxs=['is_main_comment'])
    return conv


def addReply(self, title, text, creator=None, files=None, in_reply_to=None):
    """Add a reply to this comment."""

    msg = self._old_addReply(title=title, text=text, creator=creator,
                             files=files)
    if in_reply_to:
        msg._in_reply_to = in_reply_to
        msg.reindexObject(idxs=['in_reply_to'])
    return msg


def _buildDict(self, comment):
    """Produce a dict representative of all the important properties
    of a comment.
    """
    res = self._old__buildDict(comment)
    res['is_main_comment'] = comment.is_main_comment
    res['in_reply_to'] = comment._in_reply_to
    return res


def quotedBody(self):
    return ''
