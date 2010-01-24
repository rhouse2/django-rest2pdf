#!/usr/bin/env python
# encoding: utf-8
"""
__init__.py

Test for rest2pdf.
"""
import sys
import os
DIRNAME = os.path.dirname(__file__)

from django.test import TestCase
from django.conf import settings
from django.core.management import call_command
from django.db.models.loading import load_app
from django.http import HttpResponse, HttpRequest
from django.db.models.query import QuerySet
from rest2pdf.views import rst_to_pdf
from datetime import datetime

from fakeapp.models import Faq

document_contents_dict = {
    "queryset": QuerySet().none(),
    "template_name": 'example_template.rst',
    "template_object_name" : "articles",
    "style_sheets": ['pdf.style'],
    "extra_context": {
            "document_date": datetime.today(),
            "title": "Document Title",
    }
}

class TestRest2pdf(TestCase):
    fixtures = ['fakeapp.json',] 
    def setUp(self):
        self.old_INSTALLED_APPS = settings.INSTALLED_APPS
        """
        settings.INSTALLED_APPS = (
            # 'django.contrib.auth',
            # 'django.contrib.contenttypes',
            'rest2pdf',
            'rest2pdf.tests.fakeapp',
        )
        load_app('rest2pdf.tests.fakeapp')
        
        call_command('syncdb', verbosity=0, interactive=False) #Create tables for fakeapp
        faq = Faq(question="What is rest2pdf?", 
            answer="A converter of text in a Django databse to pdf \
            using reStructuredText in a template for laying out the \
            document.",
            category="overview",
            tags="rest2pdf")
        faq.save()
        faq = Faq(question="How do you run the tests?",
            answer = 
            "If django-rest2pdf is on your PYTHONPATH, \
            then run this command from the command line: \
            **django-admin.py test --settings='rest2pdf.tests.testsettings'** \
            If you haven't got django-rest2pdf on your PYTHONPATH, \
            then run this command from the tests directory: \
            **python runtests.py**",
            category="testing",
            tags="test, command"
            )
        faq.save()
        """
        document_contents_dict['queryset'] = Faq.objects.all()

    def tearDown(self):
        settings.INSTALLED_APPS = self.old_INSTALLED_APPS

    def test_rst_to_pdf(self):
        """
        Test for the return of a pdf file
        """
        dummy_request = HttpRequest()
        response = rst_to_pdf(dummy_request, **document_contents_dict)
        # Check for a response.
        self.failUnlessEqual(response.status_code, 200)
        # Check the reponse looks like a pdf file.
        self.failUnlessEqual(response._get_content()[:4], '%PDF')
        f = open(os.path.join(DIRNAME,'example.pdf'), 'w')
        f.write(response._get_content())

