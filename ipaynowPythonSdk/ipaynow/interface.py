#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4
from ipaynowPythonSdk.ipaynow.packMsg import PackMsgSend
from ipaynowPythonSdk.ipaynow.paramlist import WP001_PostList, WP001_RespList
from ipaynowPythonSdk.ipaynow.paramlist import MQ001_PostList, MQ001_RespList
from ipaynowPythonSdk.ipaynow.paramlist import N001_QueryList, N001_RespList
from ipaynowPythonSdk.ipaynow.paramlist import N002_NotifyList
from ipaynowPythonSdk.ipaynow.unpackMsg import UnpackMsgRecv
from ipaynowPythonSdk.ipaynow.paramlist import MQ001_PostList, R001_PostList, Q001_PostList, R002_PostList, \
    Q002_PostList


#下单及查询
proTradeUrl = "https://pay.ipaynow.cn";
testTradeUrl = "https://dby.ipaynow.cn/api/payment";

#退款撤销
proRefundUrl = "https://pay.ipaynow.cn/refund/refundOrder";
testRefundUrl = "https://dby.ipaynow.cn/refund_access/refundOrder";

#退款查询
proRefundQueryUrl = "https://pay.ipaynow.cn/refund/refundQuery";
testRefundQueryUrl = "https://dby.ipaynow.cn/refund_access/refundQuery";


def trade(appKey,payparam = {}):

    pms = PackMsgSend(appKey,payparam,WP001_PostList)
    return pms.getResultString()

def query(appKey,queryparam = {}):

    pms = PackMsgSend(appKey,queryparam,MQ001_PostList)
    return pms.getResultString()

def refund(appKey,queryparam = {}):
    pms = PackMsgSend(appKey,queryparam,R001_PostList)
    return pms.getResultString()

def refundQuery(appKey,queryparam = {}):
    pms = PackMsgSend(appKey,queryparam,Q001_PostList)
    return pms.getResultString()

def backOrder(appKey,queryparam = {}):
    pms = PackMsgSend(appKey,queryparam,R002_PostList)
    return pms.getResultString()

def backOrderQuery(appKey,queryparam = {}):
    pms = PackMsgSend(appKey,queryparam,Q002_PostList)
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
