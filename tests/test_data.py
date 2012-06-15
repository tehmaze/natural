# -*- coding: utf-8 -*-
from natural import data


class TestData(object):
    def test_printable(self):
        for test, expect in (
            ('\x00\x01\x02\x03\x04\x05\x06\x06', '........'),
            ('12345678',                         '12345678'),
            ('testing\n',                        'testing.'),
            ):

            result = data.printable(test)
            assert result == expect, '%r <> %r' % (result, expect)

    def test_hexdump(self):
        for test, expect in (
            ('\x00\x01\x02\x03\x04\x05\x06\x06', '........'),
            ('12345678',                         '12345678'),
            ('testing\n',                        'testing.'),
            ):

            result = data.hexdump(test)
            assert True

    def test_sparkline(self):
        test = [15, 21, 30, 23, 47, 41, 49, 33, 41, 41, 62, 0, 82]
        expect = u'\u2582\u2582\u2583\u2582\u2585\u2584\u2585\u2583\u2584\u2584\u2586\u2581\u2588'
        result = data.sparkline(test)
        assert result == expect, '%r <> %r' % (result, expect)
