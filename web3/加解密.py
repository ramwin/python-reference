#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging
from web3 import Web3, EthereumTesterProvider
from eth_account.messages import encode_defunct, SignableMessage
from eth_account.datastructures import SignedMessage


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def basic():
    msg = "I 爱 web3"
    private_key = b"secretkey need to by 32chars len"
    w3 = Web3(EthereumTesterProvider())
    message: SignableMessage = encode_defunct(text=msg)
    signed_message: SignedMessage = w3.eth.account.sign_message(message, private_key=private_key)
    LOGGER.info("签名后: %s", signed_message)


def decrypt():
    message = "login:8bcfb9821f3d4b7e890885e4e6291543"
    encrypted = "0xe36797be11a1673c27ae95e6736b957be3ede600fc8dea6467aa527ffce73dd03d3db11ead5b78f38c97760a9dc6b16be571678dbdaf594c1bdf32ecc7a61ccc1c"
    w3 = Web3(EthereumTesterProvider())
    LOGGER.info("加密的公钥: %s",
        w3.eth.account.recover_message(
            encode_defunct(text=message),
            signature=encrypted,
        ).lower(),
    )


decrypt()
