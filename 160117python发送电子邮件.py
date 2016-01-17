# coding:utf-8
import sys
# 发送邮件使用
import smtplib
from email.mime.text import MIMEText
# mail_host="smtp.163.com"  #设置服务器
# mail_user="zettage_wangx"    #用户名
# mail_pass="gopzbloojbfujxzb"   #口令 
# mail_postfix="163.com"  #发件箱的后缀
mail_host="smtp.mxhichina.com"
mail_user="register"
mail_pass="ZEttage321"
mail_postfix="zettage.com"
def send_confirm_mail(to_list,sub,random_string):  #to_list：收件人；sub：主题；content：邮件内容
    content = '''
    <div style="width:600px; height:240px;font-size:14px;">
        <div style="width:100%; height:235px; border-bottom:1px solid #8b8b8b;">
            <p style="margin-top:0;">亲爱的<a style="text-decoration:none;color:black;">用户</a>：</p>
            <p>感谢您在数据邦注册了账号，为了更好的为您提供服务，请点击下面的链接完成激活。</p>
            <a href="http://192.168.1.88/normal/email_confirm?code={random_string}" style="text-decoration:none;color:#06b0f3;">激活链接</a> <br />
            <p style="font-size:12px;">(如果邮箱中不能打开链接，您也可以将它复制到浏览器地址栏中打开)</p>
            <p>http://192.168.1.88/normal/email_confirm?code={random_string}</p>
            <h4 style="color:#0a4dc8;font-size:14px; text-align:center; margin-top:55px;">数据邦运营团队</h4>
        </div>
        
        <p style=" width:100%;text-align:center;">系统邮件，请勿回复</p>
    </div>
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
    except Exception as e:
        print(str(e))
        return False

if __name__ == '__main__':
    send_confirm_mail(['1846468966@qq.com'],'测试发送邮件','ewfw')
