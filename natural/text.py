# -*- coding: utf-8 -*-
from natural.constant import NATO_ALPHABET, NATO_ALPHABET_PHONETIC
from natural.constant import SPELL_ALPHABET, CODE_PRONOUNCIATION
from natural.constant import CODE_ALPHABET_ARMY, CODE_ALPHABET_FAA
from natural.constant import CODE_ALPHABET_ICAO, CODE_ALPHABET_MORSE
from natural.constant import CODE_ALPHABET_WORD


NATO_ALPHABET_KEYS = NATO_ALPHABET.keys()
NATO_ALPHABET_KEYS.sort()


class Spelling(object):
    def __call__(self, sentence, pad=u' '):
        parts = []
        for letter in sentence.lower():
            letter = self.transform(letter)
            if letter is not None:
                parts.append(letter)
        return pad.join(parts)

    def transform(self, letter):
        return None


class Alphabet(Spelling):
    def __init__(self, mapping):
        self.mapping = mapping

    @staticmethod
    def from_pair(self, keys, values):
        return Alphabet(dict(zip(keys, values)))

    def transform(self, letter):
        return self.mapping.get(letter)


ALPHABET = dict(
    code=dict(
        army=Alphabet(CODE_ALPHABET_ARMY[1]),
        faa=Alphabet(CODE_ALPHABET_FAA[1]),
        icao=Alphabet(CODE_ALPHABET_ICAO[1]),
        itu=Alphabet(CODE_ALPHABET_ICAO[1]),
        morse=Alphabet(CODE_ALPHABET_MORSE[1]),
        word=Alphabet(CODE_ALPHABET_WORD[1]),
    ),
    nato=dict(
        telephony=Alphabet(NATO_ALPHABET),
        phonetic=Alphabet(NATO_ALPHABET_PHONETIC),
    ),
    spell=Alphabet(SPELL_ALPHABET),
    pronounce=Alphabet(CODE_PRONOUNCIATION),
)
CODE_PADDING = dict(
    army=CODE_ALPHABET_ARMY[0],
    faa=CODE_ALPHABET_FAA[0],
    icao=CODE_ALPHABET_ICAO[0],
    itu=CODE_ALPHABET_ICAO[0],
    morse=CODE_ALPHABET_MORSE[0],
    word=CODE_ALPHABET_WORD[0],
)


def code(sentence, pad=u'  ', format='army'):
    '''
    Transform a sentence using the code spelling alphabet, multiple
    international code alphabets are supported.

    ====== ====================================================================
    format description
    ====== ====================================================================
    army   US (international) army code alphabet
    faa    Federal Aviation Administration code alphabet, as described in "ICAO
           Phonetics in the FAA ATC Manual, §2-4-16"
    icao   International Civil Aviation Organization, as described in "Annex 10
           to the Convention on International Civil Aviation, Volume II (Fifth
           edition, 1995), Chapter 5, 38–40"
    itu    International Telecommunication Union Roman alphabet, as described
           in "ITU Phonetic Alphabet and Figure Code"
    morse  International morse code, as described in "International Morse code
           Recommendation ITU-R M.1677-1", http://itu.int/
    word   International Civil Aviation Organization, as described in "Annex 10
           to the Convention on International Civil Aviation, Volume II (Fifth
           edition, 1995), Chapter 5, 38–40"
    ====== ====================================================================

    :param sentence: input sentence
    :param pad: default ``None`` (reside to per-alphabet defaults)
    :param format: default ``army``
    '''
    try:
        return ALPHABET['code'][format](sentence, pad or CODE_PADDING[format])
    except KeyError:
        raise TypeError('Unsupported code alphabet "%s"' % (format,))


def morse(sentence, pad=CODE_PADDING['morse']):
    '''
    Wrapper for :func:`code`.
    '''
    return code(sentence, pad, 'morse')


def nato(sentence, pad=u' ', format='telephony'):
    '''
    Transform a sentence using the NATO spelling alphabet.

    :param sentence: input sentence
    :param pad: default ``u' '``
    :param format: default ``telephony``, options ``telephony`` or ``phonetic``
    '''
    try:
        return ALPHABET['nato'][format](sentence, pad)
    except KeyError:
        raise TypeError('Unsupported NATO alphabet "%s"' % (format,))


def spell(sentence, pad=u'  '):
    '''
    Transform a sentence using the localised spelling alphabet.

    :param sentence: input sentence
    :param pad: default ``u'  '``
    '''
    return ALPHABET['spell'](sentence, pad)


def pronounce(sentence, pad=u' '):
    '''
    Transform a sentence using the pronounciations of the international code
    spelling alphabet. This function is subject to change its behaviour to
    support internationalised pronounciations of letters.

    :param sentence: input sentence
    :param pad: default ``u'  '``
    '''
    return ALPHABET['pronounce'](sentence, pad)
