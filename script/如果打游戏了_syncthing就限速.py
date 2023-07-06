#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
检测当前进程是否有运行dota2
有的话设置syncthing速度为1000m
"""


import psutil
import requests

import logging
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
        speed_limit = 9000
    config = requests.get(
        CONFIG_URL,
        headers=HEADERS,
        timeout=1,
    ).json()
    config["options"]["maxSendKbps"] = speed_limit
    res = requests.put(
        CONFIG_URL,
        headers=HEADERS,
        json=config,
        timeout=1,
    )
    res.raise_for_status()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        LOGGER.exception(e)
        raise
