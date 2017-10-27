
# 聚合支付SDK使用说明 #

## 版本变更记录 ##

- 1.0.0 : 初稿

## 1. 概述 ##

### 1.1 简介 ###

- 聚合支付SDK Python版本，请使用Python3 。

### 1.2 如何获取 ###


[demo源码](https://github.com/ipaynowORG/ipaynow_pay_python)


## 2. 使用说明 ##

### 2.1 工具说明 ###
- 支付接口: ipaynowPythonSdk
   
    trade.py
    
 - H5支付
    
    
        '''
        appId:商户应用id
        appKey:商户应用秘钥
        mhtOrderDetail：订单详情
        notifyUrl:商户后台通知URL
        frontNotifyUrl :商户前台通知URL
        payChannelType：支付渠道（12支付宝，13微信）
        amt:订单金额单位分，默认1分
        orderno:订单号（默认系统时间）
        outputType ; 0-公众号0模式
        '''  
        def trade0601(appId,appKey,ordername,mhtOrderDetail,payChannelType,outputType,amt = "1", orderno = ''):  
    
 - 公众号支付
    
   
          '''
        appId:商户应用id
        appKey:商户应用秘钥
        mhtOrderDetail：订单详情
        notifyUrl:商户后台通知URL
        frontNotifyUrl :商户前台通知URL
        payChannelType：支付渠道（12支付宝，13微信）
        amt:订单金额单位分，默认1分
        orderno:订单号（默认系统时间）
        outputType ; 0-公众号0模式
        '''
        def trade0600(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,payChannelType,outputType,amt = "1", orderno = ''):

 - 主扫支付 
    
  
        '''  
        appId:商户应用id
        appKey:商户应用秘钥
        mhtOrderDetail：订单详情
        notifyUrl:商户后台通知URL
        payChannelType：支付渠道（12支付宝，13微信）
        amt:订单金额单位分，默认1分
        orderno:订单号（默认系统时间）
        outputType ; 0 返回二维码串 1 返回支付链接
        '''
        def trade08(appId,appKey,ordername,mhtOrderDetail,notifyUrl,payChannelType,outputType,amt = "1", orderno = ''):
   
 -  被扫支付  
         
 
          '''
         appId:商户应用id
         appKey:商户应用秘钥
         mhtOrderDetail：订单详情
         notifyUrl:商户后台通知URL
         payChannelType：支付渠道（12支付宝，13微信）
         amt:订单金额单位分，默认1分
         orderno:订单号（默认系统时间）
         channelAuthCode ; 支付授权码
         '''
         def trade05(appId,appKey,ordername,mhtOrderDetail,notifyUrl,payChannelType,channelAuthCode,amt = "1", orderno = ''):
   
   - PC 支付
   
         '''
         appId:商户应用id
         appKey:商户应用秘钥
         mhtOrderDetail：订单详情
         notifyUrl:商户后台通知URL
         frontNotifyUrl :商户前台通知URL
         payChannelType：支付渠道（12支付宝，13微信）
         amt:订单金额单位分，默认1分
         orderno:订单号（默认系统时间）
         outputType：0.返回支付跳转链接 2.返回支付页面（html）
         '''
         def trade04(appId,appKey,ordername,mhtOrderDetail,payChannelType,notifyUrl,frontNotifyUrl,amt = "1", orderno = '',outputType=0):
   
   
### 2.2 DEMO使用 ###

   使用方法:
   
   您可以从 GitHub 上下载 Python SDK 的源代码：
   
    git clone https://github.com/ipaynowORG/ipaynow_pay_python

    1.cd 进入ipaynowPythonSdk 文件夹
    2.执行 "python setup.py install"
    3.在代码中 import ipaynow
     参考示例代码
     示例代码
     cd 进入example文件夹
     运行 python tradeTest.py 
         
