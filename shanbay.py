#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-10-16 15:30:58

import requests, click
import pprint, os, json, string, re
API_URL = "https://api.shanbay.com/"
APP_KEY = "88b23593fb4146a53337"
APP_SECRET = "672395382beb0c019d9762604fd98d046b602b17"
def result(r):
    try: pprint.pprint(json.loads(r.text), indent=4)
    except:
        file = open('test.html','w')
        file.write(r.text)
        file.close()
        os.system('open test.html')
def get_auth():
    """ 获取token """
    APP_URL = "oauth2/authorize/"
    r = requests.get(
        url=os.path.join(API_URL, APP_URL),
        params={
            "client_id": APP_KEY,
            'client_secret': APP_SECRET,
            "response_type": "token", }
        )
    result(r)
@click.command()
@click.argument('word')
def get_word(word):
    APP_URL = 'bdc/search'
    r = requests.get(
        url=os.path.join(API_URL, APP_URL),
        params={'word': word}
    )
    result(r)

if __name__ == '__main__':
    get_word()
