# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='dozer',
    version='0.0.1',
    description='dozer makes graph data RESTful',
    long_description=readme,
    author='Steven McCauley',
    author_email='me@stevenmccauley.me',
    url='http://github.com/Brown-University-Library/dozer',
    license='MIT',
    packages=find_packages(exclude=('sample','tests', 'docs'))
)