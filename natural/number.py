import locale
import re
from natural.constant import CONVENTION, ORDINAL_SUFFIX, LARGE_NUMBER_SUFFIX


def ordinal(value):
    '''
    Converts a number to its ordinal representation.

    :param value: number
    '''

    try:
        value = long(value)
    except (TypeError, ValueError):
        raise ValueError

    if value % 100 in (11, 12, 13):
        return u'%d%s' % (value, ORDINAL_SUFFIX[0])
    else:
        return u'%d%s' % (value, ORDINAL_SUFFIX[value % 10])


def double(value):
    '''
    Converts a number to a formatted double based on the current locale.

    :param value: number
    '''

    return unicode(locale.format('%g', float(value), True))


def number(value):
    '''
    Converts a number to a formatted number based on the current locale.

    :param value: number
    '''

    return unicode(locale.format('%d', long(value), True))


def word(value):
    '''
    Converts a large number to a formatted number containing the textual suffix
    for that number.

    :param value: number
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
