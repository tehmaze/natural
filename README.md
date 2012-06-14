About
=====

Convert data to their natural (human-readable) format.

Example Usage
=============

Basic usage:

```python

    >>> from natural.file import accessed
    >>> print accessed(__file__)
    just now
```

We speak your language (with [your support](https://github.com/tehmaze/natural/wiki/translate)):

```python

    >>> import locale
    >>> locale.setlocale(locale.LC_MESSAGES, 'nl_NL')
    >>> print accessed(__file__)
    zojuist
```

Bugs/Features
=============

You can issue a ticket in GitHub: https://github.com/tehmaze/natural/issues
