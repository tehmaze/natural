import locale
import re
from natural.constant import CONVENTION, ORDINAL_SUFFIX, LARGE_NUMBER_SUFFIX


def _format(value, digits=None):
    if isinstance(value, basestring):
        value = locale.atof(value)

    number = long(value)
    convention = locale.localeconv()

    if digits is None:
        digits = convention['frac_digits']

    partials = []
    if digits == 0:
        number = long(round(value, 0))
    else:
        fraction = str(round((value - number) * 10 ** digits)).split('.')[0]
        fraction = fraction[:digits]

        if len(fraction) < digits:
            fraction = fraction.ljust(digits, '0')

        if fraction:
            partials.append(fraction)
            partials.append(convention['decimal_point'])

    number = str(number)
    for x in xrange(len(number) + 3, 0, -3):
        partial = number[max(0, x - 3):x]
        if partial:
            partials.append(number[max(0, x - 3):x])
            partials.append(convention['thousands_sep'])

    if partials[-1] == convention['thousands_sep']:
        partials = partials[:-1]

    partials.reverse()
    return ''.join(partials)


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


def double(value, digits=2):
    '''
    Converts a number to a formatted double based on the current locale.

    :param value: number
    :param digits: default ``2``
    '''

    return unicode(_format(value, digits))


def number(value):
    '''
    Converts a number to a formatted number based on the current locale.

    :param value: number
    '''

    return unicode(_format(value, 0))


def percentage(value, digits=2):
    '''
    Converts a fraction to a formatted percentage.

    :param value: number
    :param digits: default ``2``
    '''

    value = float(value) * 100.0
    return u'{} %'.format(_format(value, digits))


def word(value, digits=2):
    '''
    Converts a large number to a formatted number containing the textual suffix
    for that number.

    :param value: number
    '''

    convention = locale.localeconv()
    decimal_point = convention['decimal_point']
    prefix = value < 0 and u'-' or u''
    value = abs(long(value))
    if value < 1000L:
        return u''.join([
            prefix,
            _format(value, digits).rstrip('%s0' % (decimal_point,)),
        ])

    for base, suffix in enumerate(LARGE_NUMBER_SUFFIX):
        exp = (base + 2) * 3
        power = 10 ** exp
        if value < power:
            value = value / float(10 ** (exp - 3))
            return u''.join([
                prefix,
                _format(value, digits).rstrip('%s0' % (decimal_point,)),
                u' ',
                suffix,
            ])

    raise OverflowError
