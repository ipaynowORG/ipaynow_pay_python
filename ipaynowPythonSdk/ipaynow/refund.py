import urllib

from pip._vendor import requests

from ipaynowPythonSdk.ipaynow import interface


import urllib

from pip._vendor import requests

from ipaynowPythonSdk.ipaynow import interface
from ipaynowPythonSdk.ipaynow.interface import testRefundUrl, proRefundUrl, testRefundQueryUrl, proRefundQueryUrl

'''
撤销查询接口
appId:商户应用id
appKey:商户应用秘钥
mhtRefundNo:商户退款单号
isTest 是否测试 True 测试环境 False 生产环境
'''
def backOrderQuery(appId,appKey,mhtRefundNo,isTest=True):
    paypara = {
        'funcode':'Q002',
        'appId':appId,
        'mhtCharset': 'UTF-8',
        'signType':'MD5',
        'mhtRefundNo':mhtRefundNo
    }
    try:
        refundstr = interface.backOrderQuery(appKey,paypara)
    except interface.APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    if isTest:
        url = testRefundUrl
    else:
        url = proRefundUrl
    resp = requests.post(url,refundstr)
    return urllib.parse.unquote(resp.text)

'''
撤销接口
appId:商户应用id
appKey:商户应用秘钥
orderno:原订单号
mhtRefundNo:商户退款单号
reason:撤销原因
isTest 是否测试 True 测试环境 False 生产环境
'''
def backOrder(appId,appKey,orderno,mhtRefundNo,reason,isTest=True):
    paypara = {
        'funcode':'R002',
        'appId':appId,
        'mhtCharset': 'UTF-8',
        'reason': reason,
        'signType':'MD5',
        'mhtOrderNo':orderno,
        'mhtRefundNo':mhtRefundNo
    }
    try:
        refundstr = interface.backOrder(appKey,paypara)
    except interface.APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    if isTest:
        url = testRefundUrl
    else:
        url = proRefundUrl
    print(refundstr)
    resp = requests.post(url,refundstr)
    return urllib.parse.unquote(resp.text)


'''
退款查询
appId:商户应用id
appKey:商户应用秘钥
mhtRefundNo:商户退款单号
isTest 是否测试 True 测试环境 False 生产环境
'''
def refundQuery(appId,appKey,mhtRefundNo,isTest=True):
    paypara = {
        'funcode':'Q001',
        'appId':appId,
        'mhtCharset': 'UTF-8',
        'signType':'MD5',
        'mhtRefundNo':mhtRefundNo
    }
    try:
        refundstr = interface.refundQuery(appKey,paypara)
    except interface.APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    if isTest:
        url = testRefundQueryUrl
    else:
        url = proRefundQueryUrl
    resp = requests.post(url,refundstr)
    return urllib.parse.unquote(resp.text)


'''
退款接口
appId:商户应用id
appKey:商户应用秘钥
orderno:原订单号
mhtRefundNo:商户退款单号
amount:商户退款金额
reason:退款原因
isTest 是否测试 True 测试环境 False 生产环境
'''
def refund(appId,appKey,orderno,mhtRefundNo,amount,reason,isTest = True):
    paypara = {
        'funcode':'R001',
        'appId':appId,
        'mhtCharset': 'UTF-8',
        'amount': amount,
        'reason': reason,
        'signType':'MD5',
        'mhtOrderNo':orderno,
        'mhtRefundNo':mhtRefundNo
    }
    try:
        refundstr = interface.refund(appKey,paypara)
    except interface.APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    if isTest:
        url = testRefundUrl
    else:
        url = proRefundUrl
    resp = requests.post(url,refundstr)
    return urllib.parse.unquote(resp.text)