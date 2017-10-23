import random
import string
import time
import urllib

from ipaynowPythonSdk.ipaynow import interface


def getTradeStr(amt = 1, mhtOrderDetail='', orderno = '',ordername = 'ordername'):
    #
    paypara = {}
    paypara = {
        'funcode':'WP001',
        'appId':'1482402994841173',
        'mhtOrderType' :'01',
        'mhtCurrencyType':'156',
        'mhtOrderDetail':'ipaynowPythonSDKTestOrder',
        'mhtOrderTimeOut':3600,
        'notifyUrl':'http://posp.ipaynow.cn:10808/cpgatetest/notify',
        'frontNotifyUrl': 'http://posp.ipaynow.cn:10808/cpgatetest/frontnotify',
        'mhtCharset': 'UTF-8',
        'deviceType': '0601',
        'payChannelType' : '12',
        'mhtReserved':'',
        'consumerId':'',
        'mhtSignType':'MD5'
    }
    timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    if len(orderno) == 0:
        orderno = timestr + '_' +''.join(random.sample(string.ascii_letters, 16))
    paypara['mhtOrderStartTime'] = timestr
    paypara['mhtOrderNo'] = orderno
    paypara['mhtOrderName'] = ordername
    paypara['mhtOrderAmt'] = amt
    paypara['mhtOrderDetail'] = mhtOrderDetail
    try:
        tradestr = interface.trade("zy1gE5oiWRvUYh0fUVDsAbCeLVpUl24V",paypara)
    except interface.APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    return tradestr




from pip._vendor import requests

resp = requests.post("https://pay.ipaynow.cn",getTradeStr(mhtOrderDetail='订单详情'))
print(urllib.parse.unquote(resp.text))