import gettext
import locale
import os
locale.setlocale(locale.LC_ALL, '')

LOCALE_PATH = os.path.join(os.path.dirname(__file__), 'locale')
gettext.bindtextdomain('natural', LOCALE_PATH)
gettext.textdomain('natural')
TRANSLATION = gettext.translation('natural', LOCALE_PATH)
_ = TRANSLATION.ugettext

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


def _multi(singular, plural, count):
    if count == 1:
        return singular
    else:
        return plural
