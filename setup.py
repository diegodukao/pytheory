#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='Pytheory-testing',
    version='0.2',
    description='',
    author='',
    author_email='',
    url='',
    packages=find_packages(exclude=('tests',)),
    install_requires=["pytuning", "numeral", "pygame", "scipy"],
)
