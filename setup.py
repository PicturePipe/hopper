#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from codecs import open

from setuptools import find_packages, setup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read(*paths):
    """Build a file path from *paths and return the contents."""
    with open(os.path.join(*paths), 'r', 'utf-8') as f:
        return f.read()

requires = [
    'Django<1.9',
    'dj-database-url>=0.3.0',
    'django-braces>=1.4.0',
    'django-configurations==1.0',
    'django-cors-headers>=1.1.0',
    'django-countries==3.4.1',
    'django-crispy-forms>=1.4.0',
    'django-grappelli>=2.6.3',
    '# With Django>=1.9.0 we can remove django-pgjson because JSONField would be in the core:',
    '# https://docs.djangoproject.com/en/1.9/ref/contrib/postgres/fields/#jsonfield',
    'django-pgjson==0.3.1',
    'djangorestframework==3.1.1',
    'envdir>=0.7',
    'psycopg2>=2.5.4',
    'pytz>=2014.10',
]

extras_require = {
    'gunicorn': [
        'gunicorn==19.4.5',
    ],
    'newrelic': [
        'newrelic==2.60.0.46',
    ],
    'raven': [
        'raven==5.10.2',
    ],
    'whitenoise': [
        'whitenoise==2.0.6',
    ],
}

setup(
    name='hopper',
    version='0.1.0',
    description='A RESTful HTTP API for managing HTML forms.',
    long_description=read(BASE_DIR, 'README.rst'),
    author='transcode',
    author_email='team@transcode.de',
    extras_require=extras_require,
    include_package_data=True,
    install_requires=requires,
    license='BSD',
    packages=find_packages(exclude=['tests*']),
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
    ],
)
