import re
from collections import OrderedDict
from natural.constant import _
from natural.number import _format


# Period table of the elements. All full names are in standard new-latin form,
# because it's simply easier to translate.
# 
# Atomic weights (c) Commission on Isotopic Abundances and Atomic Weights
# http://www.ciaaw.org/
# Atomic weights (c) Queen Mary University London
# http://www.chem.qmul.ac.uk/iupac/AtWt/

ELEMENTS = OrderedDict(
    ( # Abbr    (Full name           Atomic weight)
        (None,  (None,               None)),
        ('H',   (_('hydrogen'),      1.008)),
        ('He',  (_('helium'),        4.002602)),
        ('Li',  (_('lithium'),       6.94)),
        ('Be',  (_('beryllium'),     9.012182)),
        ('B',   (_('boron'),         10.81)),
        ('C',   (_('carbon'),        12.011)),
        ('N',   (_('nitrogen'),      14.007)),
        ('O',   (_('oxygen'),        15.999)),
        ('F',   (_('fluorine'),      18.9984032)),
        ('Ne',  (_('neon'),          20.1797)),
        ('Na',  (_('natrium'),       22.98976928)),
        ('Mg',  (_('magnesium'),     24.3050)),
        ('Al',  (_('aluminium'),     26.9815386)),
        ('Si',  (_('silicium'),      28.085)),
        ('P',   (_('phosphorus'),    30.973762)),
        ('S',   (_('sulphur'),       32.06)),
        ('Cl',  (_('chlorum'),       35.45)),
        ('Ar',  (_('argon'),         39.948)),
        ('K',   (_('kalium'),        39.0983)),
        ('Ca',  (_('calcium'),       40.078)),
        ('Sc',  (_('scandium'),      44.955912)),
        ('Ti',  (_('titanium'),      47.867)),
        ('V',   (_('vanadium'),      50.9415)),
        ('Cr',  (_('chromium'),      51.9961)),
        ('Mn',  (_('manganum'),      54.938045)),
        ('Fe',  (_('ferrum'),        55.845)),
        ('Co',  (_('cobaltum'),      58.933195)),
        ('Ni',  (_('niccolum'),      58.6934)),
        ('Cu',  (_('cuprum'),        63.546)),
        ('Zn',  (_('zincum'),        65.38)),
        ('Ga',  (_('gallium'),       69.723)),
        ('Ge',  (_('germanium'),     72.63)),
        ('As',  (_('arsenicum'),     74.92160)),
        ('Se',  (_('selenium'),      78.96)),
        ('Br',  (_('bromum'),        79.904)),
        ('Kr',  (_('krypton'),       83.798)),
        ('Rb',  (_('rubidium'),      85.4678)),
        ('Sr',  (_('strontium'),     87.62)),
        ('Y',   (_('yttrium'),       88.90585)),
        ('Zr',  (_('zirconium'),     91.224)),
        ('Nb',  (_('niobium'),       92.90638)),
        ('Mo',  (_('molybdenum'),    95.96)),
        ('Tc',  (_('technetium'),    98)),
        ('Ru',  (_('ruthenium'),     101.07)),
        ('Rh',  (_('rhodium'),       102.90550)),
        ('Pd',  (_('palladium'),     106.42)),
        ('Ag',  (_('argentum'),      107.8682)),
        ('Cd',  (_('cadmium'),       112.411)),
        ('In',  (_('indium'),        114.818)),
        ('Sn',  (_('stannum'),       118.710)),
        ('Sb',  (_('stibium'),       121.760)),
        ('Te',  (_('tellurium'),     127.60)),
        ('I',   (_('iodum'),         126.90447)),
        ('Xe',  (_('xenon'),         131.293)),
        ('Cs',  (_('caesium'),       132.9054519)),
        ('Ba',  (_('barium'),        137.327)),
        ('La',  (_('lanthanum'),     138.90547)),
        ('Ce',  (_('cerium'),        140.116)),
        ('Pr',  (_('praseodymium'),  140.90765)),
        ('Nd',  (_('neodymium'),     144.242)),
        ('Pm',  (_('promethium'),    145)),
        ('Sm',  (_('samarium'),      150.36)),
        ('Eu',  (_('europium'),      151.964)),
        ('Gd',  (_('gadolinium'),    157.25)),
        ('Tb',  (_('terbium'),       158.92535)),
        ('Dy',  (_('dysprosium'),    162.500)),
        ('Ho',  (_('holmium'),       164.93032)),
        ('Er',  (_('erbium'),        167.259)),
        ('Tm',  (_('thulium'),       168.93421)),
        ('Yb',  (_('ytterbium'),     173.054)),
        ('Lu',  (_('lutetium'),      174.9668)),
        ('Hf',  (_('hafnium'),       178.49)),
        ('Ta',  (_('tantalum'),      180.94788)),
        ('W',   (_('wolframium'),    183.84)),
        ('Re',  (_('rhenium'),       186.207)),
        ('Os',  (_('osmium'),        190.23)),
        ('Ir',  (_('iridium'),       192.217)),
        ('Pt',  (_('platinum'),      195.084)),
        ('Au',  (_('aurum'),         196.966569)),
        ('Hg',  (_('hydrargyrum'),   200.59)),
        ('Tl',  (_('thallium'),      204.38)),
        ('Pb',  (_('plumbum'),       207.2)),
        ('Bi',  (_('bismuthum'),     208.98040)),
        ('Po',  (_('polonium'),      209)),
        ('At',  (_('astatum'),       210)),
        ('Rn',  (_('radon'),         222)),
        ('Fr',  (_('francium'),      223)),
        ('Ra',  (_('radium'),        226)),
        ('Ac',  (_('actinium'),      227)),
        ('Th',  (_('thorium'),       232.03806)),
        ('Pa',  (_('protactinium'),  231.03588)),
        ('U',   (_('uranium'),       238.02891)),
        ('Np',  (_('neptunium'),     237)),
        ('Pu',  (_('plutonium'),     244)),
        ('Am',  (_('americium'),     243)),
        ('Cm',  (_('curium'),        247)),
        ('Bk',  (_('berkelium'),     247)),
        ('Cf',  (_('californium'),   251)),
        ('Es',  (_('einsteinium'),   252)),
        ('Fm',  (_('fermium'),       257)),
        ('Md',  (_('mendelevium'),   258)),
        ('No',  (_('nobelium'),      259)),
        ('Lr',  (_('lawrencium'),    262)),
        ('Rf',  (_('rutherfordium'), 265)),
        ('Db',  (_('dubnium'),       268)),
        ('Sg',  (_('seaborgium'),    271)),
        ('Bh',  (_('bohrium'),       270)),
        ('Hs',  (_('hassium'),       277)),
        ('Mt',  (_('meitnerium'),    276)),
        ('Ds',  (_('darmstadtium'),  281)),
        ('Rg',  (_('roentgenium'),   280)),
        ('Cn',  (_('copernicium'),   285)),
        ('Uut', (_('ununtrium'),     284)),
        ('Fl',  (_('flerovium'),     289)),
        ('Uup', (_('ununpentium'),   288)),
        ('Lv',  (_('livermorium'),   293)),
        ('Uus', (_('ununseptium'),   294)),
        ('Uuo', (_('ununoctium'),    294)),
    ))


_RE_ELEMENTS = r'\b(%s)\b' % ('|'.join(a for a in ELEMENTS if ELEMENTS[a][0]),)
RE_FORMULA   = re.compile(r'(%s(\d*))' % _RE_ELEMENTS)


def full_name(abbreviation):
    '''
    Get the full name of an element by its abbreviated form.

    Example:

        >>> full_name('O')
        u'oxygen'

    '''
    return ELEMENTS[abbreviation.title()][0]

_RE_SEQUENCE = re.compile(r'(([A-Z][a-z]*)(\d*)|<EOS>)')

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
    total = sum([element[1] * count for element, count in parts])

    # http://en.wikipedia.org/wiki/Atomic_mass_unit
    return _('%s u') % (_format(total, digits),)
