import gettext
import locale
import os
locale.setlocale(locale.LC_ALL, '')

LOCALE_PATH = os.path.join(os.path.dirname(__file__), 'locale')
gettext.bindtextdomain('natural', LOCALE_PATH)
gettext.textdomain('natural')
TRANSLATION = gettext.translation('natural', LOCALE_PATH)
_ = TRANSLATION.gettext

CONVENTION = locale.localeconv()
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
