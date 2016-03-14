#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

dependencies = []
with open('requirements.txt', 'r') as fd_requirements:
    for dependency in fd_requirements:
        dependencies.append(dependency.strip())


setup(
    name="python-test",
    packages=find_packages(),
    install_requires = dependencies
)

