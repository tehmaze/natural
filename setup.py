#!/usr/bin/env python

from distutils.core import setup

setup(name='natural',
      version='0.0.1',
      description='Convert data to their natural (natural-readable) format',
      author='Wijnand Modderman-Lenstra',
      author_email='maze@pyth0n.org',
      url='https://github.com/tehmaze/natural',
      packages=['natural'],
      package_data={'natural': ['locale/*/LC_MESSAGES/*.mo']},
     )
