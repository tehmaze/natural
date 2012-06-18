import datetime
import time
from natural import date


class TestDate(object):
    def test_compress(self):
        for test, expect in (
            (1,             u'1s'),
            (12,            u'12s'),
            (123,           u'2m3s'),
            (1234,          u'20m34s'),
            (12345,         u'3h25m45s'),
            (123456,        u'1d10h17m36s'),
            ):

            result = date.compress(test)
            assert result == expect, '%r <> %r' % (result, expect)

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
            (now - 123456,  u'yesterday'),
            (now - 1234567, u'2 weeks ago'),
            ):

            result = date.duration(test)
            assert result == expect, '%r <> %r' % (result, expect)

        for test, expect in (
            (now + 11,      u'10 seconds from now'),
            (now - 1,       u'1 second ago'),
            (now - 11,      u'11 seconds ago'),
            (now - 3601,    u'1 hour, 1 second ago'),
            (now - 7201,    u'2 hours, 1 second ago'),
            (now - 123456,  u'1 day, 10 hours, 17 minutes ago'),
            (now - 1234567, u'2 weeks, 6 hours, 56 minutes ago'),
            ):

            result = date.duration(test, precision=3)
            assert result == expect, '%r <> %r' % (result, expect)
