# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from abstract.ploneboardstackoverflow.testing import ABSTRACT_PLONEBOARDSTACKOVERFLOW_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that abstract.ploneboardstackoverflow is properly installed."""

    layer = ABSTRACT_PLONEBOARDSTACKOVERFLOW_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if abstract.ploneboardstackoverflow is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('abstract.ploneboardstackoverflow'))

    def test_uninstall(self):
        """Test if abstract.ploneboardstackoverflow is cleanly uninstalled."""
        self.installer.uninstallProducts(['abstract.ploneboardstackoverflow'])
        self.assertFalse(self.installer.isProductInstalled('abstract.ploneboardstackoverflow'))

    def test_browserlayer(self):
        """Test that ILayer is registered."""
        from abstract.ploneboardstackoverflow.interfaces import ILayer
        from plone.browserlayer import utils
        self.assertIn(ILayer, utils.registered_layers())
