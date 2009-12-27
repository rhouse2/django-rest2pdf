#!/usr/bin/env python
# encoding: utf-8
"""
setup.py

Created by Richard on 2009-12-27.
"""

from distutils.core import setup
import os

from rest2pdf import get_version


# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('rest2pdf'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[9:] # Strip "rest2pdf/" or "rest2pdf\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(name='django-rest2pdf',
      version=get_version().replace(' ', '-'),
      description='A pdf document creator for Django content.',
      author='Richard House',
      author_email='RHouse2@gmail.com',
      url='http://code.google.com/p/django-rest2pdf/',
      download_url='http://code.google.com/p/django-rest2pdf/downloads/list',
      package_dir={'rest2pdf': 'rest2pdf'},
      packages=packages,
      package_data={'rest2pdf': data_files},
      classifiers=['Development Status :: 1 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
      )

