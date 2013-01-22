#!/usr/bin/env python

from distutils.core import setup

setup(name='natural',
    version='0.1.3',
    description='Convert data to their natural (human-readable) format',
    long_description='''
Example Usage
=============

Basic usage::

    >>> from natural.file import accessed
    >>> print accessed(__file__)
    just now

We speak your language (with `your support`_)::

    >>> import locale
    >>> locale.setlocale(locale.LC_MESSAGES, 'nl_NL')
    >>> print accessed(__file__)
    zojuist

Bugs/Features
=============

You can issue a ticket in GitHub: https://github.com/tehmaze/natural/issues

Documentation
=============

The project documentation can be found at http://natural.rtfd.org/

.. _your support: http://natural.readthedocs.org/en/latest/locales.html
''',
    author='Wijnand Modderman-Lenstra',
    author_email='maze@pyth0n.org',
    license='MIT',
    keywords='natural data date file number size',
    url='https://github.com/tehmaze/natural',
    packages=['natural'],
    package_data={'natural': ['locale/*/LC_MESSAGES/*.mo']},
)
