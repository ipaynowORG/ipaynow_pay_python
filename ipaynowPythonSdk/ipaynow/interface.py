#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4
from ipaynow.packMsg import PackMsgSend
from ipaynow.paramlist import WP001_PostList, WP001_RespList
from ipaynow.paramlist import MQ001_PostList, MQ001_RespList
from ipaynow.paramlist import N001_QueryList, N001_RespList
from ipaynow.paramlist import N002_NotifyList
from ipaynow.unpackMsg import UnpackMsgRecv
#from ipaynow.utils import trans2unicode
from ipaynowPythonSdk.ipaynow.paramlist import MQ001_PostList


def trade(appKey,payparam = {}):

    pms = PackMsgSend(appKey,payparam,WP001_PostList)
    return pms.getResultString()

def query(queryparam = {}):

    pms = PackMsgSend(queryparam,MQ001_PostList)
    return pms.getResultString()

def notify(frontNotifyParam = 'Y'):
    stringRtn = "{'success':'%s'}" %frontNotifyParam
    return stringRtn

def parseTrade(instr = ""):
    upm = UnpackMsgRecv(instr,WP001_RespList)
    recvDict = upm.getResultDict()
    isVerified = upm.verifyResponse()
    return (recvDict,isVerified)

def parseQuery(instr = ""):
 #   instrunicode = trans2unicode(instr)
    upm = UnpackMsgRecv(instr,MQ001_RespList)
    recvDict = upm.getResultDict()
    isVerified = upm.verifyResponse()
    return (recvDict,isVerified)

def parseNotify(instr = ""):
    upm = UnpackMsgRecv(instr,N001_QueryList)
    recvDict = upm.getResultDict()
    isVerified = upm.verifyResponse()
    return (recvDict,isVerified)

def parseFrontNotify(instr = ""):
    upm = UnpackMsgRecv(instr,N002_NotifyList)
    recvDict = upm.getResultDict()
    isVerified = upm.verifyResponse()
    return (recvDict,isVerified)
