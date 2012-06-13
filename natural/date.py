from natural.constant import _, _multi
import datetime


def ago(value, now=None):
    '''
    Show how long ago a given time value was. You can override the current
    time to compare to by supplying the ``now`` parameter.

    >>> now = 123456789
    >>> ago(now + 10, now)
    'just now'
    '''

    now = now or datetime.datetime.now()
    if isinstance(now, float) or \
        isinstance(now, int) or \
        isinstance(now, long):
        now = datetime.datetime.fromtimestamp(float(now))

    if isinstance(value, float) or \
        isinstance(value, int) or \
        isinstance(value, long):
        delta = now - datetime.datetime.fromtimestamp(long(value))
    elif isinstance(value, basestring):
        # TODO Maybe also accept RFC822 time stamps?
        delta = now - datetime.datetime.fromtimestamp(long(value))
    elif isinstance(value, datetime.datetime):
        delta = now - value
    elif isinstance(value, datetime.date):
        delta = now - value
    else:
        raise ValueError('Not a valid time format')

    if delta.days < 0:
        return _('in the future')

    elif delta.days == 0:
        if delta.seconds < 10:
            return _('just now')
        elif delta.seconds < 60:
            return _multi(
                _('%d second ago'),
                _('%d seconds ago'),
                delta.seconds) % (delta.seconds,)
        elif delta.seconds < 120:
            return _('a minute ago')
        elif delta.seconds < 3600:
            minutes = int(delta.seconds / 60)
            return _multi(
                _('%d minute ago'),
                _('%d minutes ago'),
                minutes) % (minutes,)
        elif delta.seconds < 7200:
            return _('an hour ago')
        elif delta.seconds < 86400:
            hours = int(delta.seconds / 3600)
            return _multi(
                _('%d hour ago'),
                _('%d hours ago'),
                hours) % (hours,)

    elif delta.days == 1:
        return _('yesterday')

    elif delta.days < 7:
        return _multi(
            _('%d day ago'),
            _('%d days ago'),
            delta.days) % (delta.days,)

    elif delta.days < 31:
        weeks = int(delta.days / 7)
        return _multi(
            _('%d week ago'),
            _('%d weeks ago'),
            weeks) % (weeks,)

    elif delta.days < 365:
        months = int(delta.days / 30)
        return _multi(
            _('%d month ago'),
            _('%d months ago'),
            months) % (months,)

    else:
        years = int(delta.days / 365)
        return _multi(
            _('%d year ago'),
            _('%d years ago'),
            years) % (years,)
