#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-23 18:05:26

# https://docs.python.org/3/library/smtplib.html#smtp-example



import smtplib
from email.mime.text import MIMEText
from email.header import Header


def basic():
    def prompt(prompt):
        return input(prompt).strip()
    
    fromaddr = prompt("From: ") or "ramwin@ramwin.com"
    toaddrs  = (prompt("To: ") or "wangxiang@inmindglobal.com").split()
    subject = (prompt("Subject: ") or "Subject")
    print("Enter message, end with ^D (Unix) or ^Z (Windows):")
    
    # Add the From: and To: headers at the start!
    msg = ("From: %s\r\nTo: %s\r\n\r\nSubject: %s\r\n\r\n"
           % (fromaddr, ", ".join(toaddrs), subject))
    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            break
        msg = msg + line
    
    print("Message length is", len(msg))
    
    server = smtplib.SMTP('localhost')
    server.set_debuglevel(1)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


def use_mail():
    import smtplib
    
    # Import the email modules we'll need
    from email.message import EmailMessage
    
    # Open the plain text file whose name is in textfile for reading.
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content('内容')
    
    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = '主题'
    msg['From'] = 'ramwin@ramwin.com'
    msg['To'] = 'wangxiang@inmindglobal.com'
    
    # Send the message via our own SMTP server.
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()


def send():
    """最新版，已经用阿里云邮箱测试过了"""
    msg = MIMEText("<p>使用Python可以做很多事情</p>",  "html" "utf-8")
    msg["Subject"] = Header("主题", 'utf-8')
    msg['From'] = Header('ramwin@alumni.sjtu.edu.cn', 'utf-8')
    msg['To'] = Header('ramwin@qq.com', 'utf-8')
    s = smtplib.SMTP('smtp.sjtu.edu.cn')
    password = input("输入邮箱密码")
    s.login('ramwin', password)
    s.sendmail(from_addr='ramwin@alumni.sjtu.edu.cn', to_addrs=['ramwin@qq.com'], msg=msg.as_string())

if __name__ == '__main__':
    send()
