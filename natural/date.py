from natural.constant import _, _multi
import datetime


# Wed, 02 Oct 2002 08:00:00 EST
# Wed, 02 Oct 2002 13:00:00 GMT
# Wed, 02 Oct 2002 15:00:00 +0200
RFC2822_DATETIME_FORMAT = '%a, %d %b %Y %T %z'
# Wed, 02 Oct 02 08:00:00 EST
# Wed, 02 Oct 02 13:00:00 GMT
# Wed, 02 Oct 02 15:00:00 +0200
RFC822_DATETIME_FORMAT  = '%a, %d %b %y %T %z'
# 2012-06-13T15:24:17
ISO8601_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
# Wed, 02 Oct 2002
RFC2822_DATE_FORMAT     = '%a, %d %b %Y'
# Wed, 02 Oct 02
RFC2822_DATE_FORMAT     = '%a, %d %b %y'
# 2012-06-13
ISO8601_DATE_FORMAT     = '%Y-%m-%d'


def _to_datetime(t):
    '''
    Internal function that tries whatever to convert ``t`` into a
    :class:`datetime.datetime` object.
    '''

    if isinstance(t, float) or \
        isinstance(t, int) or \
        isinstance(t, long):
        return datetime.datetime.fromtimestamp(float(t))

    elif isinstance(t, basestring):
        for format in (
            RFC2822_DATETIME_FORMAT,
            RFC822_DATETIME_FORMAT,
            ISO8601_DATETIME_FORMAT,
            ):
            try:
                return datetime.datetime.strptime(t, format)
            except ValueError:
                pass

        raise ValueError('Format not supported')

    elif isinstance(t, datetime.datetime):
        return t

    elif isinstance(t, datetime.date):
        return datetime.datetime.combine(t, datetime.time(0, 0))

    else:
        raise TypeError


def _to_date(t):
    '''
    Internal function that tries whatever to convert ``t`` into a
    :class:`datetime.date` object.
    '''

    if isinstance(t, float) or \
        isinstance(t, int) or \
        isinstance(t, long):
        return datetime.date.fromtimestamp(float(t))

    elif isinstance(t, basestring):
        for format in (
            RFC2822_DATE_FORMAT,
            RFC822_DATE_FORMAT,
            ISO8601_DATE_FORMAT,
            ):
            try:
                return datetime.datetime.strptime(t, format).date()
            except ValueError:
                pass

        raise ValueError('Format not supported')

    elif isinstance(t, datetime.datetime):
        return t.date()

    elif isinstance(t, datetime.date):
        return t

    else:
        raise TypeError


def delta(t1, t2):
    '''
    Calculates the estimated delta between two time objects in human-readable
    format. Used internally by the :func:`day` and :func:`duration` functions.

    :param t1: timestamp, :class:`datetime.date` or :class:`datetime.datetime`
               object
    :param t2: timestamp, :class:`datetime.date` or :class:`datetime.datetime`
               object
    '''

    t1 = _to_datetime(t1)
    t2 = _to_datetime(t2)
    diff = t1 - t2

    if diff.days == 0:
        if diff.seconds < 10:
            return _(u'just now')
        elif diff.seconds < 60:
            return _multi(
                _(u'%d second'),
                _(u'%d seconds'),
                diff.seconds) % (diff.seconds,)
        elif diff.seconds < 120:
            return _(u'a minute')
        elif diff.seconds < 3600:
            minutes = int(diff.seconds / 60)
            return _multi(
                _(u'%d minute'),
                _(u'%d minutes'),
                minutes) % (minutes,)
        elif diff.seconds < 7200:
            return _(u'an hour')
        elif diff.seconds < 86400:
            hours = int(diff.seconds / 3600)
            return _multi(
                _(u'%d hour'),
                _(u'%d hours'),
                hours) % (hours,)

    elif diff.days == 1:
        return _(u'yesterday')

    elif diff.days < 7:
        return _multi(
            _(u'%d day'),
            _(u'%d days'),
            diff.days) % (diff.days,)

    elif diff.days < 31:
        weeks = int(diff.days / 7)
        return _multi(
            _(u'%d week'),
            _(u'%d weeks'),
            weeks) % (weeks,)

    elif diff.days < 365:
        months = int(diff.days / 30)
        return _multi(
            _(u'%d month'),
            _(u'%d months'),
            months) % (months,)

    else:
        years = int(diff.days / 365)
        return _multi(
            _(u'%d year'),
            _(u'%d years'),
            years) % (years,)


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
    '''
    t1 = _to_date(t)
    t2 = _to_date(now or datetime.datetime.now())
    diff = max(t1, t2) - min(t1, t2)

    if diff.days == 0:
        return _(u'today')
    elif diff.days == 1:
        if t1 < t2:
            return _(u'yesterday')
        else:
            return _(u'tomorrow')
    elif diff.days == 7:
        if t1 < t2:
            return _(u'last week')
        else:
            return _(u'next week')
    else:
        return t1.strftime(format)


def duration(t, now=None):
    '''
    Time delta compared to ``t``. You can override ``now`` to specify what time
    to compare to.

    :param t: timestamp, :class:`datetime.date` or :class:`datetime.datetime`
              object
    :param now: default ``None``, optionally a :class:`datetime.datetime`
                object
    '''

    t1 = _to_datetime(t)
    t2 = _to_datetime(now or datetime.datetime.now())

    if t1 < t2:
        format = _(u'%s ago')
    else:
        format = _(u'%s from now')

    result = delta(max(t1, t2), min(t1, t2))
    if result == _(u'just now'):
        return result
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
    '''

    if isinstance(t, datetime.timedelta):
        seconds = t.seconds + (t.days * 86400)
    elif isinstance(t, float) or isinstance(t, int) or isinstance(t, long):
        seconds = long(t)
    else:
        return compress(datetime.datetime.now() - _to_datetime(t), sign, pad)

    parts = []
    if sign:
        parts.append(u'-' if d.days < 0 else u'+')

    weeks, seconds   = divmod(seconds, 604800)
    days, seconds    = divmod(seconds, 86400)
    hours, seconds   = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

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
