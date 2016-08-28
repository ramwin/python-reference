#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-07-04 14:08:42

import requests

url = 'http://192.168.1.60:8080/api/v1/crm/LandSeaDocReceptionRecord'
files = {'file': ('test.txt', 'test text')}
values = {
    'DocumentTitle': 'test',
    'builder': 'wangxiang',
    'keywords': 'test',
    'business_id': 'business_id',
    'business_app_name': 'business_app_name',
    'buildtime': '2017-07-04 14:00:00',
    'realty_prj': 'relaty_prj',
    'reception_id': 'reception_id',
    'complainant': 'wangxiang',
    'author': 'wangxiang',
    'submit_time': '2017-04-04 14:12:00',
    'proprietor': 'yezhu',
    'reception_type': 'jiedai',
    'complain_object': 'mingyuan',
    'accept_person': 'wangxiang',
    'business_node': 'business_node',
    'folder': '{87CC030E-538F-4C66-86CE-278F1781CBB9}'
}
r = requests.post(url, files=files, data=values)
print(r.text)
