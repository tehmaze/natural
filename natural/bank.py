from natural.constant import _, IBAN_ALPHABET
from natural.constant import BBAN_RULES, BBAN_PATTERN, BBAN_MAP
import re


def bban_compact(number):
    '''
    Printable compacted Basic Bank Account Number. Removes all the padding
    characters.

    :param number: string

    >>> bban_compact('1234.56.78.90')
    '1234567890'
    >>> bban_compact('068-9999995-01')
    '068999999501'
    '''
    return re.sub(r'[-. ]', '', str(number))


def bban_base10(number):
    '''
    Printable Basic Bank Account Number in base-10.

    :param number: string

    >>> bban_base10('01234567')
    '45670123'
    >>> bban_base10('ABCD')
    '10111213'
    '''
    number = bban_compact(number)
    number = number[4:] + number[:4]
    return ''.join([str(IBAN_ALPHABET.index(char)) for char in number])


def _bban_regex(structure):
    return re.compile(
        r'^%s$' % BBAN_PATTERN.sub(
            lambda m: '%s{%s}' % (BBAN_MAP[m.group(2)], m.group(1)),
            structure,
        )
    )


def bban(value, country=None, validate=False):
    '''
    Printable Basic Bank Account Number (BBAN) for the given country code. The
    ``country`` must be a valid ISO 3166-2 country code.

    :param value: string or int
    :param country: string

    >>> bban('068-9999995-01', 'BE')
    '068999999501'
    >>> bban('555', 'NL')
    '555'
    >>> bban('555', 'NL', validate=True)
    Traceback (most recent call last):
        ...
    ValueError: Invalid BBAN, number does not match specification
    >>> bban('123', 'XY', validate=True)
    Traceback (most recent call last):
        ...
    ValueError: Invalid BBAN, country unknown
    '''

    value = bban_compact(value)

    if validate:
        country = country.upper()

        try:
            rules = BBAN_RULES[country]
        except KeyError:
            raise ValueError(_('Invalid BBAN, country unknown'))

        regex = _bban_regex(rules['bban'])
        if not regex.match(value):
            raise ValueError(
                _('Invalid BBAN, number does not match specification')
            )

    return value


def iban(number, validate=False):
    '''
    Printable International Bank Account Number (IBAN) as specified in ISO
    13616.

    :param number: string

    >>> iban('BE43068999999501')
    'BE43 0689 9999 9501'
    >>> iban('XY32012341234123', validate=True)
    Traceback (most recent call last):
        ...
    ValueError: Invalid IBAN, country unknown
    >>> iban('BE43068999999502', validate=True)
    Traceback (most recent call last):
        ...
    ValueError: Invalid IBAN, digits check failed

    '''

    number = bban_compact(number)
    if validate:
        country = number[:2]
        if country not in BBAN_RULES:
            raise ValueError(_('Invalid IBAN, country unknown'))

        # Do the 10-mod-97 check
        digits = bban_base10(number)
        if int(digits) % 97 != 1:
            raise ValueError(_('Invalid IBAN, digits check failed'))

        # Check BBAN for country
        bban(number[4:], country, validate=True)

    groups = [number[x:x + 4] for x in range(0, len(number), 4)]
    return ' '.join(groups)
