import locale
from natural.constant import FILESIZE_SUFFIX
from natural.number import _format

FILESIZE_BASE = dict(
    decimal=1024,
    binary=1000,
    gnu=1024,
)


def filesize(value, format='decimal', digits=2):
    '''
    Convert a file size into natural readable format. Multiple formats are
    supported.

    :param value: size
    :param format: default ``decimal``, choices ``binary``, ``decimal`` or
                   ``gnu``
    :param digits: default ``2``

    >>> filesize(123)
    '123.00 B'
    >>> filesize(123456)
    '120.56 kB'
    >>> filesize(1234567890)
    '1.15 GB'
    '''

    if format not in FILESIZE_SUFFIX:
        raise TypeError

    base = FILESIZE_BASE[format]
    size = int(value)
    sign = size < 0 and u'-' or ''
    size = abs(size)

    for i, suffix in enumerate(FILESIZE_SUFFIX[format]):
        unit = base ** (i + 1)
        if size < unit:
            result = u''.join([
                sign,
                _format(base * size / float(unit), digits),
                u' ',
                suffix,
            ])
            if format == 'gnu':
                result = result.replace(' ', '')
            return result

    raise OverflowError


def decimalsize(value):
    '''
    Wrapper for :py:func:`filesize`.

    >>> decimalsize(123)
    '123.00 B'
    >>> decimalsize(123456)
    '120.56 kB'
    >>> decimalsize(1234567890)
    '1.15 GB'
    '''
    return filesize(value, format='decimal')


def binarysize(value):
    '''
    Wrapper for :py:func:`filesize`.

    >>> binarysize(123)
    '123.00 iB'
    >>> binarysize(123456)
    '123.46 KiB'
    >>> binarysize(1234567890)
    '1.23 GiB'
    '''
    return filesize(value, format='binary')


def gnusize(value, digits=1):
    '''
    Wrapper for :py:func:`filesize`.

    >>> gnusize(123)
    '123.0B'
    >>> gnusize(123456)
    '120.6K'
    >>> gnusize(1234567890)
    '1.1G'
    '''
    return filesize(value, format='gnu', digits=digits)
