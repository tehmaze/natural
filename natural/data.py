import datetime
import fcntl
import os
import struct
import sys
import termios
try:
    from io import BytesIO
except ImportError:
    from cStringIO import StringIO as BytesIO
from natural.constant import _, PRINTABLE, SPARKCHAR
from natural.file import filesize


def _termsize():
    '''
    Get the current terminal size, returns a ``(height, width)`` tuple.
    '''

    try:
        print 'plan a'
        return struct.unpack('hh',
            fcntl.ioctl(sys.stdout.fileno(), termios.TIOCGWINSZ, '1234'))
    except:
        print 'plan b'
        return (
            int(os.environ.get('LINES', 25)),
            int(os.environ.get('COLUMNS', 80)),
        )


def hexdump(stream):
    '''
    Display stream contents in hexadecimal and ASCII format. The ``stream``
    specified must either be a file-like object that supports the ``read``
    method to receive bytes, or it can be a string.

    To dump a file::

        >>> hexdump(file(filename))

    Or to dump stdin::

        >>> import sys
        >>> hexdump(sys.stdin)

    :param stream: stream input
    '''

    if isinstance(stream, basestring):
        stream = BytesIO(stream)

    row = 0
    while True:
        data = stream.read(16)
        if not data:
            break

        hextets = data.encode('hex').ljust(32)
        canonical = printable(data)

        print '%08x %s  %s  |%s|' % (row * 16,
            ' '.join(hextets[x:x + 2] for x in xrange(0x00, 0x10, 2)),
            ' '.join(hextets[x:x + 2] for x in xrange(0x10, 0x20, 2)),
            canonical,
        )
        row += 1


def printable(sequence):
    '''
    Return a printable string from the input ``sequence``

    :param sequence: byte or string sequence
    '''
    return ''.join(map(lambda c: c if c in PRINTABLE else '.', sequence))


def sparkline(data):
    '''
    Return a spark line for the given data set.

    :value data: sequence of numeric values
    '''

    min_value = float(min(data))
    max_value = float(max(data))
    steps = (max_value - min_value) / float(len(SPARKCHAR) - 1)
    return u''.join([
        SPARKCHAR[int((float(value) - min_value) / steps)]
        for value in data
    ])


def throughput(sample, window=1, format='decimal'):
    '''
    Return the throughput in (intelli)bytes per second.

    :param sample: number of samples sent
    :param window: default 1, sample window in seconds or
                   :class:`datetime.timedelta` object
    :param format: default 'decimal', see :func:`natural.size.filesize`
    '''

    if isinstance(window, datetime.timedelta):
        window = float(window.days * 86400 + window.seconds)
    elif isinstance(window, basestring):
        window = float(window)

    per_second = sample / float(window)
    return _('%s/s') % (filesize(per_second, format=format),)
