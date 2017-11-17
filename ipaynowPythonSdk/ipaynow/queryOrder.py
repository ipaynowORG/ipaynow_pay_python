import random
import string
import urllib
from datetime import time

from pip._vendor import requests

from ipaynowPythonSdk.ipaynow import interface
from ipaynowPythonSdk.ipaynow.interface import proTradeUrl, testTradeUrl

'''
 主扫支付订单查询 
 appId:商户应用id
 appKey:商户应用秘钥
 orderno:订单号 
 isTest 是否测试 True 测试环境 False 生产环境
'''
def query08(appId,appKey,orderno,isTest=True):
    return queryOrder(appId,appKey,"08",orderno,isTest)

'''
 被扫支付订单查询
 appId:商户应用id
 appKey:商户应用秘钥
 orderno:订单号 
 isTest 是否测试 True 测试环境 False 生产环境
'''
def query05(appId,appKey,orderno,isTest=True):
    return queryOrder(appId,appKey,"05",orderno,isTest)


'''
 网页支付订单查询
 appId:商户应用id
 appKey:商户应用秘钥
 orderno:订单号
 isTest 是否测试 True 测试环境 False 生产环境
'''
def query04(appId,appKey,orderno,isTest=True):
    return queryOrder(appId,appKey,"04",orderno,isTest)

'''
 公众号支付订单查询
 appId:商户应用id
 appKey:商户应用秘钥
 orderno:订单号
 isTest 是否测试 True 测试环境 False 生产环境
'''
def query0600(appId,appKey,orderno,isTest=True):
    return queryOrder(appId,appKey,"0600",orderno,isTest)


'''
 H5支付订单查询
 appId:商户应用id
 appKey:商户应用秘钥
 orderno:订单号
 isTest 是否测试 True 测试环境 False 生产环境
'''
def query0601(appId,appKey,orderno,isTest=True):
    return queryOrder(appId,appKey,"0601",orderno,isTest)

'''
 小程序支付订单查询
 appId:商户应用id
 appKey:商户应用秘钥
 orderno:订单号
 isTest 是否测试 True 测试环境 False 生产环境
'''
def query14(appId,appKey,orderno,isTest=True):
    return queryOrder(appId,appKey,"14",orderno,isTest)


def queryOrder(appId,appKey,deviceType, orderno,isTest):
    paypara = {
        'funcode':'MQ002',
        'version': '1.0.0',
        'appId':appId,
        'mhtCharset': 'UTF-8',
        'deviceType': deviceType,
        'mhtSignType':'MD5',
        'mhtOrderNo':orderno

    }
    try:
        tradestr = interface.query(appKey,paypara)
    except interface.APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    if isTest:
        url = testTradeUrl
    else:
        url = proTradeUrl
    resp = requests.post(url,tradestr)
    return urllib.parse.unquote(resp.text)