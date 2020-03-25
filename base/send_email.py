#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class SendEmail:
    global send_user
    global email_host
    global password
    email_host = "smtp.mxhichina.com"
    send_user = "jinji.zhang@domi100.com"
    password = "Domi100.com"

    def send_mail(self,user_list,sub,content):
        user = "Domi"+"<"+send_user+">"
        message = MIMEMultipart()
        # 添加邮件标题、发件人、收件人
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        # 添加邮件内容
        content_part = MIMEText(content, _subtype='plain', _charset='utf-8')
        message.attach(content_part)
        # 添加邮件附件
        file_part = MIMEApplication(open('/Users/stina/Desktop/apitest.xls', 'rb').read())
        file_part.add_header('Content-Disposition', 'attachment', filename="apitest.xls")
        message.attach(file_part)
        # 发件服务器设置
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def send_main(self, pass_list, fail_list):
        pass_num = int(len(pass_list))
        fail_num = int(len(fail_list))
        count_num = pass_num+fail_num
        pass_result = "%.2f%%" % (pass_num/count_num*100)
        fail_result = "%.2f%%" % (fail_num/count_num*100)
        user_list = ['1055607469@qq.com', 'yuhe587853@163.com']
        sub = "Api接口自动化测试报告"
        content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" %(count_num, pass_num, fail_num, pass_result, fail_result )
        self.send_mail(user_list, sub, content)
