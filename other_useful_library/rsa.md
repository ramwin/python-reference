#### Xiang Wang @ 2017-11-16 14:16:29

### 基础
* [官网](https://stuvel.eu/python-rsa-doc/index.html)
* [使用]
    import rsa
    pubkey, privkey = rsa.newkeys(2048, poolsize=8)
    message = 'hello world!'.encode('utf8')
    crypto = rsa.encrypt(message, pubkey)
    print(rsa.decrypt(crypto, privkey))
