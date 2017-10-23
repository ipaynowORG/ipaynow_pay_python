import random
import string
import time
import urllib

from ipaynowPythonSdk.ipaynow import interface


def getTradeStr(amt = 1, mhtOrderDetail='', orderno = '',ordername = 'ordername'):
    paypara = {
        'funcode':'WP001',
        'appId':'150753086263684',
        'mhtOrderType' :'01',
        'mhtCurrencyType':'156',
        'mhtOrderDetail':'python08',
        'mhtOrderTimeOut':3600,
        'notifyUrl':'http://posp.ipaynow.cn:10808/cpgatetest/notify',
        'frontNotifyUrl': 'http://posp.ipaynow.cn:10808/cpgatetest/frontnotify',
        'mhtCharset': 'UTF-8',
        'deviceType': '08',
        'payChannelType' : '12',
        'outputType': '0',
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
        tradestr = interface.trade("zHGKLmQaU9PLMEGObyubsV5uhDAeYVqQ",paypara)
    except interface.APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    return tradestr




from pip._vendor import requests

resp = requests.post("https://pay.ipaynow.cn",getTradeStr(mhtOrderDetail='订单详情',orderno='201710231426'))
print(urllib.parse.unquote(resp.text))