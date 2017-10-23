#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4
from ipaynow.version import VERSION
from ipaynow.interface import (
    trade,
    query,
    notify,
#    front_notify,
    parseTrade,
    parseQuery,
    parseNotify,
    parseFrontNotify
    )

from ipaynow.error import (
    APIError,
    APIInputError
)

from ipaynow.utils import trans2unicode

sdk_version = VERSION
api_key = "vtnkfo3TchHUHshxw2lehzQUK0Lh03Nz"

def setApiKey(key=""):
    '''set api key , you also can set this key directly.'''
    api_key = key


__all__ = ['trade','query','notify','front_notify','parseTrade','parseQuery','parseNotify','parseFrontNotify','APIError','APIInputError','trans2unicode']
