``natural.file``
================

Examples
--------

Using the :py:func:`natural.file.accessed` function::

    >>> from natural.file import accessed
    >>> print accessed(__file__)
    just now

Using the :py:func:`natural.file.created` function::

    >>> from natural.file import created
    >>> print created('/etc/fstab')
    2 months ago

Using the :py:func:`natural.file.modified` function::

    >>> from natural.file import modified
    >>> print modified('/etc/issue')
    1 month ago

Using the :py:func:`natural.file.size` function::

    >>> from natural.file import size
    >>> print size('/boot/vmlinuz')
    3.1 MB


API
---

.. automodule:: natural.file
    :members:
    :undoc-members:
    :show-inheritance:

