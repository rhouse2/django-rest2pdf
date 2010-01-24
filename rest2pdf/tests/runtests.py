#!/usr/bin/env python
# encoding: utf-8
"""
runtests.py

Created by Richard on 2010-01-24.
Avoids the need for installing the app on your python path
"""

from django.core.management import setup_environ, call_command
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. \n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    print 'Executing django-admin.py test ...'
    # setup_environ() adds the path of this file to sys.path
    setup_environ(settings)
    call_command('test')
