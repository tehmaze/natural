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

CONVENTION = locale.localeconv()
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
FILESIZE_SUFFIX = dict(
    decimal=('B', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'),
    binary=('iB', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'),
    gnu='BKMGTPEZY',
)
PRINTABLE = map(lambda c: chr(c), xrange(0x20, 0x7f))


def _multi(singular, plural, count):
    if count == 1:
        return singular
    else:
        return plural
