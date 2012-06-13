``natural.number``
==================

Examples
--------

Using the :py:func:`natural.number.double` function::
    
    >>> from natural.number import double
    >>> double(23.42)
    u'23.42'
    >>> double(1234.56)
    u'1,234.56'

Using the :py:func:`natural.number.number` function::
    
    >>> from natural.number import number
    >>> number(1)
    u'1'
    >>> number('1234567890')
    u'1,234,567,890'

Using the :py:func:`natural.ordinal.ordinal` function::
    
    >>> from natural.ordinal import ordinal
    >>> ordinal(1)
    u'1st'
    >>> ordinal(11)
    u'11th'
    >>> ordinal(113)
    u'113th'
    >>> ordinal(103)
    u'103rd'

Using the :py:func:`natural.number.word` function::

    >>> from natural.number import word
    >>> word(1)
    u'1'
    >>> word(1000)
    u'1 thousand'
    >>> word(1200000000)
    u'1.2 billion'
    >>> word(-42230000000000000000000)
    u'-42.23 sextillion'

API
---

.. automodule:: natural.number
    :members:
    :undoc-members:
    :show-inheritance:

