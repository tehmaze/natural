``natural.data``
================

Examples
--------

Using the :func:`natural.data.hexdump` function::

    >>> from natural.data import hexdump
    >>> hexdump(file('test.dat'))
    00000000  1f 8b 08 00 82 0d d9 4f  00 03 53 30 30 b0 02 22  |.......O..S00.."|
    00000010  63 13 85 d2 02 05 43 13  20 5b 47 41 c1 52 a1 b4  |c.....C. [GA.R..|
    00000020  38 b5 a8 18 c8 ca c9 4f  4c 51 48 2c 4b 2d 4a 4c  |8......OLQH,K-JL|
    00000030  4f b5 52 30 d0 33 37 d1  01 92 16 86 10 92 0b 00  |O.R0.37.........|
    00000040  21 df 77 14 3e 00 00 00                           |!.w.>...|


Using the :func:`natural.data.printable` function::

    >>> from natural.data import printable
    >>> print printable(file('test.dat').read())
    .......O..S00.."c.....C. [GA.R..8......OLQH,K-JLO.R0.37.........!.w.>...


Using the :func:`natural.data.sparkline` function::

    >>> from natural.data import sparkline
    >>> print sparkline([15, 21, 30, 23, 47, 41, 49, 33, 41, 41, 62, 0, 82])
    ▂▂▃▂▅▄▅▃▄▄▆▁█


Using the :func:`natural.data.throughput` function::

    >>> from natural.data import throughput
    >>> print throughput(456789012, 123)
    3,54169 MB/s
    >>> print throughput(456789012)
    435,628 MB/s
    >>> print throughput(456789012, format='binary')
    456,789 MiB/s


API
---

.. automodule:: natural.data
    :members:
    :undoc-members:
    :show-inheritance:

