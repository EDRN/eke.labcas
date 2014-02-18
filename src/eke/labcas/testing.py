# encoding: utf-8
# Copyright 2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from plone.app.testing import PloneSandboxLayer, IntegrationTesting, FunctionalTesting, PLONE_FIXTURE
from Products.CMFCore.utils import getToolByName

class EKELabCASLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)
    def setUpZope(self, app, configurationContext):
        import eke.labcas
        self.loadZCML(package=eke.labcas)
    def setUpPloneSite(self, portal):
        wfTool = getToolByName(portal, 'portal_workflow')
        wfTool.setDefaultChain('plone_workflow')
        self.applyProfile(portal, 'eke.labcas:default')
    
EKE_LABCAS = EKELabCASLayer()
EKE_LABCAS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EKE_LABCAS,),
    name='EKELabCASLayer:Integration'
)
EKE_LABCAS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EKE_LABCAS,),
    name='EKELabCASLayer:Functional'
)
