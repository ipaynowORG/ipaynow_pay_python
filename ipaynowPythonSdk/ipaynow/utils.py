# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4

import os
import io
import sys

__all__ = ['StringIO', 'parse_qsl', 'trans2unicode']



try:
    # When cStringIO is available
    import cStringIO as StringIO
except ImportError:
    from io import StringIO

try:
    from urlparse import parse_qsl
except ImportError:
    # Python < 2.6
    from cgi import parse_qsl



def trans2unicode(value):
    '''via this function ,every string will trans to unicode string'''
    if sys.version_info >= (3,0,0):
        # for Python 3
        if isinstance(value, bytes):
            return value.decode('utf_8')  # or  s = str(s)[2:-1]
        else:
            return value
    else:
        # for Python 2
        if isinstance(value, unicode):
            return str(value)
        else:
            return unicode(value)
