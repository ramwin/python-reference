# -*- coding: utf-8 -*-
'''
发送html文本邮件
小五义：http://www.cnblogs.com/xiaowuyi
gopzbloojbfujxzb
'''
import smtplib  
from email.mime.text import MIMEText  
# mailto_list=["1846468966@qq.com"]
# mail_host="smtp.163.com"  #设置服务器
# mail_user="zettage_wangx"    #用户名
# mail_pass="gopzbloojbfujxzb"   #口令 
# mail_postfix="163.com"  #发件箱的后缀

mailto_list=["ramwin@qq.com"]
mail_host="smtp.163.com"  #设置服务器
mail_user="zettage_wangx"    #用户名
mail_pass="zettage321"   #口令 
mail_postfix="163.com"  #发件箱的后缀

def send_mail(to_list,sub,content = '爬虫中断了'):  #to_list：收件人；sub：主题；content：邮件内容
    content = '''出大事了, %s'''%(content)
    me="王祥"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='text',_charset='utf-8')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        s = smtplib.SMTP()  
        s.connect(mail_host)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()  
        return True  
    except Exception as e:  
        print(e)
        return False  


# 使用yagmail 来发送邮件

import yagmail
print("yag")
yag = yagmail.SMTP("zettage_wangx@163.com", "Zettage321")
print("yag生成")
# yag = yagmail.SMTP("meeting_service@inmindglobal.com")
contents = ["This is the body, and here is just text http://www.ramwin.com/media/portrait.png",
    "You can find a autio file attached,", "/local/path/song.mp3"]
print("准备发送邮件")
a = yag.send("ramwin@qq.com", "subject", contents)
print(a)
