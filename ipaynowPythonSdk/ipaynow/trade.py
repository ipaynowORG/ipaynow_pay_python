import random
import string
import time
import urllib

from ipaynowPythonSdk.ipaynow import interface
from pip._vendor import requests



'''
    微信公众号支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    frontNotifyUrl :商户前台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType ; 0-公众号0模式
'''
def wx_trade0600(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,outputType,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,frontNotifyUrl=frontNotifyUrl,payChannelType="13",deviceType="0600",amt = amt, orderno = orderno,outputType=outputType)

'''
    支付宝公众号支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    frontNotifyUrl :商户前台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType ; 0-公众号0模式
'''
def ali_trade0600(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,outputType,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,frontNotifyUrl=frontNotifyUrl,payChannelType="12",deviceType="0600",amt = amt, orderno = orderno,outputType=outputType)


'''
    手Q公众号支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    frontNotifyUrl :商户前台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType ; 0-公众号0模式
'''
def handq_trade0600(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,outputType,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,frontNotifyUrl=frontNotifyUrl,payChannelType="25",deviceType="0600",amt = amt, orderno = orderno,outputType=outputType)

'''
    微信主扫支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType ; 0 返回二维码串 1 返回支付链接
'''
def wx_trade08(appId,appKey,ordername,mhtOrderDetail,notifyUrl,outputType,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,payChannelType="13",deviceType="08",amt = amt, orderno = orderno,outputType=outputType)


'''
    支付宝主扫支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType ; 0 返回二维码串 1 返回支付链接
'''
def ali_trade08(appId,appKey,ordername,mhtOrderDetail,notifyUrl,outputType,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,payChannelType="12",deviceType="08",amt = amt, orderno = orderno,outputType=outputType)

'''
    手Q主扫支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType ; 0 返回二维码串 1 返回支付链接
'''
def handq_trade08(appId,appKey,ordername,mhtOrderDetail,notifyUrl,outputType,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,payChannelType="25",deviceType="08",amt = amt, orderno = orderno,outputType=outputType)

'''
    京东主扫支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType ; 0 返回二维码串 1 返回支付链接
'''
def jd_trade08(appId,appKey,ordername,mhtOrderDetail,notifyUrl,outputType,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,payChannelType="04",deviceType="08",amt = amt, orderno = orderno,outputType=outputType)


'''
    银联主扫支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType ; 0 返回二维码串 1 返回支付链接
'''
def union_trade08(appId,appKey,ordername,mhtOrderDetail,notifyUrl,outputType,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,payChannelType="27",deviceType="08",amt = amt, orderno = orderno,outputType=outputType)

'''
    微信被扫支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    channelAuthCode ; 支付授权码
'''
def wx_trade05(appId,appKey,ordername,mhtOrderDetail,notifyUrl,channelAuthCode,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,payChannelType="13",deviceType="05",amt = amt, orderno = orderno,channelAuthCode=channelAuthCode)


'''
    支付宝被扫支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    channelAuthCode ; 支付授权码
'''
def ali_trade05(appId,appKey,ordername,mhtOrderDetail,notifyUrl,channelAuthCode,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,payChannelType="12",deviceType="05",amt = amt, orderno = orderno,channelAuthCode=channelAuthCode)


'''
    手Q被扫支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    channelAuthCode ; 支付授权码
'''
def handq_trade05(appId,appKey,ordername,mhtOrderDetail,notifyUrl,channelAuthCode,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,payChannelType="25",deviceType="05",amt = amt, orderno = orderno,channelAuthCode=channelAuthCode)


'''
    京东被扫支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    channelAuthCode ; 支付授权码
'''
def jd_trade05(appId,appKey,ordername,mhtOrderDetail,notifyUrl,channelAuthCode,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,payChannelType="04",deviceType="05",amt = amt, orderno = orderno,channelAuthCode=channelAuthCode)



'''
    银联被扫支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    channelAuthCode ; 支付授权码
'''
def union_trade05(appId,appKey,ordername,mhtOrderDetail,notifyUrl,channelAuthCode,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,payChannelType="27",deviceType="05",amt = amt, orderno = orderno,channelAuthCode=channelAuthCode)


'''
    微信H5支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    frontNotifyUrl :商户前台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType ; 0-公众号0模式
'''
def wx_trade0601(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,outputType,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,frontNotifyUrl=frontNotifyUrl,payChannelType="13",deviceType="0601",amt = amt, orderno = orderno,outputType=outputType)


'''
    支付宝H5支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    frontNotifyUrl :商户前台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType ; 0-公众号0模式
'''
def ali_trade0601(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,outputType,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,frontNotifyUrl=frontNotifyUrl,payChannelType="12",deviceType="0601",amt = amt, orderno = orderno,outputType=outputType)

'''
    银联H5支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    frontNotifyUrl :商户前台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType ; 0-公众号0模式
'''
def union_trade0601(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,outputType,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,frontNotifyUrl=frontNotifyUrl,payChannelType="27",deviceType="0601",amt = amt, orderno = orderno,outputType=outputType)

'''
    手Q H5支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    frontNotifyUrl :商户前台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType ; 0-公众号0模式
'''
def handq_trade0601(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,outputType,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,frontNotifyUrl=frontNotifyUrl,payChannelType="12",deviceType="0601",amt = amt, orderno = orderno,outputType=outputType)

'''
    招行一网通 H5支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    frontNotifyUrl :商户前台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType ; 0-公众号0模式
'''
def cmbywt_trade0601(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,outputType,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,notifyUrl=notifyUrl,frontNotifyUrl=frontNotifyUrl,payChannelType="17",deviceType="0601",amt = amt, orderno = orderno,outputType=outputType)


'''
    支付宝网页web支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    frontNotifyUrl :商户前台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType：0.返回支付跳转链接 2.返回支付页面（html）
'''
def ali_trade04(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,amt = "1", orderno = '',outputType=0):
   return trade(appId,appKey,ordername,mhtOrderDetail,payChannelType="12",notifyUrl=notifyUrl,frontNotifyUrl=frontNotifyUrl,deviceType="04",amt = amt, orderno = orderno,outputType=outputType)

'''
    银联网页web支付
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    notifyUrl:商户后台通知URL
    frontNotifyUrl :商户前台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
    outputType：0.返回支付跳转链接 2.返回支付页面（html）
'''
def union_trade04(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,amt = "1", orderno = '',outputType=0):
   return trade(appId,appKey,ordername,mhtOrderDetail,payChannelType="27",notifyUrl=notifyUrl,frontNotifyUrl=frontNotifyUrl,deviceType="04",amt = amt, orderno = orderno,outputType=outputType)


'''
    微信小程序
    appId:商户应用id
    appKey:商户应用秘钥
    mhtOrderDetail：订单详情
    oriMhtOrderAmt:原始金额
    discountAmt:优惠金额
    notifyUrl:商户后台通知URL
    frontNotifyUrl :商户前台通知URL
    amt:订单金额单位分，默认1分
    orderno:订单号（默认系统时间）
'''
def wx_app(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,oriMhtOrderAmt,discountAmt,amt = "1", orderno = ''):
   return trade(appId,appKey,ordername,mhtOrderDetail,payChannelType="13",notifyUrl=notifyUrl,frontNotifyUrl=frontNotifyUrl,deviceType="14",oriMhtOrderAmt=oriMhtOrderAmt,discountAmt=discountAmt,amt = amt, orderno = orderno,outputType="1")


def trade(appId,appKey,ordername,mhtOrderDetail,payChannelType,deviceType,notifyUrl,frontNotifyUrl="", amt = "1", orderno = '',outputType = '0',channelAuthCode='',oriMhtOrderAmt='',discountAmt=''):
    paypara = {
        'funcode':'WP001',
        'version': '1.0.0',
        'appId':appId,
        'mhtOrderType' :'01',
        'mhtCurrencyType':'156',
        'mhtOrderDetail':mhtOrderDetail,
        'mhtOrderTimeOut':3600,
        'notifyUrl':notifyUrl,
        'mhtCharset': 'UTF-8',
        'deviceType': deviceType,
        'payChannelType' : payChannelType,
        'outputType':outputType,
        'mhtSignType':'MD5'

    }
    if len(frontNotifyUrl) > 0 :
        paypara["frontNotifyUrl"] = frontNotifyUrl
    if len(channelAuthCode) > 0:
        paypara['channelAuthCode']=channelAuthCode
    timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    if len(orderno) == 0:
        orderno = timestr + '_' +''.join(random.sample(string.ascii_letters, 16))
    paypara['mhtOrderStartTime'] = timestr
    paypara['mhtOrderNo'] = orderno
    paypara['mhtOrderName'] = ordername
    paypara['mhtOrderAmt'] = amt
    if len(oriMhtOrderAmt) > 0 :
        paypara["oriMhtOrderAmt"] = oriMhtOrderAmt

    if len(discountAmt) > 0 :
        paypara["discountAmt"] = discountAmt
    try:
        tradestr = interface.trade(appKey,paypara)
    except interface.APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    resp = requests.post("https://pay.ipaynow.cn",tradestr)
    return urllib.parse.unquote(resp.text)