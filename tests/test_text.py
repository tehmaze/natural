# -*- coding: utf-8 -*-
from natural import text


class TestText(object):
    def test_code(self):
        for test, expect in (
            ('hello world',
                u'HO tell  EKK oh  LEE mah  LEE mah  OSS car  WISS key  ' + \
                u'OSS car  ROW me oh  LEE mah  DEL tah'),
            ):

            result = text.code(test)
            assert result == expect, '%r <> %r' % (result, expect)

#    def test_morse(self):
#        for test, expect in (
#            ('hello world',
#                u'.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--'),
#            ):
#
#            result = text.morse(test)
#            assert result == expect, '%r <> %r' % (result, expect)

    def test_spell(self):
        for test, expect in (
            ('abcdefg',
                u'Amsterdam  Baltimore  Casablanca  Danmark  Edison  ' + \
                u'Florida  Gallipoli'),
            ):

            result = text.spell(test)
            assert result == expect, '%r <> %r' % (result, expect)
            
    def test_pronounce(self):
        for test, expect in (
            ('abcdefg',
                u'ælfɑ ˈbrɑːˈvo ˈtʃɑːli ˈdeltɑ  ˈeko ˈfɔkstrɔt ɡʌlf'),
            ):

            result = text.pronounce(test)
            assert result == expect, '%r <> %r' % (result, expect)
