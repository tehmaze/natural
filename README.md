About
=====

Convert data to their natural (natural-readable) format.

Example Usage
=============

Basic usage:

```python

    >>> import datetime
    >>> from natural.date import timedelta
    >>> print timedelta(datetime.datetime.now())
    'just now'
```

We speak your language (with [your support](https://github.com/tehmaze/natural/wiki/translate)):

```python

    >>> import locale
    >>> locale.setlocale(locale.LC_MESSAGES, 'nl_NL')
    >>> print timedelta(datetime.datetime.now())
    'zojuist'
```

Bugs/Features
=============

You can issue a ticket in GitHub: https://github.com/tehmaze/natural/issues
