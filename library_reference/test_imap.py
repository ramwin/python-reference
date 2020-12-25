#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-12-22 10:24:30


import getpass, imaplib

M = imaplib.IMAP4("imap.exmail.qq.com", port=143)
M.login("wx@ruitiancapital.com", getpass.getpass())
M.select()
typ, data = M.search(None, 'ALL')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    print('Message %s\n%s\n' % (num, data[0][1]))
M.close()
M.logout()
