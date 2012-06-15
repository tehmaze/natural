import datetime
import time
from natural import size


class TestDate(object):
    def test_filesize(self):
        for test, expect in (
            (1,             u'1.00 B'),
            (1024,          u'1.00 kB'),
            (1448576,       u'1.38 MB'),
            ):

            result = size.filesize(test)
            assert result == expect, '%r <> %r' % (result, expect)

    def test_binarysize(self):
        for test, expect in (
            (1,             u'1.00 iB'),
            (1000,          u'1.00 KiB'),
            (1448576,       u'1.45 MiB'),
            ):

            result = size.binarysize(test)
            assert result == expect, '%r <> %r' % (result, expect)
    
    def test_gnusize(self):
        for test, expect in (
            (1,             u'1.0B'),
            (1024,          u'1.0K'),
            (1448576,       u'1.4M'),
            ):

            result = size.gnusize(test)
            assert result == expect, '%r <> %r' % (result, expect)
