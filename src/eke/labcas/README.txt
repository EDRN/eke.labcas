This package provides representation of LabCAS_ data within the EDRN_ portal.

To demonstrate how it works, we'll do a series of functional tests.  And to do
so, we'll need a test browser::

    >>> app = layer['app']
    >>> from plone.testing.z2 import Browser
    >>> from plone.app.testing import SITE_OWNER_NAME, SITE_OWNER_PASSWORD
    >>> browser = Browser(app)
    >>> browser.handleErrors = False
    >>> browser.addHeader('Authorization', 'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD))
    >>> portal = layer['portal']    
    >>> portalURL = portal.absolute_url()

Here we go.


LabCAS Folders
==============

LabCAS Folders are used to contain LabCAS datasets.  They may be created
anywhere::

    >>> browser.open(portalURL)
    >>> l = browser.getLink(id='eke-labcas-labcasfolder')
    >>> l.url.endswith('++add++eke.labcas.labcasfolder')
    True
    >>> l.click()
    >>> browser.getControl(name='form.widgets.title').value = u'Anal Datasets'
    >>> browser.getControl(name='form.widgets.description').value = u'Where I keep my proctology dataz.'
    >>> browser.getControl(name='form.widgets.rdfDataSource').value = u'testscheme://localhost/labcas/simple'
    >>> browser.getControl(name='form.buttons.save').click()
    >>> 'anal-datasets' in portal.keys()
    True
    >>> folder = portal['anal-datasets']
    >>> folder.title
    u'Anal Datasets'
    >>> folder.description
    u'Where I keep my proctology dataz.'
    >>> folder.rdfDataSource
    u'testscheme://localhost/labcas/simple'

The RDF data source had better be a URL.  Let's see what happens when it's not::

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='form.widgets.rdfDataSource').value = u'I like pie.'
    >>> browser.getControl(name='form.buttons.save').click()
    >>> browser.contents
    '...There were some errors...Constraint not satisfied...'
    >>> browser.getControl(name='form.buttons.cancel').click()



.. References:
.. _LabCAS: http://labcas.jpl.nasa.gov/
.. _EDRN: http://edrn.nci.nih.gov/
