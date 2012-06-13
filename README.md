About
=====

Convert data to their natural (human-readable) format.

Example Usage
=============

Basic usage:

```python

    >>> import datetime
    >>> from natural.date import duration
    >>> print duration(datetime.datetime.now())
    'just now'
```

We speak your language (with [your support](https://github.com/tehmaze/natural/wiki/translate)):

```python

    >>> import locale
    >>> locale.setlocale(locale.LC_MESSAGES, 'nl_NL')
    >>> print duration(datetime.datetime.now())
    'zojuist'
```

Bugs/Features
=============

You can issue a ticket in GitHub: https://github.com/tehmaze/natural/issues
