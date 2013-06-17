#!/usr/bin/env python
import os
import sys

from dynamicresponse import __version__
from setuptools import setup

def publish():
    """Publish to Pypi"""
    os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
    publish()
    sys.exit()

setup(
    name='django-dynamicresponse',
    version=__version__,
    description='Lightweight framework for easily providing REST APIs for web apps built with Django.',
    long_description=open('README.md').read(),
    author='Funkbit',
    author_email='post@funkbit.no',
    url='https://github.com/funkbit/django-dynamicresponse',
    packages=['dynamicresponse', 'dynamicresponse.middleware'],
    tests_require=['django>=1.1'],
    test_suite='examples.myblog.blog.runtests.runtests',
    license='BSD',
    classifiers=(
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    )
)
