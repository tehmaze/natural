from natural.language import _, _multi
import datetime
import math


# Wed, 02 Oct 2002 08:00:00 EST
# Wed, 02 Oct 2002 13:00:00 GMT
# Wed, 02 Oct 2002 15:00:00 +0200
RFC2822_DATETIME_FORMAT = r'%a, %d %b %Y %T %z'
# Wed, 02 Oct 02 08:00:00 EST
# Wed, 02 Oct 02 13:00:00 GMT
# Wed, 02 Oct 02 15:00:00 +0200
RFC822_DATETIME_FORMAT = r'%a, %d %b %y %T %z'
# 2012-06-13T15:24:17
ISO8601_DATETIME_FORMAT = r'%Y-%m-%dT%H:%M:%S'
# Wed, 02 Oct 2002
RFC2822_DATE_FORMAT = r'%a, %d %b %Y'
# Wed, 02 Oct 02
RFC822_DATE_FORMAT = r'%a, %d %b %y'
# 2012-06-13
ISO8601_DATE_FORMAT = r'%Y-%m-%d'
# All date formats
ALL_DATE_FORMATS = (
    RFC2822_DATE_FORMAT,
    RFC822_DATE_FORMAT,
    ISO8601_DATE_FORMAT,
)
ALL_DATETIME_FORMATS = ALL_DATE_FORMATS + (
    RFC822_DATETIME_FORMAT,
    ISO8601_DATETIME_FORMAT,
)

# Precalculated timestamps
TIME_MINUTE = 60
TIME_HOUR = 3600
TIME_DAY = 86400
TIME_WEEK = 604800


def _total_seconds(t):
    '''
    Takes a `datetime.timedelta` object and returns the delta in seconds.

    >>> _total_seconds(datetime.timedelta(23, 42, 123456))
    1987242
    >>> _total_seconds(datetime.timedelta(23, 42, 654321))
    1987243
    '''
    return sum([
        int(t.days * 86400 + t.seconds),
        int(round(t.microseconds / 1000000.0))
    ])


def _to_datetime(t):
    '''
    Internal function that tries whatever to convert ``t`` into a
    :class:`datetime.datetime` object.


    >>> _to_datetime('2013-12-11')
    datetime.datetime(2013, 12, 11, 0, 0)
    >>> _to_datetime('Wed, 11 Dec 2013')
    datetime.datetime(2013, 12, 11, 0, 0)
    >>> _to_datetime('Wed, 11 Dec 13')
    datetime.datetime(2013, 12, 11, 0, 0)
    >>> _to_datetime('2012-06-13T15:24:17')
    datetime.datetime(2012, 6, 13, 15, 24, 17)

    '''

    if isinstance(t, (float, int, long)):
        return datetime.datetime.fromtimestamp(t).replace(microsecond=0)

    elif isinstance(t, basestring):
        for date_format in ALL_DATETIME_FORMATS:
            try:
                d = datetime.datetime.strptime(t, date_format)
                return d.replace(microsecond=0)
            except ValueError:
                pass

        raise ValueError(_('Format "%s" not supported') % t)

    elif isinstance(t, datetime.datetime):
        return t.replace(microsecond=0)

    elif isinstance(t, datetime.date):
        d = datetime.datetime.combine(t, datetime.time(0, 0))
        return d.replace(microsecond=0)

    else:
        raise TypeError


def _to_date(t):
    '''
    Internal function that tries whatever to convert ``t`` into a
    :class:`datetime.date` object.

    >>> _to_date('2013-12-11')
    datetime.date(2013, 12, 11)
    >>> _to_date('Wed, 11 Dec 2013')
    datetime.date(2013, 12, 11)
    >>> _to_date('Wed, 11 Dec 13')
    datetime.date(2013, 12, 11)
    '''

    if isinstance(t, (float, int, long)):
        return datetime.date.fromtimestamp(t)

    elif isinstance(t, basestring):
        for date_format in ALL_DATE_FORMATS:
            try:
                return datetime.datetime.strptime(t, date_format).date()
            except ValueError:
                pass

        raise ValueError('Format not supported')

    elif isinstance(t, datetime.datetime):
        return t.date()

    elif isinstance(t, datetime.date):
        return t

    else:
        raise TypeError


def delta(t1, t2, words=True, justnow=datetime.timedelta(seconds=10)):
    '''
    Calculates the estimated delta between two time objects in human-readable
    format. Used internally by the :func:`day` and :func:`duration` functions.

    :param t1: timestamp, :class:`datetime.date` or :class:`datetime.datetime`
               object
    :param t2: timestamp, :class:`datetime.date` or :class:`datetime.datetime`
               object
    :param words: default ``True``, allow words like "yesterday", "tomorrow"
               and "just now"
    :param justnow: default ``datetime.timedelta(seconds=10)``,
               :class:`datetime.timedelta` object representing tolerance for
               considering a delta as meaning 'just now'

    >>> delta(_to_datetime('2012-06-13T15:24:17'), \
_to_datetime('2013-12-11T12:34:56'))
    (u'77 weeks', -594639.0)
    '''

    t1 = _to_datetime(t1)
    t2 = _to_datetime(t2)
    diff = t1 - t2
    date_diff = t1.date() - t2.date()

    # The datetime module includes milliseconds with float precision. Floats
    # will give unexpected results here, so we round the value here
    total = math.ceil(_total_seconds(diff))
    total_abs = abs(total)

    if total_abs < TIME_DAY:
        if abs(diff) < justnow and words:
            return (
                _(u'just now'),
                0,
            )

        elif total_abs < TIME_MINUTE:
            seconds = total_abs
            return (
                _multi(
                    _(u'%d second'),
                    _(u'%d seconds'),
                    seconds
                ) % (seconds,),
                0,
            )
        elif total_abs < TIME_MINUTE * 2 and words:
            return (
                _(u'a minute'),
                0,
            )

        elif total_abs < TIME_HOUR:
            minutes, seconds = divmod(total_abs, TIME_MINUTE)
            if total < 0:
                seconds *= -1
            return (
                _multi(
                    _(u'%d minute'),
                    _(u'%d minutes'),
                    minutes
                ) % (minutes,),
                seconds,
            )

        elif total_abs < TIME_HOUR * 2 and words:
            return (
                _(u'an hour'),
                0,
            )

        else:
            hours, seconds = divmod(total_abs, TIME_HOUR)
            if total < 0:
                seconds *= -1

            return (
                _multi(
                    _(u'%d hour'),
                    _(u'%d hours'),
                    hours
                ) % (hours,),
                seconds,
            )

    elif date_diff.days == 1 and words:
        return (_(u'tomorrow'), 0)

    elif date_diff.days == -1 and words:
        return (_(u'yesterday'), 0)

    elif total_abs < TIME_WEEK:
        days, seconds = divmod(total_abs, TIME_DAY)
        if total < 0:
            seconds *= -1
        return (
            _multi(
                _(u'%d day'),
                _(u'%d days'),
                days
            ) % (days,),
            seconds,
        )

    elif abs(diff.days) == TIME_WEEK and words:
        if total > 0:
            return (_(u'next week'), diff.seconds)
        else:
            return (_(u'last week'), diff.seconds)

# FIXME
#
# The biggest reliable unit we can supply to the user is a week (for now?),
# because we can not safely determine the amount of days in the covered
# month/year span.

    else:
        weeks, seconds = divmod(total_abs, TIME_WEEK)
        if total < 0:
            seconds *= -1
        return (
            _multi(
                _(u'%d week'),
                _(u'%d weeks'),
                weeks
            ) % (weeks,),
            seconds,
        )


def day(t, now=None, format='%B %d'):
    '''
    Date delta compared to ``t``. You can override ``now`` to specify what date
    to compare to.

    You can override the date format by supplying a ``format`` parameter.

    :param t: timestamp, :class:`datetime.date` or :class:`datetime.datetime`
              object
    :param now: default ``None``, optionally a :class:`datetime.datetime`
                object
    :param format: default ``'%B %d'``

    >>> import time
    >>> day(time.time())
    u'today'
    >>> day(time.time() - 86400)
    u'yesterday'
    >>> day(time.time() - 604800)
    u'last week'
    >>> day(time.time() + 86400)
    u'tomorrow'
    >>> day(time.time() + 604800)
    u'next week'
    '''
    t1 = _to_date(t)
    t2 = _to_date(now or datetime.datetime.now())
    diff = t1 - t2
    secs = _total_seconds(diff)
    days = abs(diff.days)

    if days == 0:
        return _(u'today')
    elif days == 1:
        if secs < 0:
            return _(u'yesterday')
        else:
            return _(u'tomorrow')
    elif days == 7:
        if secs < 0:
            return _(u'last week')
        else:
            return _(u'next week')
    else:
        return t1.strftime(format)


def duration(t, now=None, precision=1, pad=u', ', words=None,
             justnow=datetime.timedelta(seconds=10)):
    '''
    Time delta compared to ``t``. You can override ``now`` to specify what time
    to compare to.

    :param t: timestamp, :class:`datetime.date` or :class:`datetime.datetime`
              object
    :param now: default ``None``, optionally a :class:`datetime.datetime`
                object
    :param precision: default ``1``, number of fragments to return
    :param words: default ``None``, allow words like "yesterday", if set to
                  ``None`` this will be enabled if ``precision`` is set to
                  ``1``
    :param justnow: default ``datetime.timedelta(seconds=10)``,
                    :class:`datetime.timedelta` object passed to :func:`delta`
                    representing tolerance for considering argument ``t`` as
                    meaning 'just now'

    >>> import time
    >>> from datetime import datetime
    >>> duration(time.time() + 1)
    u'just now'
    >>> duration(time.time() + 11)
    u'11 seconds from now'
    >>> duration(time.time() - 1)
    u'just now'
    >>> duration(time.time() - 11)
    u'11 seconds ago'
    >>> duration(time.time() - 3601)
    u'an hour ago'
    >>> duration(time.time() - 7201)
    u'2 hours ago'
    >>> duration(time.time() - 1234567)
    u'2 weeks ago'
    >>> duration(time.time() + 7200, precision=1)
    u'2 hours from now'
    >>> duration(time.time() - 1234567, precision=3)
    u'2 weeks, 6 hours, 56 minutes ago'
    >>> duration(datetime(2014, 9, 8), now=datetime(2014, 9, 9))
    u'yesterday'
    >>> duration(datetime(2014, 9, 7, 23), now=datetime(2014, 9, 9))
    u'1 day ago'
    >>> duration(datetime(2014, 9, 10), now=datetime(2014, 9, 9))
    u'tomorrow'
    >>> duration(datetime(2014, 9, 11, 1), now=datetime(2014, 9, 9, 23))
    u'1 day from now'
    '''

    if words is None:
        words = precision == 1

    t1 = _to_datetime(t)
    t2 = _to_datetime(now or datetime.datetime.now())

    if t1 < t2:
        format = _(u'%s ago')
    else:
        format = _(u'%s from now')

    result, remains = delta(t1, t2, words=words, justnow=justnow)
    if result in (
            _(u'just now'),
            _(u'yesterday'),
            _(u'tomorrow'),
            _(u'last week'),
            _(u'next week'),
    ):
        return result

    elif precision > 1 and remains:
        t3 = t2 - datetime.timedelta(seconds=remains)
        return pad.join([
            result,
            duration(t2, t3, precision - 1, pad, words=False),
        ])

    else:
        return format % (result,)


def compress(t, sign=False, pad=u''):
    '''
    Convert the input to compressed format, works with a
    :class:`datetime.timedelta` object or a number that represents the number
    of seconds you want to compress.  If you supply a timestamp or a
    :class:`datetime.datetime` object, it will give the delta relative to the
    current time.

    You can enable showing a sign in front of the compressed format with the
    ``sign`` parameter, the default is not to show signs.

    Optionally, you can chose to pad the output. If you wish your values to be
    separated by spaces, set ``pad`` to ``' '``.

    :param t: seconds or :class:`datetime.timedelta` object
    :param sign: default ``False``
    :param pad: default ``u''``

    >>> compress(1)
    u'1s'
    >>> compress(12)
    u'12s'
    >>> compress(123)
    u'2m3s'
    >>> compress(1234)
    u'20m34s'
    >>> compress(12345)
    u'3h25m45s'
    >>> compress(123456)
    u'1d10h17m36s'

    '''

    if isinstance(t, datetime.timedelta):
        seconds = t.seconds + (t.days * 86400)
    elif isinstance(t, (float, int, long)):
        return compress(datetime.timedelta(seconds=t), sign, pad)
    else:
        return compress(datetime.datetime.now() - _to_datetime(t), sign, pad)

    parts = []
    if sign:
        parts.append(u'-' if t.days < 0 else u'+')

    weeks, seconds = divmod(seconds, TIME_WEEK)
    days, seconds = divmod(seconds, TIME_DAY)
    hours, seconds = divmod(seconds, TIME_HOUR)
    minutes, seconds = divmod(seconds, TIME_MINUTE)

    if weeks:
        parts.append(_(u'%dw') % (weeks,))
    if days:
        parts.append(_(u'%dd') % (days,))
    if hours:
        parts.append(_(u'%dh') % (hours,))
    if minutes:
        parts.append(_(u'%dm') % (minutes,))
    if seconds:
        parts.append(_(u'%ds') % (seconds,))

    return pad.join(parts)
