import locale
from natural.constant import FILESIZE_SUFFIX

FILESIZE_BASE = dict(
    decimal=1024,
    binary=1000,
    gnu=1024,
)


def filesize(value, format='decimal'):
    '''
    Convert a file size into natural readable format. Multiple formats are
    supported.

    :param value: size
    :param format: default ``decimal``, choices ``binary``, ``decimal`` or ``gnu``
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
                locale.format('%g', base * size / float(unit), True),
                u' ',
                suffix,
            ])
            if format == 'gnu':
                result = result.replace(' ', '')
            return result

    raise OverflowError


def decimalsize(value):
    '''
    Wrapper for :py:func:``filesize``.
    '''
    return filesize(value, format='decimal')


def binarysize(value):
    '''
    Wrapper for :py:func:``filesize``.
    '''
    return filesize(value, format='binary')


def gnusize(value):
    '''
    Wrapper for :py:func:``filesize``.
    '''
    return filesize(value, format='gnu')


if __name__ == "__main__":
    import locale
    lang, encoding = locale.getlocale(locale.LC_ALL)
    if lang != 'en_US':
        print 'Doctest only works for en_US'
    else:
        print 'Running doctests for locale', lang
        import doctest
        doctest.testmod()
