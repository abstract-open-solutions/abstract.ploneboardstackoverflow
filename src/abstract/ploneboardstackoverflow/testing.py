# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import abstract.ploneboardstackoverflow


class AbstractPloneboardstackoverflowLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=abstract.ploneboardstackoverflow)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'abstract.ploneboardstackoverflow:default')


ABSTRACT_PLONEBOARDSTACKOVERFLOW_FIXTURE = AbstractPloneboardstackoverflowLayer()


ABSTRACT_PLONEBOARDSTACKOVERFLOW_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ABSTRACT_PLONEBOARDSTACKOVERFLOW_FIXTURE,),
    name='AbstractPloneboardstackoverflowLayer:IntegrationTesting'
)


ABSTRACT_PLONEBOARDSTACKOVERFLOW_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ABSTRACT_PLONEBOARDSTACKOVERFLOW_FIXTURE,),
    name='AbstractPloneboardstackoverflowLayer:FunctionalTesting'
)


ABSTRACT_PLONEBOARDSTACKOVERFLOW_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ABSTRACT_PLONEBOARDSTACKOVERFLOW_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='AbstractPloneboardstackoverflowLayer:AcceptanceTesting'
)
