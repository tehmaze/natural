from natural import number
from nose.tools import raises


class TestNumber(object):
    def test_ordinal(self):
        for test, expect in (
                (1,     u'1st'),
                (3,     u'3rd'),
                (11,    u'11th'),
                (101,   u'101st'),
                (104,   u'104th'),
                (113,   u'113th'),
                (123,   u'123rd'),
            ):
            result = number.ordinal(test)
            assert result == expect, '%r <> %r' % (result, expect)

    def test_double(self):
        for test, expect in (
                (23.42,     u'23.42'),
                (1234.56,   u'1,234.56'),
            ):
            result = number.double(test)
            assert result == expect, '%r <> %r' % (result, expect)

    def test_number(self):
        for test, expect in (
                (1,             u'1'),
                (1234,          u'1,234'),
                (1234567,       u'1,234,567'),
                ('1234567890',  u'1,234,567,890'),
            ):
            result = number.number(test)
            assert result == expect, '%r <> %r' % (result, expect)

    @raises(TypeError)
    def test_number_none(self):
        number.number(None)

    def test_word(self):
        for test, expect in (
                (1,                         u'1'),
                (1000,                      u'1 thousand'),
                (1000000,                   u'1 million'),
                (1200000000,                u'1.2 billion'),
                (-1200000000,               u'-1.2 billion'),
                (42230000000000000000000,   u'42.23 sextillion'),
            ):
            result = number.word(test)
            assert result == expect, '%r <> %r' % (result, expect)

    @raises(TypeError)
    def test_word_none(self):
        number.word(None)
