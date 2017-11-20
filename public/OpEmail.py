#! /usr/bin/env python
# -*- coding:UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import time
import os


def sent_mail(file_new):
    # 发信邮箱
    mail_from = 'fnngj@126.com'
    # 收信邮箱
    mail_to = '123456@qq.com'
    # 定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    # 定义标题
    msg['Subject'] = u"私有云测试报告"
    # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    # 连接SMTP 服务器，此处用的126的SMTP 服务器
    smtp.connect('smtp.126.com')
    # 用户名密码
    smtp.login('fnngj@126.com', '123456')
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print('email has send out !')

if __name__ == "__main__":
    result_dir = '..\\report'
    lists = os.listdir(result_dir)
    lists.sort(
        key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not os.path.isdir(result_dir + "\\" + fn) else 0
    )
    print(u'最新测试生成的报告： ' + lists[-1])
    # 找到最新生成的文件
    file_new = os.path.join(result_dir, lists[-1])
    print
    file_new
    # 调用发邮件模块
    sent_mail(file_new)