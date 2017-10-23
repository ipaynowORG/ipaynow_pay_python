#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4
import urllib

import ipaynow as ips
try:
    import urllib.request as requestImport
except ImportError:
    import urllib2 as requestImport

def testQueryInterface(orderno = ''):
    paypara = {}
    paypara = {
        'funcode':'MQ002',
        'appId':'150753082825470',
        'deviceType': '05',
        'mhtCharset': 'UTF-8',
        'mhtSignType':'MD5'
    }
    paypara['mhtOrderNo'] = orderno
    try:
        tradestr = ips.query(paypara)
        return tradestr
    except ips.APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)


from pip._vendor import requests

resp = requests.post("https://pay.ipaynow.cn",testQueryInterface(orderno='201710231426'))
print(urllib.parse.unquote(resp.text))
