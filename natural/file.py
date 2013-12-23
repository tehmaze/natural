from natural.date import duration
from natural.size import filesize
import os
import stat


def accessed(filename):
    '''
    Retrieve how long ago a file has been accessed.

    :param filename: name of the file

    >>> print accessed(__file__)        # doctest: +SKIP
    just now
    '''
    if isinstance(filename, file):
        filename = filename.name

    return duration(os.stat(filename)[stat.ST_ATIME])


def created(filename):
    '''
    Retrieve how long ago a file has been created.

    :param filename: name of the file

    >>> print created('/')             # doctest: +SKIP
    8 weeks ago
    '''
    if isinstance(filename, file):
        filename = filename.name

    return duration(os.stat(filename)[stat.ST_CTIME])


def modified(filename):
    '''
    Retrieve how long ago a file has been modified.

    :param filename: name of the file

    >>> print modified('/')             # doctest: +SKIP
    3 days ago
    '''
    if isinstance(filename, file):
        filename = filename.name

    return duration(os.stat(filename)[stat.ST_MTIME])


def size(filename, format='decimal'):
    '''
    Retrieve the size of a file.

    :param filename: name of the file

    >>> size('/etc/mime.types')         # doctest: +SKIP
    23.70 kB

    '''
    if isinstance(filename, file):
        filename = filename.name

    return filesize(os.stat(filename)[stat.ST_SIZE], format)
