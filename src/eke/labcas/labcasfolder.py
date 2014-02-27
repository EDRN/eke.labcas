# encoding: utf-8
# Copyright 2014 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from eke.labcas import MESSAGE_FACTORY as _
from plone.supermodel import model
from zope import schema
import re

_protocols = (u'http', u'ftp', u'irc', u'news', u'imap', u'gopher', u'jabber', u'webdav', u'smb', u'fish',
    u'ldap', u'pop3', u'smtp', u'sftp', u'ssh', u'feed', u'testscheme'
)
_urlRE = re.compile(ur'({})s?://[^\s\r\n]+'.format(u'|'.join(_protocols)))

def isURL(value):
    u'''Ensure the given ``value`` looks like a URL.'''
    return True if _urlRE.match(value) else False
    
class ILabCASFolder(model.Schema):
    u'''A folder containing LabCAS datasets.'''
    title = schema.TextLine(
        title=_(u'Title'),
        description=_(u'The name of this folder'),
        required=True,
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A short summary of this folder.'),
        required=False,
    )
    rdfDataSource = schema.TextLine(
        title=_(u'RDF Data Source'),
        description=_(u'URL to a source of Resource Description Format data defines the contents of this folder.'),
        required=False,
        constraint=isURL,
    )
