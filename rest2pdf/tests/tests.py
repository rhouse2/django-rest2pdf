"""
Test for rest2pdf.
"""

from django.test import TestCase
from django.http import HttpResponse, HttpRequest
from django.db.models.query import QuerySet
from rest2pdf.views import rst_to_pdf
from datetime import datetime

document_contents_dict = {
    "queryset": QuerySet().none(),
    "template_name": 'template.rst',
    "template_object_name" : "object",
    "style_sheets": ['pdf.style'],
    "extra_context": {
            "document_date": datetime.today(),
            "title": "Document Title",
    }
}

class TestRest2pdf(TestCase):
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

