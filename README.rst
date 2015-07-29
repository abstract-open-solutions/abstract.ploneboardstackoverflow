===========================================================
abstract.ploneboardstackoverflow
==============================================================================

Adds stackoverflow-like features to PloneBoard comments.


Features
--------

This package uses `cioppino.twothumbs` for rating.

Using `archetypes.schemaextender` we add a new field `checked` that is shown on each comment.

Clicking on the checkbox will mark that comment as "checked" (like "right answer"),
uncheck all the others and reindex changed values.

You can use `comment_is_checked` index to search and sort comments.


Translations
------------

Just English.


Installation
------------

Install abstract.ploneboardstackoverflow by adding it to your buildout::

   [buildout]

    ...

    eggs =
        abstract.ploneboardstackoverflow


and then running "bin/buildout"



Contribute
----------

- Issue Tracker: https://github.com/abstract-open-solutions/abstract.ploneboardstackoverflow/issues
- Source Code: https://github.com/abstract-open-solutions/abstract.ploneboardstackoverflow


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com

License
-------

The project is licensed under the GPLv2.
