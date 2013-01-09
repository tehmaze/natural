``natural.text``
================

Examples
--------

Using the :py:func:`natural.text.code` function::

    >>> from natural.text import code
    >>> print code('hello world!')
    HO tell  EKK oh  LEE mah  LEE mah  OSS car  WISS key  OSS car  ROW me oh  LEE mah  DEL tah

Using the :py:func:`natural.text.morse` function::

    >>> from natural.text import morse
    >>> print morse('hello world!')
    .... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--

Using the :py:func:`natural.text.spell` function::

    >>> from natural.text import spell
    >>> print spell('abcdefg')
    Amsterdam  Baltimore  Casablanca  Danmark  Edison  Florida  Gallipoli

Using the :py:func:`natural.text.pronounce` function::

    >>> from natural.text import pronounce
    >>> print pronounce('abcdefg')
    ælfɑ ˈbrɑːˈvo ˈtʃɑːli ˈdeltɑ  ˈeko ˈfɔkstrɔt ɡʌlf

API
---

.. automodule:: natural.text
    :members:
    :undoc-members:
    :show-inheritance:

