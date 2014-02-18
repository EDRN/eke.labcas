# encoding: utf-8
#
# Copyright 2013 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

u'''LabCAS for EKE — setup tests'''

from eke.labcas.testing import EKE_LABCAS_INTEGRATION_TESTING
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
import unittest2 as unittest

class SetupTest(unittest.TestCase):
    layer = EKE_LABCAS_INTEGRATION_TESTING
    def setUp(self):
        super(SetupTest, self).setUp()
        self.portal = self.layer['portal']
    def testTypes(self):
        u'''Check types'''
        pass
