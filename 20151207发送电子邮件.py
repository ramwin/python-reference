# -*- coding: utf-8 -*-
'''
发送html文本邮件
小五义：http://www.cnblogs.com/xiaowuyi
gopzbloojbfujxzb
'''
import smtplib  
from email.mime.text import MIMEText  
mailto_list=["zettage_wangx@163.com"]
mail_host="smtp.163.com"  #设置服务器
mail_user="zettage_wangx"    #用户名
mail_pass="gopzbloojbfujxzb"   #口令 
mail_postfix="163.com"  #发件箱的后缀

def send_mail(to_list,sub,random_string):  #to_list：收件人；sub：主题；content：邮件内容
    content = '''
        <h1>感谢您注册振古科技数据邦</h1>
        <p>请点击下面的链接确认注册</p> <a href='http://192.168.1.88/normal/email_confime?code={random_string}'>点击确认</a>
        <p>如果链接无法点击，请复制以下链接进行访问</p><br>
        <p>http://192.168.1.88/normal/email_confime?code={random_string}</p>
    '''.format(random_string=random_string)
    me="振古科技数据邦注册确认"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='utf-8')    #创建一个实例，这里设置为html格式邮件
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
    except Exception, e:  
        print str(e)  
        return False  
if __name__ == '__main__':  
    if send_mail(mailto_list,"hello",random_string='werrewewaasd'):  
        print "发送成功"  
    else:  
        print "发送失败"  

