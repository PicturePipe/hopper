#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from codecs import open

from setuptools import find_packages, setup


def read(*paths):
    """Build a file path from *paths and return the contents."""
    with open(os.path.join(*paths), 'r', 'utf-8') as f:
        return f.read()

requires = [
    'Django<1.9',
    'dj-database-url>=0.3.0',
    'django-braces>=1.4.0',
    'django-crispy-forms>=1.4.0',
    'django-grappelli>=2.6.3',
    'djangorestframework==3.1.1',
    'envdir>=0.7',
    'psycopg2>=2.5.4',
    'pytz>=2014.10',
]

docs_requires = [
    'Sphinx==1.2.2',
]

tests_requires = [
    'coverage==3.7.1',
    'factory_boy==2.4.1',
    'freezegun==0.2.8',
    'isort==3.9.5',
    'pytest-django==2.7.0',
    'pytest-httpretty==0.2.0',
    'pytest-pythonpath==0.6',
    'pytest==2.6.4',
    'tox==1.9.2',
]

setup(
    name='hopper',
    version='0.1.0',
    description='A RESTful HTTP API for managing HTML forms.',
    long_description=read('README.rst'),
    author='transcode',
    author_email='team@transcode.de',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    extras_require={
        'docs': docs_requires,
        'tests': tests_requires,
    },
    license='BSD',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
