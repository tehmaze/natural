.. Natural documentation master file, created by
   sphinx-quickstart on Wed Jun 13 17:18:42 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Natural's documentation!
===================================

Natural is a Python library to easily transform data into human-readable
formats such as dates, time differences, numbers and sizes.

Features:

 * Natural is not using any third-party libraries, so it runs from a bare Python installation

 * Natural is fully internationalised and speaks :doc:`your language <locales>`

 * Natural uses unicode strings where possible

 * Natural is PEP8_ compliant

 * Natural has an extensive `test suite`_

.. _PEP8: http://www.python.org/dev/peps/pep-0008/
.. _test suite: http://nose.readthedocs.org/en/latest/


Demo:

.. doctest::

    >>> from natural import date, number, size
    >>> import datetime
    >>> date.compress(datetime.datetime(2012, 01, 01, 23, 42))
    u'23w2d17h52m59s'
    >>> number.word(2300000)
    u'2.3 million'
    >>> size.filesize(102410241024)
    u'95.377 GB'


We speak :doc:`your language <locales>` too!

.. doctest::

    >>> import locale
    >>> locale.setlocale(locale.LC_ALL, 'de_DE')
    >>> from natural import date
    >>> date.duration(1337000000)   # doctest: +SKIP
    u'vor 4 Wochen'


Download
========

There are no official releases yet, however you can get the latest snapshots:

 * `tarball <https://github.com/tehmaze/natural/tarball/master>`_
 
 * `zipball <https://github.com/tehmaze/natural/zipball/master>`_

 * `git repository at GitHub <https://github.com/tehmaze/natural>`_


Contents
========

.. toctree::
   :maxdepth: 2

   natural/bank
   natural/data
   natural/date
   natural/file
   natural/number
   natural/size
   natural/text
   locales
   django


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

