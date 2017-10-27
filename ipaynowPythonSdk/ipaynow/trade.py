import random
import string
import time
import urllib

from ipaynowPythonSdk.ipaynow import interface
from pip._vendor import requests



'''
    公众号支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    payChannelType：支付渠道（12支付宝，13微信）
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType ; 0-公众号0模式
'''
def trade0600(appId,appKey,ordername,mhtOrderDetail,payChannelType,outputType,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,payChannelType,"0600",amt = amt, orderno = orderno,outputType=outputType)

'''
    主扫支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    payChannelType：支付渠道（12支付宝，13微信）
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType ; 0 返回二维码串 1 返回支付链接
'''
def trade08(appId,appKey,ordername,mhtOrderDetail,payChannelType,outputType,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,payChannelType,"08",amt = amt, orderno = orderno,outputType=outputType)

'''
    被扫支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    payChannelType：支付渠道（12支付宝，13微信）
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    channelAuthCode ; 支付授权码
'''
def trade05(appId,appKey,ordername,mhtOrderDetail,payChannelType,channelAuthCode,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,payChannelType,"05",amt = amt, orderno = orderno,channelAuthCode=channelAuthCode)

'''
    H5支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    payChannelType：支付渠道（12支付宝，13微信）
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType ; 0-公众号0模式
'''
def trade0601(appId,appKey,ordername,mhtOrderDetail,payChannelType,outputType,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,payChannelType,"0601",amt = amt, orderno = orderno,outputType=outputType)

'''
    PC支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    payChannelType：支付渠道（12支付宝，13微信）
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType：0.返回支付跳转链接 2.返回支付页面（html）
'''
def trade04(appId,appKey,ordername,mhtOrderDetail,payChannelType,amt = "1", orderno = '',outputType=0):
   return trade(appId,appKey,ordername,mhtOrderDetail,payChannelType,"04",amt = amt, orderno = orderno,outputType=outputType)


def trade(appId,appKey,ordername,mhtOrderDetail,payChannelType,deviceType, amt = "1", orderno = '',outputType = '0',channelAuthCode=''):
    paypara = {
        'funcode':'WP001',
        'version': '1.0.0',
        'appId':appId,
        'mhtOrderType' :'01',
        'mhtCurrencyType':'156',
        'mhtOrderDetail':mhtOrderDetail,
        'mhtOrderTimeOut':3600,
        'notifyUrl':'http://posp.ipaynow.cn:10808/cpgatetest/notify',
        'frontNotifyUrl':'http://posp.ipaynow.cn:10808/cpgatetest/frontnotify',
        'mhtCharset': 'UTF-8',
        'deviceType': deviceType,
        'payChannelType' : payChannelType,
        'outputType':outputType,
        'mhtSignType':'MD5'

    }
    if len(channelAuthCode) > 0:
        paypara['channelAuthCode']=channelAuthCode
    timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    if len(orderno) == 0:
        orderno = timestr + '_' +''.join(random.sample(string.ascii_letters, 16))
    paypara['mhtOrderStartTime'] = timestr
    paypara['mhtOrderNo'] = orderno
    paypara['mhtOrderName'] = ordername
    paypara['mhtOrderAmt'] = amt
    try:
        tradestr = interface.trade(appKey,paypara)
    except interface.APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    resp = requests.post("https://pay.ipaynow.cn",tradestr)
    return urllib.parse.unquote(resp.text)