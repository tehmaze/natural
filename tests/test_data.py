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
