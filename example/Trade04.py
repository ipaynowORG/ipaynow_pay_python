import random
import string
import time
import urllib

from ipaynowPythonSdk.ipaynow import interface


def getTradeStr(amt = 1, orderno = '',ordername = 'ordername'):
    #
    paypara = {}
    paypara = {
        'funcode':'WP001',
        'version': '1.0.0',
        'appId':'150753107733024',
        'mhtOrderType' :'01',
        'mhtCurrencyType':'156',
        'mhtOrderDetail':'ipaynowPythonSDKTestOrder',
        'mhtOrderTimeOut':3600,
        'notifyUrl':'http://posp.ipaynow.cn:10808/cpgatetest/notify',
        'frontNotifyUrl':'http://posp.ipaynow.cn:10808/cpgatetest/frontnotify',
        'mhtCharset': 'UTF-8',
        'deviceType': '04',
        'payChannelType' : '12',
        'outputType':'0',
        #'mhtSubAppId':'wx0b5cc697d69ab732',
        'mhtLimitPay':'',
        #'consumerId':'ofJA_wc8GygaK6WTsp0VadnUDCR8',
        'mhtSignType':'MD5'
    }
    timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    if len(orderno) == 0:
        orderno = timestr + '_' +''.join(random.sample(string.ascii_letters, 16))
    paypara['mhtOrderStartTime'] = timestr
    paypara['mhtOrderNo'] = orderno
    paypara['mhtOrderName'] = ordername
    paypara['mhtOrderAmt'] = amt
    try:
        tradestr = interface.trade("4Bl0qsRhe5xhRn3sO0Kwomqts6WgpMbq",paypara)
    except interface.APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    return tradestr




from pip._vendor import requests

resp = requests.post("https://pay.ipaynow.cn",getTradeStr())
print(resp.text)
print(urllib.parse.unquote(resp.text))