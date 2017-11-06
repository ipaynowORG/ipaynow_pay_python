#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4


from ipaynowPythonSdk.ipaynow.trade import ali_trade05

print(ali_trade05("150753082825470", "8jTST7ywIBY0QQ3RlcxWEl08Xj9gaYyQ", "orderNaem python05", "orederDetil",
              notifyUrl="https://op-tester.ipaynow.cn/paytest/notify",channelAuthCode="135339698149197910",amt="2",
              orderno=""));

# print(trade08(appId="150753086263684",appKey="zHGKLmQaU9PLMEGObyubsV5uhDAeYVqQ",ordername="ordername",mhtOrderDetail="detil",notifyUrl="https://op-tester.ipaynow.cn/paytest/notify",payChannelType="12",outputType="0"));

# print(trade0600(appId="150753094138037",appKey="n0bloMQxHYDfwnqlF6poU6P6i9mXzdWB",ordername="ordername",mhtOrderDetail="detil",notifyUrl="https://op-tester.ipaynow.cn/paytest/notify",frontNotifyUrl="https://op-tester.ipaynow.cn/paytest/notify",payChannelType="12",outputType="0"));


# print(trade0601(appId="1482402994841173",appKey="zy1gE5oiWRvUYh0fUVDsAbCeLVpUl24V",ordername="ordername",mhtOrderDetail="detil",notifyUrl="https://op-tester.ipaynow.cn/paytest/notify",frontNotifyUrl="https://op-tester.ipaynow.cn/paytest/notify",payChannelType="12",outputType="0"));