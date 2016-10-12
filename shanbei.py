#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-10-07 16:50:51


"""
    扇贝官方API: http://www.shanbay.com/developer/wiki/intro/
"""

import requests

def get_token():
    requests.post(
        url = 'https://api.shanbay.com/oauth2/token/',
        data = {
            'client_id': '88b23593fb4146a53337',
            'grant_type': 'authorization-code',
            'code': '',
            'redirect_uri': '',
        },
    )
r = requests.get(
    url = 'https://api.shanbay.com/bdc/search/',
    params = {
        'word': 'important',
    },
)
import pprint
import json
pprint.pprint(json.loads(r.text), indent=4, width=4)
