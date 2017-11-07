import urllib

from pip._vendor import requests

from ipaynowPythonSdk.ipaynow import interface


import urllib

from pip._vendor import requests

from ipaynowPythonSdk.ipaynow import interface


'''
撤销查询接口
appId:商户应用id
appKey:商户应用秘钥
mhtRefundNo:商户退款单号
'''
def backOrderQuery(appId,appKey,mhtRefundNo):
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
    resp = requests.post("https://pay.ipaynow.cn/refund/refundOrder",refundstr)
    return urllib.parse.unquote(resp.text)

'''
撤销接口
appId:商户应用id
appKey:商户应用秘钥
orderno:原订单号
mhtRefundNo:商户退款单号
reason:撤销原因
'''
def backOrder(appId,appKey,orderno,mhtRefundNo,reason):
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
    resp = requests.post("https://pay.ipaynow.cn/refund/refundOrder",refundstr)
    return urllib.parse.unquote(resp.text)


'''
退款查询
appId:商户应用id
appKey:商户应用秘钥
mhtRefundNo:商户退款单号
'''
def refundQuery(appId,appKey,mhtRefundNo):
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
    resp = requests.post("https://pay.ipaynow.cn/refund/refundQuery",refundstr)
    return urllib.parse.unquote(resp.text)

'''
退款接口
appId:商户应用id
appKey:商户应用秘钥
orderno:原订单号
mhtRefundNo:商户退款单号
amount:商户退款金额
reason:退款原因
'''
def refund(appId,appKey,orderno,mhtRefundNo,amount,reason):
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
    resp = requests.post("https://pay.ipaynow.cn/refund/refundOrder",refundstr)
    return urllib.parse.unquote(resp.text)