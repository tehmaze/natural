import locale
import re
from natural.constant import CONVENTION, ORDINAL_SUFFIX, LARGE_NUMBER_SUFFIX


def ordinal(value):
    '''
    Converts a number to its ordinal representation.

    >>> ordinal(1)
    u'1st'
    >>> ordinal(11)
    u'11th'
    >>> ordinal(113)
    u'113th'
    >>> ordinal(101)
    u'101st'
    '''

    try:
        value = long(value)
    except (TypeError, ValueError):
        raise ValueError

    if value % 100 in (11, 12, 13):
        return u'%d%s' % (value, ORDINAL_SUFFIX[0])
    else:
        return u'%d%s' % (value, ORDINAL_SUFFIX[value % 10])


def double(value, precision=2):
    '''
    Converts a number to a formatted double based on the current locale.

    >>> double(23.42)
    u'23.42'
    >>> double(1234.56)
    u'1,234.56'

    For nl_NL locale:

    >>> double(23.42) # doctest:+SKIP
    u'23,42'
    '''

    return unicode(locale.format('%g', float(value), True))


def number(value, group=0):
    '''
    Converts a number to a formatted number based on the current locale.

    >>> number(1)
    u'1'
    >>> number(1234)
    u'1,234'
    >>> number('1234567')
    u'1,234,567'
    >>> number('1234567890')
    u'1,234,567,890'
    '''

    return unicode(locale.format('%d', long(value), True))


def word(value):
    '''
    Converts a large number to a formatted number containing the textual suffix
    for that number.

    >>> word(1)
    u'1'
    >>> word(1000)
    u'1 thousand'
    >>> word(1000000)
    u'1 million'
    >>> word(1200000000)
    u'1.2 billion'
    >>> word(-1200000000)
    u'-1.2 billion'
    >>> word(42230000000000000000000)
    u'42.23 sextillion'
    '''

    prefix = value < 0 and u'-' or u''
    value = abs(long(value))
    if value < 1000L:
        return u''.join([
            prefix,
            str(value),
        ])

    for base, suffix in enumerate(LARGE_NUMBER_SUFFIX):
        exp = (base + 2) * 3
        power = 10 ** exp
        if value < power:
            value = value / float(10 ** (exp - 3))
            return u''.join([
                prefix,
                locale.format('%g', value, True),
                u' ',
                suffix,
            ])

    raise OverflowError

if __name__ == "__main__":
    import locale
    lang, encoding = locale.getlocale(locale.LC_ALL)
    if lang != 'en_US':
        print 'Doctest only works for en_US'
    else:
        print 'Running doctests for locale', lang
        import doctest
        doctest.testmod()
