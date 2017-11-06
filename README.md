
# 聚合支付SDK使用说明 #

## 版本变更记录 ##

- 1.0.0 : 初稿
- 1.0.1 ：接口按渠道分开，增加微信支付宝外的渠道方法

## 目录 ##

[1. 概述](#1)

&nbsp;&nbsp;&nbsp;&nbsp;[1.1 简介](#1.1)

&nbsp;&nbsp;&nbsp;&nbsp;[1.2 如何获取](#1.2)
[2. API](#2)

&nbsp;&nbsp;&nbsp;&nbsp;[2.1 聚合交易API](#2.1)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[微信被扫支付](#2.1.1)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[支付宝被扫支付](#2.1.2)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[手Q被扫支付](#2.1.3)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[京东被扫支付](#2.1.4)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[银联被扫支付](#2.1.5)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[微信主扫支付](#2.1.6)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[支付宝主扫支付](#2.1.7)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[手Q主扫支付](#2.1.8)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[京东主扫支付](#2.1.9)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[银联主扫支付](#2.1.10)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[微信公众号支付](#2.1.11)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[微信公众号支付(获取支付要素)](#2.1.12)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[支付宝公众号支付](#2.1.13)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[手Q公众号支付](#2.1.15)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[微信H5](#2.1.17)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[支付宝H5](#2.1.18)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[银联H5](#2.1.19)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[招行一网通H5](#2.1.20)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[手Q H5](#2.1.21)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[支付宝网页web](#2.1.22)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[银联网页web](#2.1.23)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[微信小程序支付](#2.1.24)


<h2 id='1'> 1. 概述 </h2>
<h4 id='1.1'> 1.1 简介 </h4>

- 聚合支付SDK Python版本，请使用Python3 。

### 1.2 如何获取 ###
 <h5 id='1.2'></h5>


[demo源码](https://github.com/ipaynowORG/ipaynow_pay_python)


## 2. 使用说明 ##

<h4 id='2.1'> 2.1 聚合交易API </h4>

交易SDK:trade.py

<h5 id='2.1.1'></h5>

- 微信被扫支付

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
    
<h5 id='2.1.2'></h5>

- 支付宝被扫支付

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
<h5 id='2.1.3'></h5>

- 手Q被扫支付

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

<h5 id='2.1.4'></h5>

- 京东被扫支付

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
<h5 id='2.1.5'></h5>

- 银联被扫支付

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
        def union_trade05(appId,appKey,ordername,mhtOrderDetail,notifyUrl,channelAuthCode,amt = "1", orderno = '')
<h5 id='2.1.6'></h5>

- 微信主扫支付

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
        def wx_trade08(appId,appKey,ordername,mhtOrderDetail,notifyUrl,outputType,amt = "1", orderno = '')
<h5 id='2.1.7'></h5>

- 支付宝主扫支付

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
        def ali_trade08(appId,appKey,ordername,mhtOrderDetail,notifyUrl,outputType,amt = "1", orderno = '')
<h5 id='2.1.8'></h5>

- 手Q主扫支付

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
        def handq_trade08(appId,appKey,ordername,mhtOrderDetail,notifyUrl,outputType,amt = "1", orderno = '')
<h5 id='2.1.9'></h5>

- 京东主扫支付

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
        def jd_trade08(appId,appKey,ordername,mhtOrderDetail,notifyUrl,outputType,amt = "1", orderno = '')
<h5 id='2.1.10'></h5>

- 银联主扫支付

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
        def union_trade08(appId,appKey,ordername,mhtOrderDetail,notifyUrl,outputType,amt = "1", orderno = '')
<h5 id='2.1.11'></h5>

- 微信公众号支付

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
        def wx_trade0600(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,outputType,amt = "1", orderno = '')

<h5 id='2.1.13'></h5>

- 支付宝公众号支付

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
        def ali_trade0600(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,outputType,amt = "1", orderno = '')

<h5 id='2.1.15'></h5>

- 手Q公众号支付

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
        def handq_trade0600(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,outputType,amt = "1", orderno = '')

<h5 id='2.1.17'></h5>

- 微信H5

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
        def wx_trade0601(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,outputType,amt = "1", orderno = '')
<h5 id='2.1.18'></h5>

- 支付宝H5

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
        def ali_trade0601(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,outputType,amt = "1", orderno = '')
<h5 id='2.1.19'></h5>

- 银联H5

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
        def union_trade0601(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,outputType,amt = "1", orderno = '')

<h5 id='2.1.20'></h5>
- 招行一网通H5

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
        def cmbywt_trade0601(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,outputType,amt = "1", orderno = '')

<h5 id='2.1.21'></h5>


- 手Q H5

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
        def handq_trade0601(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,outputType,amt = "1", orderno = '')
<h5 id='2.1.22'></h5>

- 支付宝网页web

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
        def ali_trade04(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,amt = "1", orderno = '',outputType=0)
<h5 id='2.1.23'></h5>

- 银联网页web

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
        def union_trade04(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,amt = "1", orderno = '',outputType=0)
<h5 id='2.1.24'></h5>

- 微信小程序支付

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
        def wx_app(appId,appKey,ordername,mhtOrderDetail,notifyUrl,frontNotifyUrl,oriMhtOrderAmt,discountAmt,amt = "1", orderno = '')
   
   
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
     
     
字段含义如下:

<table>
        <tr>
            <th>字段名称</th>
            <th>字段Key</th>
            <th>备注</th>
        </tr>
        <tr>
            <td>功能码</td>
            <td>funcode</td>
            <td>定值：N001</td>
        </tr>
        <tr>
            <td>接口版本号</td>
            <td>version</td>
            <td>定值：1.0.0</td>
         </tr>
<tr>
            <td>商户应用唯一标识</td>
            <td>appId</td>
            <td></td>
         </tr>
<tr>
            <td>商户订单号</td>
            <td>mhtOrderNo</td>
            <td></td>
         </tr>
<tr>
            <td>商户商品名称</td>
            <td>mhtOrderName</td>
            <td></td>
         </tr>
<tr>
            <td>商户交易类型</td>
            <td>mhtOrderType</td>
            <td></td>
         </tr>
<tr>
            <td>商户订单币种类型</td>
            <td>mhtCurrencyType</td>
            <td>156人民币</td>
         </tr>
<tr>
            <td>商户订单原单金额</td>
            <td>oriMhtOrderAmt</td>
            <td>单位(人民币)：分</td>
         </tr>
<tr>
            <td>商户订单实付金额</td>
            <td>mhtOrderAmt</td>
            <td>单位(人民币)：分</td>
         </tr>
<tr>
            <td>商户订单优惠金额</td>
            <td>discountAmt</td>
            <td>单位(人民币)：分</td>
         </tr>
<tr>
            <td>商户订单超时时间</td>
            <td>mhtOrderTimeOut</td>
            <td>60~3600秒，默认3600</td>
         </tr>
<tr>
            <td>商户订单开始时间</td>
            <td>mhtOrderStartTime</td>
            <td>yyyyMMddHHmmss</td>
         </tr>
<tr>
            <td>支付成功时间</td>
            <td>payTime</td>
            <td>yyyyMMddHHmmss</td>
         </tr>
<tr>
            <td>商户字符编码</td>
            <td>mhtCharset</td>
            <td>UTF-8</td>
         </tr>
<tr>
            <td>现在支付流水号</td>
            <td>nowPayOrderNo</td>
            <td></td>
         </tr>
<tr>
            <td>设备类型</td>
            <td>deviceType</td>
            <td></td>
         </tr>
<tr>
            <td>用户所选渠道类型</td>
            <td>payChannelType</td>
            <td>12-支付宝 13-微信 27-银联 04-京东 25-手Q</td>
         </tr>
<tr>
            <td>交易支付状态</td>
            <td>transStatus</td>
            <td></td>
         </tr>
<tr>
            <td>渠道订单号</td>
            <td>channelOrderNo</td>
            <td></td>
         </tr>
<tr>
            <td>付款人账号</td>
            <td>payConsumerId</td>
            <td>微信返回sub_openid,支付宝返回buyer_user_id</td>
         </tr>
<tr>
            <td>商户保留域</td>
            <td>mhtReserved</td>
            <td>给商户使用的字段，商户可以对交易进行标记，现在支付将原样返回</td>
         </tr>
<tr>
            <td>签名方法</td>
            <td>signType</td>
            <td>定值：MD5</td>
         </tr>
<tr>
            <td>数据签名</td>
            <td>signature</td>
            <td>除signature字段外，所有参数都参与MD5签名</td>
         </tr>
<tr>
            <td>银行类型</td>
            <td>bankType</td>
            <td>微信渠道返回</td>
         </tr>
<tr>
            <td>卡类型</td>
            <td>cardType</td>
            <td>CREDIT 信用卡  DEBIT  借记卡</td>
         </tr>
    </table>
         
