# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import six
from natural.language import _


'''
.. py:attribute:: IBAN_ALPHABET

   Valid characters in an International Bank Account Number (IBAN).


.. py:attribute:: BBAN_RULES

   Per-country rules for Basic Bank Account Numbers (BBAN) and International
   Bank Account Numbers (IBAN), as specified by the Society for Worldwide
   Interbank Financial Telecommunication (SWIFT).


.. py:attribute:: BBAN_PATTERN

   Regular expression that captures a valid BBAN specification pattern.


.. py:attribute:: BBAN_MAP

   Map of BBAN specification pattern character groups.


.. py:attribute:: ORDINAL_SUFFIX

   Suffixes for the ordinal number representation.


.. py:attribute:: LARGE_NUMBER_SUFFIX

   Suffixes for the word number representation.


.. py:attribute:: FILESIZE_SUFFIX

   Suffixes for the file size representations.


.. py:function:: _(message)

   Return the localised translation of ``message``, based on the current global
   domain, language, and locales directory.


.. py:function:: _multi(singular, plural, count)

   Return the localised translation based on ``count``, the ``singular``
   version if ``count == 1``, the ``plural`` version otherwise.

'''


# natural.bank
BBAN_RULES = dict(
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
BBAN_PATTERN = re.compile(r'([1-9][0-9]*)!([acen])')
BBAN_MAP = dict(
    a=r'[A-Z]',
    c=r'[a-zA-Z0-9]',
    e=r' ',
    n=r'[0-9]',
)
IBAN_ALPHABET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# natural.number
ORDINAL_SUFFIX = (
    _('th'),
    _('st'),
    _('nd'),
    _('rd'),
    _('th'),
    _('th'),
    _('th'),
    _('th'),
    _('th'),
    _('th'),
)
LARGE_NUMBER_SUFFIX = (
    _('thousand'),
    _('million'),
    _('billion'),
    _('trillion'),
    _('quadrillion'),
    _('quintillion'),
    _('sextillion'),
    _('septillion'),
    _('octillion'),
    _('nonillion'),
    _('decillion'),
    _('undecillion'),
    _('duodecillion'),
    _('tredecillion'),
    _('quattuordecillion'),
    _('quindecillion'),
    _('sexdecillion'),
    _('septendecillion'),
    _('octodec'),
    _('novemdecillion'),
    _('vigintillion'),
    _('unvigintillion'),
    _('duovigintil'),
    _('tresvigintillion'),
    _('quattuorvigintillion'),
    _('quinquavigintillion'),
    _('sesvigintillion'),
    _('septemvigintillion'),
    _('octovigintillion'),
    _('novemvigintillion'),
    _('trigintillion'),
    _('untrigintillion'),
    _('duotrigintillion'),
    _('trestrigintillion'),
    _('quattuortrigintillion'),
    _('quinquatrigintillion'),
    _('sestrigintillion'),
    _('septentrigintillion'),
    _('octotrigintillion'),
    _('novemtrigintillion'),
    _('quadragintillion'),
)

# natural.file
FILESIZE_SUFFIX = dict(
    decimal=('B', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'),
    binary=('iB', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'),
    gnu='BKMGTPEZY',
)

# natural.data
PRINTABLE = list(map(lambda c: chr(c), six.moves.xrange(0x20, 0x7f)))
SPARKCHAR = '\u2581\u2582\u2583\u2584\u2585\u2586\u2587\u2588'

# natural.phone
PHONE_E161_ALPHABET = {
    '0':     '0',
    '1':     '1',
    '2abc':  '2',
    '3def':  '3',
    '4ghi':  '4',
    '5jkl':  '5',
    '6mno':  '6',
    '7prqs': '7',
    '8tuv':  '8',
    '9xyz':  '9',
    '*':     '*',
    '#':     '#',
}
PHONE_PREFIX = list(filter(None, re.split(r'[\n\s]*', '''
1   20  21  211 212 213 216 218 220 221 222 223 224 225 226 227 228 229 230 231
232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251
252 253 254 255 256 257 258 260 261 262 263 264 265 266 267 268 269 27  290 291
297 298 299 30  31  32  33  34  350 351 352 353 354 355 356 357 358 359 36  370
371 372 373 374 375 376 377 378 379 380 381 382 385 386 387 388 389 39  40  41
420 421 423 43  44  45  46  47  48  49  500 501 502 503 504 505 506 507 508 509
51  52  53  54  55  56  57  58  590 591 592 593 594 595 596 597 598 599 60  61
62  63  64  65  66  670 672 673 674 675 676 677 678 679 680 681 682 683 685 686
687 688 689 690 691 692 7   800 808 81  82  84  850 851 852 853 854 855 856 86
870 871 872 873 874 878 880 881 882 883 886 888 90  91  92  93  94  95  960 961
962 963 964 965 966 967 968 970 971 972 973 974 975 976 977 979 98  992 993 994
995 996 998
''')))

# natural.spelling
SPELL_ALPHABET = {
    'a': _('Amsterdam'),
    'ä': _('ä'),          # There is no en_US entry for this
    'b': _('Baltimore'),
    'c': _('Casablanca'),
    'd': _('Danmark'),
    'e': _('Edison'),
    'f': _('Florida'),
    'g': _('Gallipoli'),
    'h': _('Havanna'),
    'i': _('Italia'),
    'j': _('Jerusalem'),
    'k': _('Kilogramme'),
    'l': _('Liverpool'),
    'm': _('Madagaskar'),
    'n': _('New York'),
    'ñ': _('ñ'),          # There is no en_US entry for this
    'o': _('Oslo'),
    'ö': _('ö'),          # There is no en_US entry for this
    'p': _('Paris'),
    'q': _('Québec'),
    'r': _('Roma'),
    's': _('Santiago'),
    't': _('Tripoli'),
    'u': _('Uppsala'),
    'ü': _('ü'),          # There is no en_US entry for this
    'v': _('Valencia'),
    'w': _('Washington'),
    'x': _('Xantippe'),
    'y': _('Yokohama'),
    'z': _('Zürich'),
}
NATO_ALPHABET = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    'a': 'alpha',
    'b': 'bravo',
    'c': 'charlie',
    '-': 'dash',
    'd': 'delta',
    'e': 'echo',
    'f': 'foxtrot',
    'g': 'golf',
    'h': 'hotel',
    'i': 'india',
    'j': 'juliet',
    'k': 'kilo',
    'l': 'lima',
    'm': 'mike',
    'n': 'november',
    'o': 'oscar',
    'p': 'papa',
    'q': 'quebec',
    'r': 'romeo',
    's': 'sierra',
    '.': 'stop',
    't': 'tango',
    'u': 'uniform',
    'v': 'victor',
    'w': 'whiskey',
    'x': 'xray',
    'y': 'yankee',
    'z': 'zulu',
}
NATO_ALPHABET_PHONETIC = {
    '0': 'zee-ro',
    '1': 'wun',
    '2': 'too',
    '3': 'tree',
    '4': 'fow-er',
    '5': 'fife',
    '6': 'six',
    '7': 'sev-en',
    '8': 'ait',
    '9': 'nin-er',
    'a': 'alf-ah',
    'b': 'brah-voh',
    'c': 'char-lee',
    '-': 'das',
    'd': 'dell-tah',
    'e': 'eck-oh',
    'f': 'foks-trot',
    'g': 'golf',
    'h': 'hoh-tel',
    'i': 'in-dee-ah',
    'j': 'jew-lee-ett',
    'k': 'key-loh',
    'l': 'lee-mah',
    'm': 'mike',
    'n': 'no-vem-ber',
    'o': 'oss-cah',
    'p': 'pah-pah',
    'q': 'keh-beck',
    'r': 'row-me-oh',
    's': 'see-air-rah',
    '.': 'stop',
    't': 'tang-go',
    'u': 'you-nee-form',
    'v': 'vic-tah',
    'w': 'wiss-key',
    'x': 'ecks-ray',
    'y': 'yang-key',
    'z': 'zoo-loo',
}
CODE_ALPHABET_ARMY = ('  ', {
    '0': 'ZE roo',
    '1': 'OO nah wun',
    '2': 'BEES soh too',
    '3': 'TAY rah tree',
    '4': 'KAR tay fower',
    '5': 'PAN tah five',
    '6': 'SOK see six',
    '7': 'SAY tay seven',
    '8': 'OK toh eight',
    '9': 'NO vay niner',
    'a': 'AL fah',
    'b': 'BRAH voh',
    'c': 'CHAR lee',
    '-': 'DASH',
    'd': 'DEL tah',
    'e': 'EKK oh',
    'f': 'FOKS trot',
    'g': 'Golf',
    'h': 'HO tell',
    'i': 'IN dee ah',
    'j': 'JEW lee ett',
    'k': 'KEY loh',
    'l': 'LEE mah',
    'm': 'Mike',
    'n': 'NOH vem ber',
    'o': 'OSS car',
    'p': 'PAH pah',
    'q': 'keh BECK',
    'r': 'ROW me oh',
    's': 'see AIR ah',
    '.': 'STOP',
    't': 'TANG go',
    'u': 'YOU nee form',
    'v': 'VIK ter',
    'w': 'WISS key',
    'x': 'EKS ray',
    'y': 'YANG kee',
    'z': 'ZOO loo',
})
CODE_ALPHABET_FAA = (u' ', {
    '0': 'ZERO',
    '1': 'WUN',
    '2': 'TOO',
    '3': 'TREE',
    '4': 'FOW ER',
    '5': 'FIFE',
    '6': 'SIX',
    '7': 'SEV EN',
    '8': 'AIT',
    '9': 'NIN ER',
    'a': 'ALFAH',
    'b': 'BRAHVOH',
    'c': 'CHARLEE',
    'd': 'DELLTAH',
    'e': 'ECKOH',
    'f': 'FOKSTROT',
    'g': 'GOLF',
    'h': 'HOHTELL',
    'i': 'INDEE AH',
    'j': 'JEWLEE ETT',
    'k': 'KEYLOH',
    'l': 'LEEMAH',
    'm': 'MIKE',
    'n': 'NOVEMBER',
    'o': 'OSSCAH',
    'p': 'PAHPAH',
    'q': 'KEHBECK',
    'r': 'ROWME OH',
    's': 'SEEAIRAH',
    '.': 'STOP',
    't': 'TANGGO',
    'u': 'YOUNEE FORM',
    'v': 'VIKTAH',
    'w': 'WISSKEY',
    'x': 'ECKSRAY',
    'y': 'YANGKEY',
    'z': 'ZOOLOO',
})
CODE_ALPHABET_ICAO = ('  ', {
    '0': 'ZE RO',
    '1': 'OO NAH WUN',
    '2': 'TOO',
    '3': 'TREE',
    '4': 'FOW ER',
    '5': 'FIFE',
    '6': 'SIX',
    '7': 'SEVEN',
    '8': 'AIT',
    '9': 'NIN ER',
    'a': 'AL FAH',
    'b': 'BRAH VOH',
    'c': 'CHAR LEE',
    'd': 'DELL TAH',
    'e': 'ECK OH',
    'f': 'FOKS TROT',
    'g': 'GOLF',
    'h': 'HOH TELL',
    'i': 'IN DEE AH',
    'j': 'JEW LEE ETT',
    'k': 'KEY LOH',
    'l': 'LEE MAH',
    'm': 'MIKE',
    'n': 'NO VEM BER',
    'o': 'OSS CAH',
    'p': 'PAH PAH',
    'q': 'KEH BECK',
    'r': 'ROW ME OH',
    's': 'SEE AIR RAH',
    '.': 'STOP',
    't': 'TANG GO',
    'u': 'YOU NEE FORM',
    'v': 'VIK TAH',
    'w': 'WISS KEY',
    'x': 'ECKS RAY',
    'y': 'YANG KEY',
    'z': 'ZOO LOO',
})
CODE_ALPHABET_MORSE = (' ', {
    '=': '-...-',
    ' ': '/',
    '_': '..--.-',
    '-': '-....-',
    ',': '--..--',
    ';': '-.-.-.',
    ':': '---...',
    '!': '-.-.--',
    '?': '..--..',
    '/': '-..-.',
    '.': '.-.-.-',
    '"': '.-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '$': '..._.._',
    '&': '.-...',
    '+': '.-.-.',
    "'": '.----.',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    'a': '.-',
    '@': '.--.-.',      # A + C
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
})
CODE_ALPHABET_WORD = (' ', {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    'a': 'alfa',
    'b': 'bravo',
    'c': 'charlie',
    '-': 'dash',
    'd': 'delta',
    'e': 'echo',
    'f': 'foxtrot',
    'g': 'golf',
    'h': 'hotel',
    'i': 'india',
    'j': 'juliett',
    'k': 'kilo',
    'l': 'lima',
    'm': 'mike',
    'n': 'november',
    'o': 'oscar',
    'p': 'papa',
    'q': 'quebec',
    'r': 'romeo',
    's': 'sierra',
    '.': 'stop',
    't': 'tango',
    'u': 'uniform',
    'v': 'victor',
    'w': 'whiskey',
    'x': 'x-ray',
    'y': 'yankee',
    'z': 'zulu',
})
CODE_PRONOUNCIATION = {
    '0': _('ˈzɛroʊ'),
    '1': _('ˈwʌn'),
    '2': _('ˈtuː'),
    '3': _('ˈtriː'),
    '4': _('ˈfoʊ.ər'),
    '5': _('ˈfaɪf'),
    '6': _('ˈsɪks'),
    '7': _('ˈsɛvɛn'),
    '8': _('ˈeɪt'),
    '9': _('ˈnaɪnər'),
    'a': _('ælfɑ'),
    'b': _('ˈbrɑːˈvo'),
    'c': _('ˈtʃɑːli'),
    'd': _('ˈdeltɑ '),
    'e': _('ˈeko'),
    'f': _('ˈfɔkstrɔt'),
    'g': _('ɡʌlf'),
    'h': _('hoːˈtel'),
    'i': _('ˈindiˑɑ'),
    'j': _('ˈdʒuːliˑˈet'),
    'k': _('ˈkiːlo'),
    'l': _('ˈliːmɑ'),
    'm': _('mɑik'),
    'n': _('noˈvembə'),
    'o': _('ˈɔskɑ'),
    'p': _('pəˈpɑ'),
    'q': _('keˈbek'),
    'r': _('ˈroːmiˑo'),
    's': _('siˈerɑ'),
    't': _('ˈtænɡo'),
    '.': _('ˈstɒp'),
    'u': _('ˈjuːnifɔːm'),
    'v': _('ˈviktɑ'),
    'w': _('ˈwiski'),
    'x': _('ˈeksˈrei'),
    'y': _('ˈjænki'),
    'z': _('ˈzuːluː'),
}
