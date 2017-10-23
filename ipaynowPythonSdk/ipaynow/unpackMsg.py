#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4
try:
    import sys
    reload(sys)
    sys.setdefaultencoding( "utf-8" )
except Exception:
    pass

# WP001-无插件聚合支付
from ipaynow.paramlist import WP001_PostList, WP001_RespList
# MQ001-商户支付订单查询
from ipaynow.paramlist import MQ001_PostList, MQ001_RespList
# N001-商户服务器端支付结果通知
from ipaynow.paramlist import N001_QueryList, N001_RespList
# N002-商户前端支付结果通知
from ipaynow.paramlist import N002_NotifyList

import ipaynow
from ipaynow.error import APIInputError
from ipaynow.md5Faced import md5calc
from ipaynow.utils import trans2unicode

try:
    from urllib import unquote
except ImportError:
    from urllib.parse import unquote

import getopt, sys
def usage():
    print ('''
NAME
    pack send message.
Usage
    python packMsg.py [options]
    ''')


class UnpackMsgRecv:
    __recvStr = ""
    __filterRule = []
    __apiKey = ""
    __unpackDict = {}
    __recvSortedList = []
    __md5Dict = {}
    __tarDictJoinMd5 = {}
    __md5Result = ""
    __tarListJoinMd5 = []
    __fromStrMd5 = ""
    def __init__(self, recvStr = "", filterrule = []):
        unicodestr = trans2unicode(recvStr)
        self.__recvStr = unquote(unicodestr)
        self.__filterRule = filterrule
        self.__apiKey = ipaynow.api_key
    def __recvStr2Dict(self):
        tempDict = {}
        tempList = self.__recvStr.split("&")
        for onpair in tempList:
            pairList = onpair.split("=")
            tempDict[pairList[0]] = pairList[1]
        self.__unpackDict = tempDict
    def __recvFilter(self):
        """from __unpackDict to __md5Dict.
        Use paramlist to filter the input dictionary.
        """
        for singleParam in self.__filterRule:
            filedName = singleParam['name']
            # judeg if the filedName exist in source dictionary.
            if filedName in self.__unpackDict: #exist
                # the filedName is exist in sourcedict.
                # then judge if the length is right.
                srcContent = self.__unpackDict[filedName]
                if ( len(str(srcContent)) > singleParam['len']):
                    errmsg = '''Recv parameter [{}] is too long. Max length is [{}].'''.format(filedName,singleParam['len'])
                    raise APIInputError(errmsg)
                if (len(str(srcContent)) == 0):
                    continue
#                self.__tarDict[filedName] = srcContent
                # if the info needs md5 calc .
                if (singleParam['md5'] == 'Y'):
                    self.__tarDictJoinMd5[filedName] = srcContent
            else : # no exist
                # judge if the parameter is mandatory
                if singleParam['mandatory'] == 'Y': # this parameter is mandatory
                    if filedName == 'mhtSignature':
                        continue
                    errmsg = '''Didn't receive parameter [{}].this parameter indicts [{}].'''.format(filedName,singleParam['desp'])
                    raise APIInputError(errmsg)
                else:
                    continue
    def __sortDict(self, ):
        sortedListJoinmd5 = sorted(self.__tarDictJoinMd5.items(),key = lambda e: e[0],reverse = False)
        self.__tarListJoinMd5 = sortedListJoinmd5
    def __createFromStr(self):
        fromstrmd5 = ""
        for formContentMd5 in self.__tarListJoinMd5:
            if formContentMd5[1] == '' or formContentMd5[1] == None:
                continue
            fromstrmd5 += str(formContentMd5[0]) + "=" + str(formContentMd5[1]) + "&"
        self.__fromStrMd5 = fromstrmd5
    def __calcMd5(self):
        sourceString = self.__fromStrMd5
        securityKeyMd5 = md5calc(self.__apiKey.encode('utf-8'))
        sourceString += securityKeyMd5
       # print("待签名字符串:{}".format(sourceString))
        md5Result = md5calc(sourceString.encode('utf_8'))
        self.__md5Result = md5Result
    def getResultDict(self):
        self.__recvStr2Dict()
        return self.__unpackDict
    def verifyResponse(self):
        if not self.__unpackDict: # assert dictionary is exist.
            self.__recvStr2Dict()
        # start calc the md5 string
        self.__recvFilter()
        self.__sortDict()
        self.__createFromStr()
        self.__calcMd5()
       # print("calc md5 string:")
       #print(self.__md5Result)
       # print("signature:")
       # print(self.__unpackDict["signature"])
        return self.__md5Result == self.__unpackDict["signature"]
    def test(self):
        pass
if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "file="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print( str(err)) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    file=""

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--file"):
            file= a
        else:
            assert False, "unhandled option"
    recvStr = '''mhtCharset=UTF-8&responseCode=A001&payChannelType=12&appId=1409801351286401&mhtOrderStartTime=20151102100843&mhtOrderNo=20151102100843_LAzqDtZklJhwmdBO&signType=MD5&mhtOrderAmt=10&transStatus=A001&mhtOrderTimeOut=120&mhtOrderName=ordername&deviceType=02&mhtOrderType=05&responseMsg=%E6%9F%A5%E8%AF%A2%E4%BA%A4%E6%98%93%E6%88%90%E5%8A%9F&signature=ad86ba36954dbde4b9f9aee97f4132c8&responseTime=20151102100954&mhtCurrencyType=156'''
    try:
        upmv = unpackMsgRecv(recvStr,MQ001_RespList)
        #  resultStr = pms.getResultString()
        recvDict = upmv.getResultDict()
        print(recvDict)
        a = upmv.verifyResponse()
        print(a)
        #upmv.test()
    except APIInputError as e:
        print("api error occured")
        print(e.with_traceback)
    except Exception as e:
        print("other exception")
        print(e.with_traceback)
        
