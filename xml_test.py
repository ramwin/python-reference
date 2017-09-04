#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-08-07 10:34:26

import dicttoxml
import json
from xml.dom.minidom import parseString


data = {
    'appid': 'wx2421b1c4370ec43b',
    'attach': '支付测试',
    'body': 'H5支付测试',
    'mch_id': '10000100',
    'nonce_str': '1add1a30ac87aa2db72f57a2375d8fec',
    'notify_url': 'http://wxpay.wxutil.com/pub_v2/pay/notify.v2.php',
    'openid': 'oUpF8uMuAJO_M2pxb1Q9zNjWeS6o',
    'out_trade_no': '1415659990',
    'spbill_create_ip': '14.23.150.211',
    'total_fee': '1',
    'trade_type': 'MWEB',
    'scene_info': '{"h5_info": {"type":"IOS","app_name": "王者荣耀","package_name": "com.tencent.tmgp.sgame"}}',
    'sign': '0CB01533B8C1EF103065174F50BCA001',
}


def main():
    xml = dicttoxml.dicttoxml(data)
    dom = parseString(xml)
    print(dom.toprettyxml())

if __name__ == '__main__':
    main()
