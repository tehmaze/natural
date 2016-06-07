import re
import six


# Default Luhn check digits (base-10)
DIGITS = '0123456789'


def luhn_checksum(number, chars=DIGITS):
    '''
    Calculates the Luhn checksum for `number`

    :param number: string or int
    :param chars: string

    >>> luhn_checksum(1234)
    4

    '''
    length = len(chars)
    number = [chars.index(n) for n in reversed(str(number))]
    return (
        sum(number[::2]) +
        sum(sum(divmod(i * 2, length)) for i in number[1::2])
    ) % length


def luhn_calc(number, chars=DIGITS):
    '''
    Calculate the Luhn check digit for ``number``.

    :param number: string
    :param chars: string

    >>> luhn_calc('42')
    '2'

    '''

    checksum = luhn_checksum(str(number) + chars[0], chars)
    return chars[-checksum]


def luhn_append(number, chars=DIGITS):
    '''
    Append the Luhn check digit of ``number`` to the input.

    :param number: string
    :param chars: string

    >>> luhn_append('666')
    '6668'

    '''
    return str(number) + luhn_calc(number, chars)


def strip(value, chars):
    '''
    Removes characters in ``chars`` from input ``value``.

    :param value: string
    :param chars: iterable

    >>> strip('hello.world', '.')
    'helloworld'
    '''
    return u''.join([x for x in value if x not in chars])


def to_decimal(number, strip='- '):
    '''
    Converts a number to a string of decimals in base 10.

    >>> to_decimal(123)
    '123'
    >>> to_decimal('o123')
    '83'
    >>> to_decimal('b101010')
    '42'
    >>> to_decimal('0x2a')
    '42'
    '''
    if isinstance(number, six.integer_types):
        return str(number)

    number = str(number)
    number = re.sub(r'[%s]' % re.escape(strip), '', number)

    # hexadecimal
    if number.startswith('0x'):
        return to_decimal(int(number[2:], 16))

    # octal
    elif number.startswith('o'):
        return to_decimal(int(number[1:], 8))

    # binary
    elif number.startswith('b'):
        return to_decimal(int(number[1:], 2))

    else:
        return str(int(number))
