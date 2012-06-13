import datetime
import time
from natural import date


class TestDate(object):
    def test_day(self):
        now = time.time()
        for test, expect in (
            (now,           u'today'),
            (now - 86400,   u'yesterday'),
            (now - 604800,  u'last week'),
            (now + 86400,   u'tomorrow'),
            (now + 604800,  u'next week'),
            ):

            result = date.day(test)
            assert result == expect, '%r <> %r' % (result, expect)

    def test_duration(self):
        now = time.time()
        for test, expect in (
            (now + 1,       u'just now'),
            (now + 11,      u'10 seconds from now'),
            (now - 1,       u'just now'),
            (now - 11,      u'11 seconds ago'),
            (now - 3601,    u'an hour ago'),
            (now - 7201,    u'2 hours ago'),
            ):

            result = date.duration(test)
            assert result == expect, '%r <> %r' % (result, expect)
