#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4

from ipaynowPythonSdk.ipaynow.paramlist import WP001_PostList
from ipaynowPythonSdk.ipaynow.error import APIInputError
from ipaynowPythonSdk.ipaynow.md5Faced import md5calc

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode
import getopt, sys


def usage():
    print('''
NAME
    pack send message.
Usage
    python packMsg.py [options]
    ''')


class PackMsgSend:
    __srcDict = {}
    __tarDict = {}
    __tarDictJoinMd5 = {}
    __tarListJoinMd5 = []
    __filterRule = []
    __fromStrMd5 = ""
    # __md5Key = ""
    __appKey = ""
    __md5Result = ""

    def __init__(self, appKey, sourcedict={}, filterrule=[]):
        self.__appKey = appKey
        self.__srcDict = sourcedict
        self.__filterRule = filterrule

    def __inputFilter(self):
        '''
        from __srcDict to __tarDict
        use paramlist to filter the input dictionary.
        '''
        for singleParam in self.__filterRule:
            filedName = singleParam['name']
            # judeg if the filedName exist in source dictionary.
            if filedName in self.__srcDict:  # exist
                # the filedName is exist in sourcedict.
                # then judge if the length is right.
                srcContent = self.__srcDict[filedName]
                if (len(str(srcContent)) > singleParam['len']):
                    errmsg = '''Your input parameter [{}] is too long. Max length is [{}].'''.format(filedName,
                                                                                                     singleParam['len'])
                    raise APIInputError(errmsg)
                if (len(str(srcContent)) == 0):
                    continue
                self.__tarDict[filedName] = srcContent
                # if the info needs md5 calc .
                if (singleParam['md5'] == 'Y'):
                    self.__tarDictJoinMd5[filedName] = srcContent
            else:  # no exist
                # judge if the parameter is mandatory
                if singleParam['mandatory'] == 'Y':  # this parameter is mandatory
                    if filedName == 'mhtSignature':
                        continue
                    errmsg = '''You should input parameter [{}].this parameter indicts [{}].'''.format(filedName,
                                                                                                       singleParam[
                                                                                                           'desp'])
                    raise APIInputError(errmsg)
                else:
                    continue
        self.__sortDict()

    def __sortDict(self):
        sortedListJoinmd5 = sorted(self.__tarDictJoinMd5.items(), key=lambda e: e[0], reverse=False)
        self.__tarListJoinMd5 = sortedListJoinmd5

    def __createFromStr(self):
        fromstrmd5 = ""
        for formContentMd5 in self.__tarListJoinMd5:
            if formContentMd5[1] == '' or formContentMd5[1] == None:
                continue
            fromstrmd5 += str(formContentMd5[0]) + "=" + str(formContentMd5[1]) + "&"
        self.__fromStrMd5 = fromstrmd5

    def __calcMd5(self):
        # remove string that don't join md5 calc
        sourceString = self.__fromStrMd5
        securityKeyMd5 = md5calc(self.__appKey.encode('utf-8'))
        sourceString += securityKeyMd5
        # print("待签名字符串:{}".format(sourceString))
        md5Result = md5calc(sourceString.encode('utf_8'))
        self.__tarDict['mhtSignature'] = md5Result
        self.__md5Result = md5Result

    def getResultString(self):
        self.__inputFilter()
        self.__createFromStr()
        self.__calcMd5()
        resultStr = urlencode(self.__tarDict)
        return resultStr

    def test(self):
        # print("__fromstr :",self.__fromStr)
        # print("__fromstrmd5 :",self.__fromStrMd5)
        # print("__tarDict :",self.__tarDict)
        # print("__tarDictJoinMd5 :",self.__tarDictJoinMd5)
        pass


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "file="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    file = ""

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--file"):
            file = a
        else:
            assert False, "unhandled option"
    paypara = {
        'funcode': 'WP001',
        'version': '1.0.0',
        'appId': '150753082825470',
        'mhtOrderType': '01',
        'mhtCurrencyType': '156',
        'mhtOrderDetail': 'ipaynowPythonSDKTestOrder',
        'mhtOrderTimeOut': 3600,
        'notifyUrl': 'http://posp.ipaynow.cn:10808/cpgatetest/notify',
        'mhtCharset': 'UTF-8',
        'deviceType': '05',
        'payChannelType': '13',
        'channelAuthCode': '134954669523328956',
        'mhtReserved': '',
        'consumerId': '',
        'mhtSignType': 'MD5'
    }
    import time

    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    paypara['mhtOrderStartTime'] = '20171027101225'
    try:
        pms = PackMsgSend("8jTST7ywIBY0QQ3RlcxWEl08Xj9gaYyQ", paypara, WP001_PostList)
        resultStr = pms.getResultString()
        print(resultStr)
    except APIInputError as e:
        print(e)

    print("============")
    # print(quote_plus(resultStr,safe='=&'))
