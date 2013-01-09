import re
from natural.constant import _
from natural.number import _format
from natural.chemistry.element import ELEMENTS


# Used in the sequence decoder, returns groups of potential element
# abbreviations (but require manual checking)
_RE_SEQUENCE = re.compile(r'(([A-Z][a-z]*)(\d*)|<EOS>)')


def name(symbol):
    '''
    Get the full name of an element by its abbreviated form.

    Example:

        >>> name('O')
        u'oxygen'

    '''
    return ELEMENTS[symbol.title()].name


def name_sequence(sequence):
    # http://limestone.k12.il.us/teachers/rhebron/Chem_HO/C04_Naming_Writing.html
    parts = decode_sequence(sequence)
    groups = set([element.group for element, count in parts])
    
    # Binary compounds
    if len(parts) == 2:
        # Type I Binary Compounds
        if all(group in (1, 2) for group in groups):
            return u'%s %dide' % (parts[0].name, parts[0].root)
    
        # Type II Binary Compounds
        else: 
            return 

def decode_sequence(sequence):
    input = sequence + '<EOS>'
    where = 0
    parts = []
    while input:
        match = _RE_SEQUENCE.match(input, where)
        if match is None:
            raise ValueError('Unexpected input')

        where = match.end()
        group = match.groups()
        if group[0] == '<EOS>':
            break

        else:
            try:
                element = ELEMENTS[group[1]]
            except KeyError:
                raise TypeError('Unknown element "%s"' % (group[1],))

            parts.append((element, int(group[2] or 1)))

    return parts


def atomic_weight(sequence, digits=None):
    '''
    Get the atomic weight for the given chemical sequence.

    Example:

        >>> atomic_weight('C5H11BrO')
        u'167.50 u'

    '''

    parts = decode_sequence(sequence)
    total = sum([element.mass * count for element, count in parts])

    # http://en.wikipedia.org/wiki/Atomic_mass_unit
    return _('%s u') % (_format(total, digits),)

print name('O')
print atomic_weight('C5H11BrO')
