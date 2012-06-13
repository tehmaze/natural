import datetime
import time
from natural import date


class TestDate(object):
    def test_ago(self):

        now = time.time()
        for test, expect in (
            (now - 1,       u'just now'),
            (now - 11,      u'11 seconds ago'),
            (now - 3601,    u'an hour ago'),
            (now - 7201,    u'2 hours ago'),
            ):

            result = date.ago(test)
            assert result == expect, '%r <> %r' % (result, expect)
