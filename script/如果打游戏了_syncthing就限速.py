#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
检测当前进程是否有运行dota2
有的话设置syncthing速度为1000m
"""


import time

import logging

import psutil
import requests

import logging_config


GAMES = [
    "dota2.exe",
]

HEADERS = {"X-API-Key": "3iRZPuLmwNNtdtKJA5joUxP4CNCxwzgb"}
CONFIG_URL = "http://localhost:8384/rest/config"
LOGGER = logging.getLogger(__name__)


def is_playing_games() -> bool:
    for p in psutil.process_iter():
        name = p.name()
        if name in GAMES:
            return True
    return False


def main():
    if is_playing_games():
        speed_limit = 100
    else:
        speed_limit = 8000
    config = requests.get(
        CONFIG_URL,
        headers=HEADERS,
        timeout=1,
    ).json()
    LOGGER.info("当前限速: %d", config["options"]["maxSendKbps"])
    config["options"]["maxSendKbps"] = speed_limit
    res = requests.put(
        CONFIG_URL,
        headers=HEADERS,
        json=config,
        timeout=1,
    )
    res.raise_for_status()


if __name__ == "__main__":
    LOGGER.info("执行")
    try:
        main()
        time.sleep(5 * 60 / 2)
        main()
        LOGGER.info("完成")
    except requests.exceptions.ConnectTimeout:
        LOGGER.info("服务尚未启动")
    except Exception as e:
        LOGGER.exception(e)
        raise
