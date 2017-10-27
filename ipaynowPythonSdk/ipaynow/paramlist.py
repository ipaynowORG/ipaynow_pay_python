#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4

# define interface parameter attributes and max len

# key name 'name' indicates parameter name
# key name 'must' indicates parameter
# WP001-无插件聚合支付
WP001_PostList = [
    {'name': 'funcode', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 5, 'desp': "功能码"},
    {'name': 'version', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 5, 'desp': "版本1.0.0"},
    {'name': 'appId', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户应用唯一标识"},
    {'name': 'mhtOrderNo', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户订单号"},
    {'name': 'mhtOrderName', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户商品名称"},
    {'name': 'mhtOrderType', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户交易类型"},
    {'name': 'mhtCurrencyType', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 3, 'desp': "商户订单币种类型"},
    {'name': 'mhtOrderAmt', 'mandatory': 'Y', 'md5': 'Y', 'type': 'num', 'len': 22, 'desp': "商户订单交易金额"},
    {'name': 'mhtOrderDetail', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 200, 'desp': "商户订单详情"},
    {'name': 'mhtOrderTimeOut', 'mandatory': 'N', 'md5': 'Y', 'type': 'num', 'len': 4, 'desp': "商户订单超时时间"},
    {'name': 'mhtOrderStartTime', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 14, 'desp': "商户订单开始时间"},
    {'name': 'notifyUrl', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 200, 'desp': "商户后台通知URL"},
    {'name': 'frontNotifyUrl', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 200, 'desp': "商户前台通知URL"},
    {'name': 'mhtCharset', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 16, 'desp': "商户字符编码-UTF8"},
    {'name': 'deviceType', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 4, 'desp': "设备类型"},
    {'name': 'payChannelType', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 2, 'desp': "用户所选渠道类型"},
    {'name': 'channelAuthCode', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 20, 'desp': "渠道编号"},
    {'name': 'mhtReserved', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 100, 'desp': "商户保留域"},
    {'name': 'consumerId', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "消费者ID"},
    {'name': 'outputType', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 2, 'desp': "输出格式"},
    {'name': 'mhtSubAppId', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 64, 'desp': "公众号appId"},
    {'name': 'mhtSignType', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 3, 'desp': "商户签名方法-MD5"},
    {'name': 'mhtSignature', 'mandatory': 'Y', 'md5': 'N', 'type': 'str', 'len': 64, 'desp': "商户数据签名"}

]
# 接口接入URL：https://api.ipaynow.cn  请求类型：POST

# WP001-无插件聚合支付 Response
# 支付交易同步返回
WP001_RespList = [
    {'name': 'funcode', 'mandatory': 'Y', 'md5': 'N', 'type': 'str', 'len': 4, 'desp': "功能码"},
    {'name': 'version', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 5, 'desp': "版本1.0.0"},
    {'name': 'appId', 'mandatory': 'Y', 'md5': 'N', 'type': 'str', 'len': 40, 'desp': "商户应用唯一标识"},
    {'name': 'mhtOrderNo', 'mandatory': 'Y', 'md5': 'N', 'type': 'str', 'len': 40, 'desp': "商户订单号"},
    {'name': 'responseTime', 'mandatory': 'Y', 'md5': 'N', 'type': 'str', 'len': 40, 'desp': "响应时间"},
    {'name': 'responseCode', 'mandatory': 'Y', 'md5': 'N', 'type': 'str', 'len': 4, 'desp': "响应码"},
    {'name': 'responseMsg', 'mandatory': 'N', 'md5': 'N', 'type': 'str', 'len': 100, 'desp': "响应信息"},
    {'name': 'nowPayOrderNo', 'mandatory': 'N', 'md5': 'N', 'type': 'str', 'len': 40, 'desp': "现在支付订单号(TN)"}
]

# MQ002-商户支付订单查询
# 接口接入URL：https://api.ipaynow.cn  请求类型：POST  由商户发起
MQ001_PostList = [
    {'name': 'funcode', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 5, 'desp': "功能码"},
    {'name': 'version', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 5, 'desp': "版本1.0.0"},
    {'name': 'appId', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户应用唯一标识"},
    {'name': 'deviceType', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 4, 'desp': "设备类型"},
    {'name': 'mhtOrderNo', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户订单号"},
    {'name': 'mhtCharset', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 6, 'desp': "商户字符集"},
    {'name': 'mhtSignType', 'mandatory': 'Y', 'md5': 'N', 'type': 'str', 'len': 6, 'desp': "签名方法"},
    {'name': 'mhtSignature', 'mandatory': 'Y', 'md5': 'N', 'type': 'str', 'len': 64, 'desp': "数据签名"}
]

# MQ001-商户支付订单查询 Response
# 支付交易同步返回
MQ001_RespList = [
    {'name': 'appId', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户应用唯一标识"},
    {'name': 'version', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 5, 'desp': "版本1.0.0"},
    {'name': 'mhtOrderNo', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户订单号"},
    {'name': 'mhtOrderName', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户商品名称"},
    {'name': 'mhtOrderType', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 2, 'desp': "订单交易类型"},
    {'name': 'mhtCurrencyType', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 3, 'desp': "订单币种类型"},
    {'name': 'mhtOrderAmt', 'mandatory': 'Y', 'md5': 'Y', 'type': 'num', 'len': 22, 'desp': "订单交易金额"},
    {'name': 'mhtOrderTimeOut', 'mandatory': 'N', 'md5': 'Y', 'type': 'num', 'len': 4, 'desp': "订单超时时间"},
    {'name': 'mhtOrderStartTime', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 14, 'desp': "订单开始时间"},
    {'name': 'mhtCharset', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 6, 'desp': "交易字符编码"},
    {'name': 'deviceType', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 2, 'desp': "设备类型"},
    {'name': 'payChannelType', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 2, 'desp': "用户所选渠道类型"},
    {'name': 'fee', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 22, 'desp': "交易手续费"},
    {'name': 'settleAmt', 'mandatory': 'N', 'md5': 'Y', 'type': 'num', 'len': 22, 'desp': "商户结算金额"},
    {'name': 'transStatus', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 4, 'desp': "交易状态"},
    {'name': 'responseTime', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 14, 'desp': "响应时间"},
    {'name': 'responseCode', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 4, 'desp': "响应码"},
    {'name': 'responseMsg', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 100, 'desp': "响应信息"},
    {'name': 'signType', 'mandatory': 'Y', 'md5': 'N', 'type': 'str', 'len': 6, 'desp': "签名方法"},
    {'name': 'signature', 'mandatory': 'Y', 'md5': 'N', 'type': 'str', 'len': 64, 'desp': "数据签名"}
]

# N001-商户服务器端支付结果通知
# 现在支付的聚合支付服务端异步发起：  --通讯方式：HTTP POST 方式--
N001_QueryList = [
    {'name': 'funcode', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 4, 'desp': "功能码"},
    {'name': 'version', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 5, 'desp': "版本1.0.0"},
    {'name': 'appId', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户应用唯一标识"},
    {'name': 'mhtOrderNo', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户订单号"},
    {'name': 'mhtOrderName', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户商品名称"},
    {'name': 'mhtOrderType', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 2, 'desp': "商户交易类型"},
    {'name': 'mhtCurrencyType', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 3, 'desp': "商户订单币种类型"},
    {'name': 'mhtOrderAmt', 'mandatory': 'Y', 'md5': 'Y', 'type': 'num', 'len': 22, 'desp': "商户订单交易金额"},
    {'name': 'mhtOrderTimeOut', 'mandatory': 'N', 'md5': 'Y', 'type': 'num', 'len': 4, 'desp': "商户订单超时时间"},
    {'name': 'mhtOrderStartTime', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 14, 'desp': "商户订单开始时间"},
    {'name': 'mhtCharset', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 6, 'desp': "商户字符编码"},
    {'name': 'deviceType', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 2, 'desp': "设备类型"},
    {'name': 'payChannelType', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 2, 'desp': "用户所选渠道类型"},
    {'name': 'nowPayOrderNo', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 64, 'desp': "现在支付账号"},
    {'name': 'tradeStatus', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 4, 'desp': "交易支付状态"},
    {'name': 'mhtReserved', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 100, 'desp': "商户保留域"},
    {'name': 'signType', 'mandatory': 'Y', 'md5': 'N', 'type': 'str', 'len': 6, 'desp': "签名方法"},
    {'name': 'signature', 'mandatory': 'Y', 'md5': 'N', 'type': 'str', 'len': 64, 'desp': "数据签名"},
    {'name': 'channelOrderNo', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 100, 'desp': "渠道订单号"}
]

# N001-商户服务器端支付结果通知 Resp
N001_RespList = [
    {'name': 'success', 'mandatory': 'Y', 'md5': 'N', 'type': 'str', 'len': 1, 'desp': "是否成功"}
]

# N002-商户前端支付结果通知
N002_NotifyList = [
    {'name': 'funcode', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 4, 'desp': "功能码"},
    {'name': 'version', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 5, 'desp': "版本1.0.0"},
    {'name': 'appId', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户应用唯一标识"},
    {'name': 'mhtOrderNo', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户订单号"},
    {'name': 'mhtCharset', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 6, 'desp': "商户字符编码"},
    {'name': 'tradeStatus', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 4, 'desp': "交易支付状态"},
    {'name': 'mhtReserved', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 100, 'desp': "商户保留域"},
    {'name': 'signType', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 6, 'desp': "签名方法"},
    {'name': 'signature', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 64, 'desp': "数据签名"},
]
