# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4

from ipaynowPythonSdk.ipaynow import utils

__all__ = ['md5calc']

try:
    import hashlib
except ImportError:
    hashlib = None

if not hashlib:
    raise ImportError(
        "ipaynow sdk can't import hashlib.please check if it "
    )


def md5calc(md5source):
    try:
        m = hashlib.md5()
        m.update(md5source)
        return m.hexdigest()
    except Exception as e:
        print(e.args)
        return ""

if __name__ == "__main__":
    strout = "MD5 test string :"
    strtest = ""
    strout += strtest
    strmd5 = md5calc(strtest.encode('utf-8'))
    strout += "\nMD5 result string :" + strmd5
    print(strout)
