#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4

import getopt, sys

class IpaynowError(Exception):
    def __init__(self, message=None):
        super(IpaynowError, self).__init__(message)
        self._message = message
    def __unicode__(self):
        return self._message

    if sys.version_info > (3, 0):
        __str__ = lambda self: self.__unicode__()
    else:
        __str__ = lambda self: unicode(self).encode('utf-8')

class APIError(IpaynowError):
    pass

class APIInputError(IpaynowError):
    pass


