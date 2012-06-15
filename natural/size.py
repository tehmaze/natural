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
    '''

    if not format in FILESIZE_SUFFIX:
        raise TypeError

    base = FILESIZE_BASE[format]
    size = long(value)
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
    '''
    return filesize(value, format='decimal')


def binarysize(value):
    '''
    Wrapper for :py:func:`filesize`.
    '''
    return filesize(value, format='binary')


def gnusize(value, digits=1):
    '''
    Wrapper for :py:func:`filesize`.
    '''
    return filesize(value, format='gnu', digits=digits)
