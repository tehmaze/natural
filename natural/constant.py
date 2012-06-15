# -*- coding: utf-8 -*-
import gettext
import locale
import os


'''
.. py:attribute:: LOCALE_PATH

   Path on the file system to the locale/ directory, used to find translations
   for the current locale.


.. py:attribute:: CONVENTION

   Container for all the locale conventions, see
   http://docs.python.org/library/locale.html#locale.localeconv


.. py:attribute:: ORDINAL_SUFFIX

   Suffixes for the ordinal number representation.


.. py:attribute:: LARGE_NUMBER_SUFFIX

   Suffixes for the word number representation.


.. py:attribute:: FILESIZE_SUFFIX

   Suffixes for the file size representations.


.. py:function:: _(message)

   Return the localised translation of ``message``, based on the current global
   domain, language, and locale directory.


.. py:function:: _multi(singular, plural, count)

   Return the localised translation based on ``count``, the ``singular``
   version if ``count == 1``, the ``plural`` version otherwise.

'''


locale.setlocale(locale.LC_ALL, '')

LOCALE_PATH = os.path.join(os.path.dirname(__file__), 'locale')
gettext.bindtextdomain('natural', LOCALE_PATH)
gettext.textdomain('natural')
try:
    TRANSLATION = gettext.translation('natural', LOCALE_PATH)
    _ = TRANSLATION.ugettext
except IOError:
    _ = gettext.NullTranslations().ugettext

# generic
CONVENTION = locale.localeconv()
# natural.number
ORDINAL_SUFFIX = (
    _(u'th'),
    _(u'st'),
    _(u'nd'),
    _(u'rd'),
    _(u'th'),
    _(u'th'),
    _(u'th'),
    _(u'th'),
    _(u'th'),
    _(u'th'),
)
LARGE_NUMBER_SUFFIX = (
    _(u'thousand'),
    _(u'million'),
    _(u'billion'),
    _(u'trillion'),
    _(u'quadrillion'),
    _(u'quintillion'),
    _(u'sextillion'),
    _(u'septillion'),
    _(u'octillion'),
    _(u'nonillion'),
    _(u'decillion'),
    _(u'undecillion'),
    _(u'duodecillion'),
    _(u'tredecillion'),
    _(u'quattuordecillion'),
    _(u'quindecillion'),
    _(u'sexdecillion'),
    _(u'septendecillion'),
    _(u'octodec'),
    _(u'novemdecillion'),
    _(u'vigintillion'),
    _(u'unvigintillion'),
    _(u'duovigintil'),
    _(u'tresvigintillion'),
    _(u'quattuorvigintillion'),
    _(u'quinquavigintillion'),
    _(u'sesvigintillion'),
    _(u'septemvigintillion'),
    _(u'octovigintillion'),
    _(u'novemvigintillion'),
    _(u'trigintillion'),
    _(u'untrigintillion'),
    _(u'duotrigintillion'),
    _(u'trestrigintillion'),
    _(u'quattuortrigintillion'),
    _(u'quinquatrigintillion'),
    _(u'sestrigintillion'),
    _(u'septentrigintillion'),
    _(u'octotrigintillion'),
    _(u'novemtrigintillion'),
    _(u'quadragintillion'),
)
# natural.file
FILESIZE_SUFFIX = dict(
    decimal=('B', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'),
    binary=('iB', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'),
    gnu='BKMGTPEZY',
)
# natural.data
PRINTABLE = map(lambda c: chr(c), xrange(0x20, 0x7f))
SPARKCHAR = u'\u2581\u2582\u2583\u2584\u2585\u2586\u2587\u2588'
# natural.spelling
SPELL_ALPHABET = {
    u'a': _(u'Amsterdam'),
    u'ä': _(u'ä'),          # There is no en_US entry for this
    u'b': _(u'Baltimore'),
    u'c': _(u'Casablanca'),
    u'd': _(u'Danmark'),
    u'e': _(u'Edison'),
    u'f': _(u'Florida'),
    u'g': _(u'Gallipoli'),
    u'h': _(u'Havanna'),
    u'i': _(u'Italia'),
    u'j': _(u'Jerusalem'),
    u'k': _(u'Kilogramme'),
    u'l': _(u'Liverpool'),
    u'm': _(u'Madagaskar'),
    u'n': _(u'New York'),
    u'ñ': _(u'ñ'),          # There is no en_US entry for this
    u'o': _(u'Oslo'),
    u'ö': _(u'ö'),          # There is no en_US entry for this
    u'p': _(u'Paris'),
    u'q': _(u'Québec'),
    u'r': _(u'Roma'),
    u's': _(u'Santiago'),
    u't': _(u'Tripoli'),
    u'u': _(u'Uppsala'),
    u'ü': _(u'ü'),          # There is no en_US entry for this
    u'v': _(u'Valencia'),
    u'w': _(u'Washington'),
    u'x': _(u'Xantippe'),
    u'y': _(u'Yokohama'),
    u'z': _(u'Zürich'),
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
CODE_ALPHABET_ARMY = (u'  ', {
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
CODE_ALPHABET_ICAO = (u'  ', {
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
CODE_ALPHABET_MORSE = (u' ', {
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
CODE_ALPHABET_WORD = (u' ', {
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
    '0': _(u'ˈzɛroʊ'),
    '1': _(u'ˈwʌn'),
    '2': _(u'ˈtuː'),
    '3': _(u'ˈtriː'),
    '4': _(u'ˈfoʊ.ər'),
    '5': _(u'ˈfaɪf'),
    '6': _(u'ˈsɪks'),
    '7': _(u'ˈsɛvɛn'),
    '8': _(u'ˈeɪt'),
    '9': _(u'ˈnaɪnər'),
    'a': _(u'ælfɑ'),
    'b': _(u'ˈbrɑːˈvo'),
    'c': _(u'ˈtʃɑːli'),
    'd': _(u'ˈdeltɑ '),
    'e': _(u'ˈeko'),
    'f': _(u'ˈfɔkstrɔt'),
    'g': _(u'ɡʌlf'),
    'h': _(u'hoːˈtel'),
    'i': _(u'ˈindiˑɑ'),
    'j': _(u'ˈdʒuːliˑˈet'),
    'k': _(u'ˈkiːlo'),
    'l': _(u'ˈliːmɑ'),
    'm': _(u'mɑik'),
    'n': _(u'noˈvembə'),
    'o': _(u'ˈɔskɑ'),
    'p': _(u'pəˈpɑ'),
    'q': _(u'keˈbek'),
    'r': _(u'ˈroːmiˑo'),
    's': _(u'siˈerɑ'),
    't': _(u'ˈtænɡo'),
    '.': _(u'ˈstɒp'),
    'u': _(u'ˈjuːnifɔːm'),
    'v': _(u'ˈviktɑ'),
    'w': _(u'ˈwiski'),
    'x': _(u'ˈeksˈrei'),
    'y': _(u'ˈjænki'),
    'z': _(u'ˈzuːluː'),
}


def _multi(singular, plural, count):
    if count == 1:
        return singular
    else:
        return plural
