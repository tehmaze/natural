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
    Show how long a given time value was. You can override the current
    time to compare to by supplying the ``now`` parameter.
    '''

    t1 = _to_datetime(t1)
    t2 = _to_datetime(t2)
    diff = t1 - t2

    if diff.days == 0:
        if diff.seconds < 10:
            return _('just now')
        elif diff.seconds < 60:
            return _multi(
                _('%d second'),
                _('%d seconds'),
                diff.seconds) % (diff.seconds,)
        elif diff.seconds < 120:
            return _('a minute')
        elif diff.seconds < 3600:
            minutes = int(diff.seconds / 60)
            return _multi(
                _('%d minute'),
                _('%d minutes'),
                minutes) % (minutes,)
        elif diff.seconds < 7200:
            return _('an hour')
        elif diff.seconds < 86400:
            hours = int(diff.seconds / 3600)
            return _multi(
                _('%d hour'),
                _('%d hours'),
                hours) % (hours,)

    elif diff.days == 1:
        return _('yesterday')

    elif diff.days < 7:
        return _multi(
            _('%d day'),
            _('%d days'),
            diff.days) % (diff.days,)

    elif diff.days < 31:
        weeks = int(diff.days / 7)
        return _multi(
            _('%d week'),
            _('%d weeks'),
            weeks) % (weeks,)

    elif diff.days < 365:
        months = int(diff.days / 30)
        return _multi(
            _('%d month'),
            _('%d months'),
            months) % (months,)

    else:
        years = int(diff.days / 365)
        return _multi(
            _('%d year'),
            _('%d years'),
            years) % (years,)


def timedelta(t, now=None):
    t1 = _to_datetime(t)
    t2 = _to_datetime(now or datetime.datetime.now())

    if t1 < t2:
        suffix = _('ago')
    else:
        suffix = _('from now')
    
    result = delta(max(t1, t2), min(t1, t2))
    if result == _('just now'):
        return result
    else:
        return u' '.join([result, suffix])


def datedelta(t, now=None, format='%B %d'):
    t1 = _to_date(t)
    t2 = _to_date(now or datetime.datetime.now())
    diff = max(t1, t2) - min(t1, t2)

    if diff.days == 0:
        return _('today')
    elif diff.days == 1:
        if t1 < t2:
            return _('yesterday')
        else:
            return _('tomorrow')
    elif diff.days == 7:
        if t1 < t2:
            return _('last week')
        else:
            return _('next week')
    else:
        return t1.strftime(format)