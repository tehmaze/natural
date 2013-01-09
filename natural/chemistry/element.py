from natural.constant import _


__all__ = ['ELEMENTS', 'GROUPS', 'SERIES']

# Collected elements
ELEMENTS = dict()

# Groups in the periodic system
GROUPS = {
    1:  ('IA',      'Alkali metals'),
    2:  ('IIA',     'Alkaline earths'),
    3:  ('IIIB',    ''),
    4:  ('IVB',     ''),
    5:  ('VB',      ''),
    6:  ('VIB',     ''),
    7:  ('VIIB',    ''),
    8:  ('VIIIB',   ''),
    9:  ('VIIIB',   ''),
    10: ('VIIIB',   ''),
    11: ('IB',      'Coinage metals'),
    12: ('IIB',     ''),
    13: ('IIIA',    'Boron group'),
    14: ('IVA',     'Carbon group'),
    15: ('VA',      'Pnictogens'),
    16: ('VIA',     'Chalcogens'),
    17: ('VIIA',    'Halogens'),
    18: ('VIIIA',   'Noble gases'),
}

# Series in the periodic system
SERIES = {
    1:  'Nonmetals',
    2:  'Noble gases',
    3:  'Alkali metals',
    4:  'Alkaline earth metals',
    5:  'Metalloids',
    6:  'Halogens',
    7:  'Poor metals',
    8:  'Transition metals',
    9:  'Lanthanides',
    10: 'Actinides'
}

# ...
OXYANIONS = (
    ('HClO4',   _('perchloric acid')),
    ('HClO3',   _('chloric acid')),
    ('HClO2',   _('chlrous acid')),
    ('HClO',    _('hypochlorous acid')),
)


class Element(object):
    def __init__(self, index, symbol, name, root, **kwargs):
        self.index = index
        self.symbol = symbol
        self.name = name
        self.root = root
        self.__dict__.update(kwargs)
        ELEMENTS[self.symbol] = self

    def __unicode__(self):
        return self.name
    
    @property
    def charge(self):
        if self.group in (1, 2):
            return self.group
        
        elif self.group in (3, 4, 5, 6, 7):
            return -(8 - self.group)
        
        else:
            

# Period table of the elements. All full names are in standard new-latin form,
# because it's simply easier to translate.
#
# Atomic weights (c) Commission on Isotopic Abundances and Atomic Weights
# http://www.ciaaw.org/
# Atomic weights (c) Queen Mary University London
# http://www.chem.qmul.ac.uk/iupac/AtWt/

Element(1, 'H',
        name=_('hydrogen'),
        root=_('hydr'),
        mass=1.008000)
Element(2, 'He',
        name=_('helium'),
        root=_('hel'),
        mass=4.002602)
Element(3, 'Li',
        name=_('lithium'),
        root=_('lith'),
        mass=6.940000)
Element(4, 'Be',
        name=_('beryllium'),
        root=_('beryl'),
        mass=9.012182)
Element(5, 'B',
        name=_('boron'),
        root=_('bor'),
        mass=10.810000)
Element(6, 'C',
        name=_('carbon'),
        root=_('carb'),
        mass=12.011000)
Element(7, 'N',
        name=_('nitrogen'),
        root=_('nitr'),
        mass=14.007000)
Element(8, 'O',
        name=_('oxygen'),
        root=_('oxy'),
        mass=15.999000)
Element(9, 'F',
        name=_('fluorine'),
        root=_('fluor'),
        mass=18.998403)
Element(10, 'Ne',
        name=_('neon'),
        root=_('neon'),
        mass=20.179700)
Element(11, 'Na',
        name=_('natrium'),
        root=_('natr'),
        mass=22.989769)
Element(12, 'Mg',
        name=_('magnesium'),
        root=_('magnes'),
        mass=24.305000)
Element(13, 'Al',
        name=_('aluminium'),
        root=_('aluminium'),
        mass=26.981539)
Element(14, 'Si',
        name=_('silicium'),
        root=_('silicium'),
        mass=28.085000)
Element(15, 'P',
        name=_('phosphorus'),
        root=_('phosphorus'),
        mass=30.973762)
Element(16, 'S',
        name=_('sulphur'),
        root=_('sulph'),
        mass=32.060000)
Element(17, 'Cl',
        name=_('chlorum'),
        root=_('chlorum'),
        mass=35.450000)
Element(18, 'Ar',
        name=_('argon'),
        root=_('argon'),
        mass=39.948000)
Element(19, 'K',
        name=_('kalium'),
        root=_('kalium'),
        mass=39.098300)
Element(20, 'Ca',
        name=_('calcium'),
        root=_('calcium'),
        mass=40.078000)
Element(21, 'Sc',
        name=_('scandium'),
        root=_('scandium'),
        mass=44.955912)
Element(22, 'Ti',
        name=_('titanium'),
        root=_('titanium'),
        mass=47.867000)
Element(23, 'V',
        name=_('vanadium'),
        root=_('vanadium'),
        mass=50.941500)
Element(24, 'Cr',
        name=_('chromium'),
        root=_('chromium'),
        mass=51.996100)
Element(25, 'Mn',
        name=_('manganum'),
        root=_('manganum'),
        mass=54.938045)
Element(26, 'Fe',
        name=_('ferrum'),
        root=_('ferrum'),
        mass=55.845000)
Element(27, 'Co',
        name=_('cobaltum'),
        root=_('cobaltum'),
        mass=58.933195)
Element(28, 'Ni',
        name=_('niccolum'),
        root=_('niccolum'),
        mass=58.693400)
Element(29, 'Cu',
        name=_('cuprum'),
        root=_('cuprum'),
        mass=63.546000)
Element(30, 'Zn',
        name=_('zincum'),
        root=_('zincum'),
        mass=65.380000)
Element(31, 'Ga',
        name=_('gallium'),
        root=_('gallium'),
        mass=69.723000)
Element(32, 'Ge',
        name=_('germanium'),
        root=_('germanium'),
        mass=72.630000)
Element(33, 'As',
        name=_('arsenicum'),
        root=_('arsenicum'),
        mass=74.921600)
Element(34, 'Se',
        name=_('selenium'),
        root=_('selenium'),
        mass=78.960000)
Element(35, 'Br',
        name=_('bromum'),
        root=_('bromum'),
        mass=79.904000)
Element(36, 'Kr',
        name=_('krypton'),
        root=_('krypton'),
        mass=83.798000)
Element(37, 'Rb',
        name=_('rubidium'),
        root=_('rubidium'),
        mass=85.467800)
Element(38, 'Sr',
        name=_('strontium'),
        root=_('strontium'),
        mass=87.620000)
Element(39, 'Y',
        name=_('yttrium'),
        root=_('yttrium'),
        mass=88.905850)
Element(40, 'Zr',
        name=_('zirconium'),
        root=_('zirconium'),
        mass=91.224000)
Element(41, 'Nb',
        name=_('niobium'),
        root=_('niobium'),
        mass=92.906380)
Element(42, 'Mo',
        name=_('molybdenum'),
        root=_('molybdenum'),
        mass=95.960000)
Element(43, 'Tc',
        name=_('technetium'),
        root=_('technetium'),
        mass=98.000000)
Element(44, 'Ru',
        name=_('ruthenium'),
        root=_('ruthenium'),
        mass=101.070000)
Element(45, 'Rh',
        name=_('rhodium'),
        root=_('rhodium'),
        mass=102.905500)
Element(46, 'Pd',
        name=_('palladium'),
        root=_('palladium'),
        mass=106.420000)
Element(47, 'Ag',
        name=_('argentum'),
        root=_('argentum'),
        mass=107.868200)
Element(48, 'Cd',
        name=_('cadmium'),
        root=_('cadmium'),
        mass=112.411000)
Element(49, 'In',
        name=_('indium'),
        root=_('indium'),
        mass=114.818000)
Element(50, 'Sn',
        name=_('stannum'),
        root=_('stannum'),
        mass=118.710000)
Element(51, 'Sb',
        name=_('stibium'),
        root=_('stibium'),
        mass=121.760000)
Element(52, 'Te',
        name=_('tellurium'),
        root=_('tellurium'),
        mass=127.600000)
Element(53, 'I',
        name=_('iodum'),
        root=_('iodum'),
        mass=126.904470)
Element(54, 'Xe',
        name=_('xenon'),
        root=_('xenon'),
        mass=131.293000)
Element(55, 'Cs',
        name=_('caesium'),
        root=_('caesium'),
        mass=132.905452)
Element(56, 'Ba',
        name=_('barium'),
        root=_('barium'),
        mass=137.327000)
Element(57, 'La',
        name=_('lanthanum'),
        root=_('lanthanum'),
        mass=138.905470)
Element(58, 'Ce',
        name=_('cerium'),
        root=_('cerium'),
        mass=140.116000)
Element(59, 'Pr',
        name=_('praseodymium'),
        root=_('praseodymium'),
        mass=140.907650)
Element(60, 'Nd',
        name=_('neodymium'),
        root=_('neodymium'),
        mass=144.242000)
Element(61, 'Pm',
        name=_('promethium'),
        root=_('promethium'),
        mass=145.000000)
Element(62, 'Sm',
        name=_('samarium'),
        root=_('samarium'),
        mass=150.360000)
Element(63, 'Eu',
        name=_('europium'),
        root=_('europium'),
        mass=151.964000)
Element(64, 'Gd',
        name=_('gadolinium'),
        root=_('gadolinium'),
        mass=157.250000)
Element(65, 'Tb',
        name=_('terbium'),
        root=_('terbium'),
        mass=158.925350)
Element(66, 'Dy',
        name=_('dysprosium'),
        root=_('dysprosium'),
        mass=162.500000)
Element(67, 'Ho',
        name=_('holmium'),
        root=_('holmium'),
        mass=164.930320)
Element(68, 'Er',
        name=_('erbium'),
        root=_('erbium'),
        mass=167.259000)
Element(69, 'Tm',
        name=_('thulium'),
        root=_('thulium'),
        mass=168.934210)
Element(70, 'Yb',
        name=_('ytterbium'),
        root=_('ytterbium'),
        mass=173.054000)
Element(71, 'Lu',
        name=_('lutetium'),
        root=_('lutetium'),
        mass=174.966800)
Element(72, 'Hf',
        name=_('hafnium'),
        root=_('hafnium'),
        mass=178.490000)
Element(73, 'Ta',
        name=_('tantalum'),
        root=_('tantalum'),
        mass=180.947880)
Element(74, 'W',
        name=_('wolframium'),
        root=_('wolframium'),
        mass=183.840000)
Element(75, 'Re',
        name=_('rhenium'),
        root=_('rhenium'),
        mass=186.207000)
Element(76, 'Os',
        name=_('osmium'),
        root=_('osmium'),
        mass=190.230000)
Element(77, 'Ir',
        name=_('iridium'),
        root=_('iridium'),
        mass=192.217000)
Element(78, 'Pt',
        name=_('platinum'),
        root=_('platinum'),
        mass=195.084000)
Element(79, 'Au',
        name=_('aurum'),
        root=_('aurum'),
        mass=196.966569)
Element(80, 'Hg',
        name=_('hydrargyrum'),
        root=_('hydrargyrum'),
        mass=200.590000)
Element(81, 'Tl',
        name=_('thallium'),
        root=_('thallium'),
        mass=204.380000)
Element(82, 'Pb',
        name=_('plumbum'),
        root=_('plumbum'),
        mass=207.200000)
Element(83, 'Bi',
        name=_('bismuthum'),
        root=_('bismuthum'),
        mass=208.980400)
Element(84, 'Po',
        name=_('polonium'),
        root=_('polonium'),
        mass=209.000000)
Element(85, 'At',
        name=_('astatum'),
        root=_('astatum'),
        mass=210.000000)
Element(86, 'Rn',
        name=_('radon'),
        root=_('radon'),
        mass=222.000000)
Element(87, 'Fr',
        name=_('francium'),
        root=_('francium'),
        mass=223.000000)
Element(88, 'Ra',
        name=_('radium'),
        root=_('radium'),
        mass=226.000000)
Element(89, 'Ac',
        name=_('actinium'),
        root=_('actinium'),
        mass=227.000000)
Element(90, 'Th',
        name=_('thorium'),
        root=_('thorium'),
        mass=232.038060)
Element(91, 'Pa',
        name=_('protactinium'),
        root=_('protactinium'),
        mass=231.035880)
Element(92, 'U',
        name=_('uranium'),
        root=_('uranium'),
        mass=238.028910)
Element(93, 'Np',
        name=_('neptunium'),
        root=_('neptunium'),
        mass=237.000000)
Element(94, 'Pu',
        name=_('plutonium'),
        root=_('plutonium'),
        mass=244.000000)
Element(95, 'Am',
        name=_('americium'),
        root=_('americium'),
        mass=243.000000)
Element(96, 'Cm',
        name=_('curium'),
        root=_('curium'),
        mass=247.000000)
Element(97, 'Bk',
        name=_('berkelium'),
        root=_('berkelium'),
        mass=247.000000)
Element(98, 'Cf',
        name=_('californium'),
        root=_('californium'),
        mass=251.000000)
Element(99, 'Es',
        name=_('einsteinium'),
        root=_('einsteinium'),
        mass=252.000000)
Element(100, 'Fm',
        name=_('fermium'),
        root=_('fermium'),
        mass=257.000000)
Element(101, 'Md',
        name=_('mendelevium'),
        root=_('mendelevium'),
        mass=258.000000)
Element(102, 'No',
        name=_('nobelium'),
        root=_('nobelium'),
        mass=259.000000)
Element(103, 'Lr',
        name=_('lawrencium'),
        root=_('lawrencium'),
        mass=262.000000)
Element(104, 'Rf',
        name=_('rutherfordium'),
        root=_('rutherfordium'),
        mass=265.000000)
Element(105, 'Db',
        name=_('dubnium'),
        root=_('dubnium'),
        mass=268.000000)
Element(106, 'Sg',
        name=_('seaborgium'),
        root=_('seaborgium'),
        mass=271.000000)
Element(107, 'Bh',
        name=_('bohrium'),
        root=_('bohrium'),
        mass=270.000000)
Element(108, 'Hs',
        name=_('hassium'),
        root=_('hassium'),
        mass=277.000000)
Element(109, 'Mt',
        name=_('meitnerium'),
        root=_('meitnerium'),
        mass=276.000000)
Element(110, 'Ds',
        name=_('darmstadtium'),
        root=_('darmstadtium'),
        mass=281.000000)
Element(111, 'Rg',
        name=_('roentgenium'),
        root=_('roentgenium'),
        mass=280.000000)
Element(112, 'Cn',
        name=_('copernicium'),
        root=_('copernicium'),
        mass=285.000000)
Element(113, 'Uut',
        name=_('ununtrium'),
        root=_('ununtrium'),
        mass=284.000000)
Element(114, 'Fl',
        name=_('flerovium'),
        root=_('flerovium'),
        mass=289.000000)
Element(115, 'Uup',
        name=_('ununpentium'),
        root=_('ununpentium'),
        mass=288.000000)
Element(116, 'Lv',
        name=_('livermorium'),
        root=_('livermorium'),
        mass=293.000000)
Element(117, 'Uus',
        name=_('ununseptium'),
        root=_('ununseptium'),
        mass=294.000000)
Element(118, 'Uuo',
        name=_('ununoctium'),
        root=_('ununoctium'),
        mass=294.000000)
