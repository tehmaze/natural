``natural.size``
================

Examples
--------

Using the :py:func:`natural.size.filesize` function::

    >>> from natural.size import filesize
    >>> filesize(1)
    u'1 B'
    >>> filesize(1024)
    u'1 kB'
    >>> filesize(12345678)
    u'11.7738 MB'
    >>> filesize(12345678, 'binary')
    u'12.3457 MiB'
    >>> filesize(-12345678, 'gnu')
    u'-11.7738M'

API
---

.. automodule:: natural.size
    :members:
    :undoc-members:
    :show-inheritance:

