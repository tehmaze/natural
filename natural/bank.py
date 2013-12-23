from natural.constant import _
import re


class BBAN(object):
    _alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    _rules = dict(
        AD=dict(bban='4!n4!n12!c',
                name=_('Andorra')),
        AE=dict(bban='3!n16!n',
                name=_('United Arab Emirates')),
        AL=dict(bban='8!n16!c',
                name=_('Albania')),
        AT=dict(bban='5!n11!n',
                name=_('Austria')),
        AZ=dict(bban='4!a20!c',
                name=_('Republic of Azerbaijan')),
        BA=dict(bban='3!n3!n8!n2!n',
                name=_('Bosnia and Herzegovina')),
        BE=dict(bban='3!n7!n2!n',
                name=_('Belgium')),
        BG=dict(bban='4!a4!n2!n8!c',
                name=_('Bulgaria')),
        BH=dict(bban='4!a14!c',
                name=_('Bahrain (Kingdom of)')),
        BR=dict(bban='8!n5!n10!n1!a1!c',
                name=_('Brazil')),
        CH=dict(bban='5!n12!c',
                name=_('Switzerland')),
        CR=dict(bban='3!n14!n',
                name=_('Costa Rica')),
        CY=dict(bban='3!n5!n16!c',
                name=_('Cyprus')),
        CZ=dict(bban='4!n6!n10!n',
                name=_('Czech Republic')),
        DE=dict(bban='8!n10!n',
                name=_('Germany')),
        DK=dict(bban='4!n9!n1!n',
                name=_('Denmark')),
        FO=dict(bban='4!n9!n1!n',
                name=_('Denmark (Faroe Islands')),
        GL=dict(bban='4!n9!n1!n',
                name=_('Denmark (Greenland)')),
        DO=dict(bban='4!c20!n',
                name=_('Dominican Republic')),
        EE=dict(bban='2!n2!n11!n1!n',
                name=_('Estonia')),
        ES=dict(bban='4!n4!n1!n1!n10!n',
                name=_('Spain')),
        FI=dict(bban='Not in use',
                name=_('Finland')),
        FR=dict(bban='5!n5!n11!c2!n',
                name=_('France')),
        GB=dict(bban='4!a6!n8!n',
                name=_('United Kingdom')),
        GE=dict(bban='2!a16!n',
                name=_('Georgia')),
        GI=dict(bban='4!a15!c',
                name=_('Gibraltar')),
        GR=dict(bban='3!n4!n16!c',
                name=_('Greece')),
        GT=dict(bban='4!c20!c',
                name=_('Guatemala')),
        HR=dict(bban='7!n10!n',
                name=_('Croatia')),
        HU=dict(bban='3!n4!n1!n15!n1!n',
                name=_('Hungary')),
        IE=dict(bban='4!a6!n8!n',
                name=_('Ireland')),
        IL=dict(bban='3!n3!n13!n',
                name=_('Israel')),
        IS=dict(bban='4!n2!n6!n10!n',
                name=_('Iceland')),
        IT=dict(bban='1!a5!n5!n12!c',
                name=_('Italy')),
        KW=dict(bban='4!a22!c',
                name=_('Kuwait')),
        KZ=dict(bban='3!n13!c',
                name=_('Kazakhstan')),
        LB=dict(bban='4!n20!c',
                name=_('Lebanon')),
        LI=dict(bban='5!n12!c',
                name=_('Liechtenstein (Principality of)')),
        LT=dict(bban='5!n11!n',
                name=_('Lithuania')),
        LU=dict(bban='3!n13!c',
                name=_('Luxembourg')),
        LV=dict(bban='4!a13!c',
                name=_('Latvia')),
        MC=dict(bban='5!n5!n11!c2!n',
                name=_('Monaco')),
        MD=dict(bban='2!c18!c',
                name=_('Republic of Moldova')),
        ME=dict(bban='3!n13!n2!n',
                name=_('Montenegro')),
        MK=dict(bban='3!n10!c2!n',
                name=_('Macedonia, Former Yugoslav Republic of')),
        MR=dict(bban='5!n5!n11!n2!n',
                name=_('Mauritania')),
        MT=dict(bban='4!a5!n18!c',
                name=_('Malta')),
        MU=dict(bban='4!a2!n2!n12!n3!n3!a',
                name=_('Mauritius')),
        NL=dict(bban='4!a10!n',
                name=_('The Netherlands')),
        NO=dict(bban='4!n6!n1!n ',
                name=_('Norway')),
        PK=dict(bban='4!a16!c',
                name=_('Pakistan')),
        PL=dict(bban='8!n16!n',
                name=_('Poland')),
        PS=dict(bban='4!a21!c',
                name=_('Palestine, State of')),
        PT=dict(bban='4!n4!n11!n2!n',
                name=_('Portugal')),
        QA=dict(bban='2!n4!a21!c',
                name=_('Qatar')),
        RO=dict(bban='4!a16!c',
                name=_('Romania')),
        RS=dict(bban='3!n13!n2!n',
                name=_('Serbia')),
        SA=dict(bban='2!n18!c',
                name=_('Saudi Arabia')),
        SE=dict(bban='3!n16!n1!n',
                name=_('Sweden')),
        SI=dict(bban='5!n8!n2!n',
                name=_('Slovenia')),
        SK=dict(bban='4!n6!n10!n',
                name=_('Slovak Republic')),
        SM=dict(bban='1!a5!n5!n12!c',
                name=_('San Marino')),
        TN=dict(bban='2!n3!n13!n2!n',
                name=_('Tunisia')),
        TR=dict(bban='5!n1!c16!c',
                name=_('Turkey')),
        VG=dict(bban='4!a16!n',
                name=_('Virgin Islands, British')),
    )
    _bban_sre = re.compile(r'([1-9][0-9]*)!([acen])')
    _bban_map = dict(
        a=r'[A-Z]',
        c=r'[a-zA-Z0-9]',
        e=r' ',
        n=r'[0-9]',
    )

    @staticmethod
    def _regex(structure):
        return re.compile(
            r'^%s$' % IBAN._bban_sre.sub(
                lambda m: '%s{%s}' % (BBAN._bban_map[m.group(2)], m.group(1)),
                structure,
            )
        )

    @staticmethod
    def base10(number):
        number = IBAN.compact(number)
        number = number[4:] + number[:4]
        return ''.join([str(IBAN._alphabet.index(char)) for char in number])

    @staticmethod
    def validate(bban, country):
        rules = BBAN._rules[country]
        regex = BBAN._regex(rules['bban'])
        if regex.match(bban):
            return True
        else:
            country = rules['country']
            raise ValueError(_('Invalid BBAN for %s') % country)


class IBAN(BBAN):
    @staticmethod
    def compact(number):
        return re.sub(r'[ -]', '', number)

    @staticmethod
    def format(number):
        number = IBAN.compact(number)
        return ' '.join([
            number[x:x + 4]
            for x in xrange(0, len(number), 4)
        ])

    @staticmethod
    def validate(number):
        # First two digits must be a valid ISO 3166-2 country code
        country = number[:2]
        try:
            BBAN._rules[country]
        except KeyError:
            raise ValueError(_('Invalid IBAN, country unknown'))

        digits = IBAN.base10(number)
        if long(digits) % 97 != 1:
            raise ValueError(_('Invalid IBAN, digits check failed'))

        bban = number[4:]
        return BBAN.validate(bban, country)


# vim:fdm=indent
