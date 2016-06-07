import locale
import re
import six
from natural.constant import ORDINAL_SUFFIX, LARGE_NUMBER_SUFFIX


def _format(value, digits=None):
    if isinstance(value, six.string_types):
        value = locale.atof(value)

    number = int(value)
    convention = locale.localeconv()

    if digits is None:
        digits = convention['frac_digits']

    partials = []
    if digits == 0:
        number = int(round(value, 0))
    else:
        fraction = str(round((value - number) * 10 ** digits)).split('.')[0]
        fraction = fraction[:digits]

        if len(fraction) < digits:
            fraction = fraction.ljust(digits, '0')

        if fraction:
            partials.append(fraction)
            partials.append(convention['decimal_point'])

    number = str(number)
    for x in six.moves.xrange(len(number) + 3, 0, -3):
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

    >>> ordinal(1)
    '1st'
    >>> ordinal(11)
    '11th'
    >>> ordinal(101)
    '101st'
    >>> ordinal(104)
    '104th'
    >>> ordinal(113)
    '113th'
    >>> ordinal(123)
    '123rd'
    '''

    try:
        value = int(value)
    except (TypeError, ValueError):
        raise ValueError

    if value % 100 in (11, 12, 13):
        return '%d%s' % (value, ORDINAL_SUFFIX[0])
    else:
        return '%d%s' % (value, ORDINAL_SUFFIX[value % 10])


def double(value, digits=2):
    '''
    Converts a number to a formatted double based on the current locale.

    :param value: number
    :param digits: default ``2``

    >>> double(42)
    '42.00'
    >>> double(42, digits=1)
    '42.0'
    >>> double(12.34)
    '12.34'
    >>> double(1234.56)
    '1,234.56'

    '''

    return six.u(_format(value, digits))


def number(value):
    '''
    Converts a number to a formatted number based on the current locale.

    :param value: number

    >>> number(42)
    '42'
    >>> number(12.34)
    '12'
    >>> number(1234)
    '1,234'
    >>> number(1234567)
    '1,234,567'

    '''

    return six.u(_format(value, 0))


def percentage(value, digits=2):
    '''
    Converts a fraction to a formatted percentage.

    :param value: number
    :param digits: default ``2``

    >>> percentage(1)
    '100.00 %'
    >>> percentage(0.23, digits=0)
    '23 %'
    >>> percentage(23.421)
    '2,342.10 %'

    '''

    value = float(value) * 100.0
    return '%s %%' % (_format(value, digits),)


def word(value, digits=2):
    '''
    Converts a large number to a formatted number containing the textual suffix
    for that number.

    :param value: number

    >>> word(1)
    '1'
    >>> word(123456789)
    '123.46 million'

    '''

    convention = locale.localeconv()
    decimal_point = convention['decimal_point']
    decimal_zero = re.compile(r'%s0+' % re.escape(decimal_point))
    prefix = value < 0 and '-' or ''
    value = abs(int(value))
    if value < 1000:
        return ''.join([
            prefix,
            decimal_zero.sub('', _format(value, digits)),
        ])

    for base, suffix in enumerate(LARGE_NUMBER_SUFFIX):
        exp = (base + 2) * 3
        power = 10 ** exp
        if value < power:
            value = value / float(10 ** (exp - 3))
            return ''.join([
                prefix,
                decimal_zero.sub('', _format(value, digits)),
                ' ',
                suffix,
            ])

    raise OverflowError
