# -*- coding: utf-8 -*-

from DateTime import DateTime
from plone.app.contenttypes.browser.collection import CollectionView
from Products.Five import BrowserView
from zope.component import getMultiAdapter
from plone import api
from Products.CMFCore.utils import getToolByName

class PubblicazioneView(BrowserView):
    """
    Vista del contenuto Pubblicazione
    """

    def __init__(self, context, request):
        super(PubblicazioneView, self).__init__(context, request)
        self.plone_view = getMultiAdapter(
              (context, request), name=u'plone')

    def toLocalizedTime(self, publication_date):
        time = DateTime(publication_date.strftime('%Y-%m-%d'))
        return self.plone_view.toLocalizedTime(time, False, False)


    def get_mime_type(self, context):
        portal = api.portal.get()
        mimereg = getToolByName(portal,'mimetypes_registry')
        return mimereg.lookupExtension(context.publicationFile.filename).extensions[0].upper()

    def get_file_size(self, context):
        return format(context.publicationFile.getSize()/float(1024*1024), '.2f')


class PubblicazioniCollectionView(CollectionView):
    """
    Vista del contenuto Pubblicazione
    """

    def __init__(self, context, request):
        super(PubblicazioniCollectionView, self).__init__(context, request)
        self.plone_view = getMultiAdapter(
              (context, request), name=u'plone')

    def toLocalizedTime(self, publication_date):
        time = DateTime(publication_date.strftime('%Y-%m-%d'))
        return self.plone_view.toLocalizedTime(time, False, False)
