import hashlib
import re
import six
from binascii import unhexlify
from natural.constant import PHONE_PREFIX, PHONE_E161_ALPHABET
from natural.language import _
from natural.util import luhn_append, luhn_calc, strip, to_decimal


def e123(number, areasize=3, groupsize=4, national=False):
    '''
    Printable E.123 (Notation for national and international telephone numbers
    from ITU) numbers.

    :param number: string
    :param areasize: int
    :param groupsize: int
    :param national: bool

    >>> e123(155542315678)
    '+1 555 4231 5678'
    >>> e123('+31654231567', areasize=1)
    '+31 6 5423 1567'
    >>> e123('+3114020', areasize=2)
    '+31 14 020'
    >>> e123('+312054231567', areasize=2, national=True)
    '(020) 5423 1567'
    '''

    if isinstance(number, six.integer_types):
        return e123('+%s' % number, areasize, groupsize)

    elif isinstance(number, six.string_types):
        number = strip(number, '-. ()')
        if number.startswith('+'):
            number = number[1:]

        if not number.isdigit():
            raise ValueError(_('Invalid telephone number'))

        groups = []
        prefix = ''
        remain = number

        if national:
            for x in six.moves.xrange(3, 0, -1):
                if number[:x] in PHONE_PREFIX:
                    groups.append('(0%s)' % number[x:x + areasize])
                    remain = number[x + areasize:]
                    break

        else:
            prefix = '+'
            for x in six.moves.xrange(3, 0, -1):
                if number[:x] in PHONE_PREFIX:
                    groups.append(number[:x])
                    groups.append(number[x:x + areasize])
                    remain = number[x + areasize:]
                    break

        for x in six.moves.xrange(0, len(remain) + 1, groupsize):
            groups.append(remain[x:x + groupsize])

        return '%s%s' % (prefix, ' '.join(list(filter(None, groups))))


def e161(number, alphabet=PHONE_E161_ALPHABET):
    '''
    Printable a 26 Latin letters (A to Z) phone number to the 12-key telephone
    keypad number.

    :param number: string
    :param alphabet: dict

    >>> e161('0800-PIZZA123')
    '080074992123'
    >>> e161('0800^PIZZA123')
    Traceback (most recent call last):
        ...
    ValueError: Character "^" (0x5e) is not in the E.161 alphabet
    '''

    digits = []
    for char in strip(number, '+-. ()').lower():
        length = len(digits)
        for group, digit in alphabet.items():
            if char in group:
                digits.append(digit)
                break

        if len(digits) == length:
            raise ValueError(
                _('Character "%s" (0x%02x) is not in the E.161 alphabet') %
                (char, ord(char))
            )

    return u''.join(digits)


def e164(number):
    '''
    Printable E.164 (The international public telecommunication numbering plan
    from ITU) numbers.

    :param number: string

    >>> e164(155542315678)
    '+155542315678'
    >>> e164('+31 20 5423 1567')
    '+312054231567'
    '''
    if isinstance(number, six.integer_types):
        return e164('+%s' % number)

    elif isinstance(number, six.string_types):
        number = strip(number, '-. ()')
        if number.startswith('+'):
            number = number[1:]

        return u'+%s' % number


def enum(number, zone='e164.arpa'):
    '''
    Printable DNS ENUM (telephone number mapping) record.

    :param number: string
    :param zone: string


    >>> enum('+31 20 5423 1567')
    '7.6.5.1.3.2.4.5.0.2.1.3.e164.arpa.'
    >>> enum('+31 97 99 6642', zone='e164.spacephone.org')
    '2.4.6.6.9.9.7.9.1.3.e164.spacephone.org.'

    '''
    number = e164(number).lstrip('+')
    return u'.'.join([
        u'.'.join(number[::-1]),
        zone.strip(u'.'),
        '',
    ])


def imei(number):
    '''
    Printable International Mobile Station Equipment Identity (IMEI) numbers.

    :param number: string or int

    >>> imei(12345678901234)
    '12-345678-901234-7'
    >>> imei(1234567890123456)
    '12-345678-901234-56'
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
    return u'-'.join(list(filter(None, groups)))


def imsi(number):
    '''
    Printable International Mobile Subscriber Identity (IMSI) numbers. Mind
    that there is no validation done on the actual correctness of the MCC/MNC.
    If you wish to validate IMSI numbers, take a look at `python-stdnum`_.

    :param number: string or int

    >>> imsi(2042312345)
    '204-23-12345'

    .. _python-stdnum: https://pypi.python.org/pypi/python-stdnum/
    '''
    number = to_decimal(number)
    groups = (number[:3], number[3:5], number[5:])
    return u'-'.join(list(filter(None, groups)))


def meid(number, separator=u' '):
    '''
    Printable Mobile Equipment Identifier (MEID) number.

    >>> meid(123456789012345678)
    '1B 69B4BA 630F34 6'
    >>> meid('1B69B4BA630F34')
    '1B 69B4BA 630F34 6'
    '''

    if isinstance(number, six.string_types):
        number = re.sub(r'[\s-]', '', number)

        try:
            number = '%014X' % int(number, 16)
        except ValueError:
            if len(number) < 18 and number.isdigit():
                return meid('%014X' % int(number), separator)
            else:
                raise ValueError(_('Invalid MEID, size mismatch'))
        else:
            if len(number) not in (14, 15):
                raise ValueError(_('Invalid MEID, size mismatch'))

    elif isinstance(number, six.integer_types):
        if number > 0xfffffffffffffff:
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
    return separator.join(list(filter(None, groups)))


def pesn(number, separator=u''):
    '''
    Printable Pseudo Electronic Serial Number.

    :param number: hexadecimal string

    >>> pesn('1B69B4BA630F34E')
    '805F9EF7'
    '''

    number = re.sub(r'[\s-]', '', meid(number))
    serial = hashlib.sha1(unhexlify(number[:14]))
    return separator.join(['80', serial.hexdigest()[-6:].upper()])
