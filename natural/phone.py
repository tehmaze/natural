import hashlib
import re
from natural.language import _
from natural.util import luhn_append, luhn_calc, to_decimal


def imei(number):
    '''
    Printable International Mobile Station Equipment Identity (IMEI) numbers.

    :param number: string, int or long

    >>> print imei(12345678901234)
    12-345678-901234-7
    >>> print imei(1234567890123456)
    12-345678-901234-56
    '''
    number = to_decimal(number)
    length = len(number)
    if length not in (14, 15, 16):
        raise ValueError(
            _('Invaid International Mobile Station Equipment Identity')
        )

    if len(number) == 14:
        # Add Luhn check digit
        number = luhn_append(number)

    groups = (number[:2], number[2:8], number[8:14], number[14:])
    return u'-'.join(filter(None, groups))


def imsi(number):
    '''
    Printable International Mobile Subscriber Identity (IMSI) numbers. Mind
    that there is no validation done on the actual correctness of the MCC/MNC.
    If you wish to validate IMSI numbers, take a look at `python-stdnum`_.

    :param number: string, int or long

    >>> print imsi(2042312345)
    204-23-12345

    .. _python-stdnum: https://pypi.python.org/pypi/python-stdnum/
    '''
    number = to_decimal(number)
    groups = (number[:3], number[3:5], number[5:])
    return u'-'.join(filter(None, groups))


def meid(number, separator=u' '):
    '''
    Printable Mobile Equipment Identifier (MEID) number.

    >>> meid(123456789012345678)
    u'1B 69B4BA 630F34 6'
    >>> meid('1B69B4BA630F34')
    u'1B 69B4BA 630F34 6'
    '''

    if isinstance(number, basestring):
        number = re.sub(r'[\s-]', '', number)

        try:
            number = '%014X' % long(number, 16)
        except ValueError:
            if len(number) < 18 and number.isdigit():
                return meid('%014X' % long(number), separator)
            else:
                raise ValueError(_('Invalid MEID, size mismatch'))
        else:
            if len(number) not in (14, 15):
                raise ValueError(_('Invalid MEID, size mismatch'))

    elif isinstance(number, (int, long)):
        if number > 0xfffffffffffffffL:
                raise ValueError(_('Invalid MEID, size mismatch'))
        return meid(('%014X' % number)[:14], separator)

    else:
        raise TypeError(_('Invalid MEID, input type invalid'))

    number = number.upper()
    region = number[:2]
    manufacturer = number[2:8]
    serial_number = number[8:14]
    check_digit = number[14:]

    if check_digit == '':
        check_digit = luhn_calc(number, chars='0123456789ABCDEF')

    groups = (region, manufacturer, serial_number, check_digit)
    return separator.join(filter(None, groups))


def pesn(number, separator=u''):
    '''
    Printable Pseudo Electronic Serial Number.

    :param number: hexadecimal string

    >>> pesn('1B69B4BA630F34E')
    u'805F9EF7'
    '''

    number = re.sub(r'[\s-]', '', meid(number))
    serial = hashlib.sha1(number[:14].decode('hex'))
    return separator.join(['80', serial.hexdigest()[-6:].upper()])
