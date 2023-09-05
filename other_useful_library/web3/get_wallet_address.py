#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3, EthereumTesterProvider
from web3.middleware import construct_sign_and_send_raw_middleware

w3 = Web3(EthereumTesterProvider())

private_key = "0xf87f727f6386a4f41444204cfc11d8fb3aba38479a26c39c7f128cec7e6336b5"

assert private_key is not None, "You must set PRIVATE_KEY environment variable"
assert private_key.startswith("0x"), "Private key must start with 0x hex prefix"

account: LocalAccount = Account.from_key(private_key)
w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))

print(f"Your hot wallet address is {account.address}")

# Now you can use web3.eth.send_transaction(), Contract.functions.xxx.transact() functions
# with your local private key through middleware and you no longer get the error
# "ValueError: The method eth_sendTransaction does not exist/is not available
