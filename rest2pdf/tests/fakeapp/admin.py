#!/usr/bin/env python
# encoding: utf-8

from django.contrib import admin
from models import Faq

class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', )

admin.site.register(Faq, FaqAdmin)
