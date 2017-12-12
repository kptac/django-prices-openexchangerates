#! /usr/bin/env python
import os
from setuptools import setup

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules']

setup(
    name='django-prices-openexchangerates',
    author='Mirumee Software',
    author_email='hello@mirumee.com',
    description='openexchangerates.org support for django-prices',
    license='BSD',
    version='1.0.0-beta',
    url='https://github.com/mirumee/django-prices-openexchangerates',
    packages=[
        'django_prices_openexchangerates',
        'django_prices_openexchangerates.management',
        'django_prices_openexchangerates.management.commands',
        'django_prices_openexchangerates.migrations',
        'django_prices_openexchangerates.templatetags'],
    include_package_data=True,
    classifiers=CLASSIFIERS,
    install_requires=['Django>=1.4', 'django-prices>=0.6.1', 'prices>=1.0.0-beta'],
    platforms=['any'],
    zip_safe=False)
