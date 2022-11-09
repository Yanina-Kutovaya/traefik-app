#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(name='traefik-app',
      version='1.0',
      description='Traefik basic application',
      author='Yanina Kutovaya',
      author_email='kutovaiayp@yandex.ru',
      url='https://github.com/Yanina-Kutovaya/traefik-app.git',
      package_dir={"": "src"},
      packages=find_packages(where="src"),
     )