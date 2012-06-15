from django.template import Library
from natural import data, date, number, text, size

register = Library()


# natural.data

@register.filter
def printable(value):
    return data.printable(value)


@register.filter
def sparkline(value):
    return data.sparkline(value)


@register.filter
def throughput(value, window=1, format='decimal'):
    return data.throughput(value, window, format)


# natural.date

@register.filter
def compress(value, sign=False, pad=u''):
    return date.compress(value, sign, pad)


@register.filter
def day(value, now=None, format='%B %d'):
    return date.day(value, now, format)


@register.filter
def delta(value1, value2):
    return date.delta(value1, value2)


@register.filter
def duration(value, now=None):
    return date.duration(value, now)


# natural.file

@register.filter
def accessed(filename):
    return file.accessed(filename)


@register.filter
def created(filename):
    return file.created(filename)


@register.filter
def modified(filename):
    return file.modified(filename)


@register.filter
def filesize(filename, format='decimal'):
    return file.size(filename, format)


# natural.number

@register.filter
def double(value, digits=2):
    return number.double(value, digits)


@register.filter
def number(value):
    return number.number(value)


@register.filter
def ordinal(value):
    return number.ordinal(value)


@register.filter
def percentage(value, digits=2):
    return number.percentage(value, digits)


@register.filter
def word(value, digits=2):
    return number.word(value, digits)


# natural.size

@register.filter
def binarysize(value):
    return size.binarysize(value)


@register.filter
def decimalsize(value):
    return size.decimalsize(value)


@register.filter
def gnusize(value, digits=1):
    return size.gnusize(value, digits)


# natural.text

@register.filter
def code(sentence, pad=u'  ', format='army'):
    return text.code(sentence, pad, format)


@register.filter
def morse(sentence, pad=' / '):
    return text.morse(sentence, pad)


@register.filter
def nato(sentence, pad=u' ', format='telephony'):
    return text.nato(sentence, pad, format)


@register.filter
def pronounce(sentence, pad=u' '):
    return text.pronounce(sentence, pad)


@register.filter
def spell(sentence, pad=u'  '):
    return text.spell(sentence, pad)
