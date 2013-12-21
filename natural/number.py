import locale
import string
from natural.constant import _, ORDINAL_SUFFIX, LARGE_NUMBER_SUFFIX
from natural.constant import IBAN_CHARS, IBAN_COUNTRY_SIZE


# ISO/IEC 7063:2003 - Information Technology - Security Techniques
#                   - Check character systems
IBAN_CHARS = string.ascii_uppercase + '0123456789'


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


def _iban_check_chars(number):
    for char in number:
        if char not in IBAN_CHARS:
            return False
    return True


def _iban_check_size(number):
    country = number[:2]
    if country not in IBAN_COUNTRY_SIZE:
        raise ValueError(_('Invalid IBAN, country "%s" unknown' % country))
    elif len(number) != IBAN_COUNTRY_SIZE[country]:
        raise ValueError(_('Invalid IBAN, country "%s" has size %d, got %d' % \
            (country, len(number), IBAN_COUNTRY_SIZE[country])))


def _iban_check_mod97(number):
    # Move the four initial characters to the end of the string.
    rearranged = number[4:] + number[:4]

    # Replace each letter in the string with two digits, thereby expanding the
    # string, where A = 10, B = 11, ..., Z = 35.
    sequence = []
    for char in rearranged:
        if char.isdigit():
            sequence.append(char)
        else:
            sequence.append(str(ord(char) - 55))

    # Interpret the string as a decimal integer and compute the remainder of
    # that number on division by 97. If the remainder is 1, the check digit
    # test is passed and the IBAN might be valid.
    if long(''.join(sequence)) % 97 != 1:
        raise ValueError(_('Invalid IBAN, digit check failed'))


def iban(value, strict=False):
    '''
    Converts an International Bank Account Number (IBAN) to a printable number.
    If strict mode is enabled, we'll check if the characters in the IBAN are
    conform ISO/IEC 7064:2003.

    :param value: string
    :param strict: boolean
    '''
    if isinstance(value, basestring):
        number = str(value).replace(' ', '')
    else:
        raise TypeError(_('IBAN must be a string'))

    if strict:
        _iban_check_chars(number)
        _iban_check_size(number)
        _iban_check_mod97(number)

    number = number.upper()
    return ' '.join([number[x:x + 4] for x in xrange(0, len(number), 4)])


def iban_mask(value, strict=False):
    '''
    Converts an International Bank Account Number (IBAN) to a masked printable
    number, suitable for printing in less secured environments. If strict mode
    is enabled, we'll check if the characters in the IBAN are conform ISO/IEC
    7064:2003.

    :param value: string
    :param strict: boolean
    '''
    number = str(value).replace(' ', '')
    prefix = number[:2]
    suffix = number[-4:]
    return iban(''.join([prefix, 'X' * (len(number) - 6), suffix]))


def percentage(value, digits=2):
    '''
    Converts a fraction to a formatted percentage.

    :param value: number
    :param digits: default ``2``
    '''

    value = float(value) * 100.0
    return u'%s %%' % (_format(value, digits),)


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
