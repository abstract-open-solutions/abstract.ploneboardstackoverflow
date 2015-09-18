

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
