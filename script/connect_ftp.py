#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import ftplib

# 1. Connect and log in
ftp = ftplib.FTP()
ftp.connect("192.168.31.6", port=2121)
ftp.login(user="wangxiang", passwd=input("输入ftp密码"))

# 2. Download the file
remote_filename = "document.txt"
local_filename = "downloaded_document.txt"

with open(local_filename, "wb") as local_file:
    # 'RETR' is the FTP command to retrieve a file
    ftp.retrbinary(f"RETR {remote_filename}", local_file.write)

print(f"Downloaded {remote_filename} successfully!")

# 3. Clean up
ftp.quit()
