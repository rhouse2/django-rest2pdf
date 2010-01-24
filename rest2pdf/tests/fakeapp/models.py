#!/usr/bin/env python
# encoding: utf-8
"""
models.py for test

"""

# models.py for knowledgebase
from django.db import models

class Faq(models.Model):
    """A simple model for testing"""
    question = models.TextField(blank=False)
    answer = models.TextField(blank=True)
    category = models.CharField(blank=True, max_length=80)
    tags = models.CharField(blank=True, max_length=80)
    date_posted = models.DateField(blank=True, null=True, auto_now_add=True)
    
    class Meta:
        ordering = []

    def __unicode__(self):
        return u"Faq"

    @models.permalink
    def get_absolute_url(self):
        return ('Faq', [self.id])
