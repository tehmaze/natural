``natural.date``
================

Examples
--------

Using the :py:func:`natural.date.compress` function::

    >>> from natural.date import compress
    >>> print compress(123)
    2m3s
    >>> print compress(123456)
    1d10h17m36s

Using the :py:func:`natural.date.day` function::

    >>> from natural.date import day
    >>> from datetime import datetime, timedelta
    >>> now = datetime.now()
    >>> print delta(now, now - timedelta(seconds=10))
    just now
    >>> print delta(now, now - timedelta(days=7))
    1 week

Using the :py:func:`natural.date.delta` function::

    >>> from natural.date import delta
    >>> import os, stat
    >>> print day(os.stat(__file__)[stat.ST_MTIME])
    today
    >>> print day(os.stat('/etc/fstab')[stat.ST_MTIME])
    May 02

Using the :py:func:`natural.date.duration` function::

    >>> from natural.date import duration
    >>> from os.path import getmtime
    >>> print duration(getmtime('/etc/fstab'))
    1 month ago
    >>> print duration(getmtime('/etc/issue'))
    2 months ago
    >>> print duration(getmtime('/etc/issue'), precision=3)
    2 months, 1 week, 42 seconds ago


API
---

.. automodule:: natural.date
    :members:
    :undoc-members:
    :show-inheritance:

