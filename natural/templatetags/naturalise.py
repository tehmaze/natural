from django.template import Library
from natural import data, date, number, text, size, file

register = Library()


# natural.data

@register.filter
def printable(value):
    '''Wrapper for :func:`natural.data.printable`'''
    return data.printable(value)


@register.filter
def sparkline(value):
    '''Wrapper for :func:`natural.data.sparkline`'''
    return data.sparkline(value)


@register.filter
def throughput(value, window=1, format='decimal'):
    '''Wrapper for :func:`natural.data.throughput`'''
    return data.throughput(value, window, format)


# natural.date

@register.filter
def compress(value, sign=False, pad=u''):
    '''Wrapper for :func:`natural.date.compress`'''
    return date.compress(value, sign, pad)


@register.filter
def day(value, now=None, format='%B %d'):
    '''Wrapper for :func:`natural.date.day`'''
    return date.day(value, now, format)


@register.filter
def delta(value1, value2):
    '''Wrapper for :func:`natural.date.delta`'''
    return date.delta(value1, value2)


@register.filter
def duration(value, now=None):
    '''Wrapper for :func:`natural.date.duration`'''
    return date.duration(value, now)


# natural.file

@register.filter
def accessed(filename):
    '''Wrapper for :func:`natural.file.accessed`'''
    return file.accessed(filename)


@register.filter
def created(filename):
    '''Wrapper for :func:`natural.file.created`'''
    return file.created(filename)


@register.filter
def modified(filename):
    '''Wrapper for :func:`natural.file.modified`'''
    return file.modified(filename)


@register.filter
def filesize(filename, format='decimal'):
    '''Wrapper for :func:`natural.file.filesize`'''
    return file.size(filename, format)


# natural.number

@register.filter
def double(value, digits=2):
    '''Wrapper for :func:`natural.number.double`'''
    return number.double(value, digits)


@register.filter
def number(value):
    '''Wrapper for :func:`natural.number.number`'''
    return number.number(value)


@register.filter
def ordinal(value):
    '''Wrapper for :func:`natural.number.ordinal`'''
    return number.ordinal(value)


@register.filter
def percentage(value, digits=2):
    '''Wrapper for :func:`natural.number.percentage`'''
    return number.percentage(value, digits)


@register.filter
def word(value, digits=2):
    '''Wrapper for :func:`natural.number.word`'''
    return number.word(value, digits)


# natural.size

@register.filter
def binarysize(value):
    '''Wrapper for :func:`natural.size.binarysize`'''
    return size.binarysize(value)


@register.filter
def decimalsize(value):
    '''Wrapper for :func:`natural.size.decimalsize`'''
    return size.decimalsize(value)


@register.filter
def gnusize(value, digits=1):
    '''Wrapper for :func:`natural.size.gnusize`'''
    return size.gnusize(value, digits)


# natural.text

@register.filter
def code(sentence, pad=u'  ', format='army'):
    '''Wrapper for :func:`natural.text.code`'''
    return text.code(sentence, pad, format)


@register.filter
def morse(sentence, pad=' / '):
    '''Wrapper for :func:`natural.text.morse`'''
    return text.morse(sentence, pad)


@register.filter
def nato(sentence, pad=u' ', format='telephony'):
    '''Wrapper for :func:`natural.text.nato`'''
    return text.nato(sentence, pad, format)


@register.filter
def pronounce(sentence, pad=u' '):
    '''Wrapper for :func:`natural.text.pronounce`'''
    return text.pronounce(sentence, pad)


@register.filter
def spell(sentence, pad=u'  '):
    '''Wrapper for :func:`natural.text.spell`'''
    return text.spell(sentence, pad)
