# !/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


# 腾讯邮箱
mail_host = 'smtp.exmail.qq.com'
mail_user = 'appam@thecover.co'
mail_pass = 'F@Mf@m**2x2x2x'

sender = 'appam@thecover.co'
receiver = ['alex@thecover.co']
acc = ['alex@thecover.co']

msg = MIMEMultipart('related')

msg['to'] = 'alex@thecover.co'
msg['Cc'] = '120279687@qq.com'
msg['from'] = sender
msgAlternative = MIMEMultipart('alternative')
msg.attach(msgAlternative)


def cs_mail_send_image(m_subject, html, pic_l):

    # 读取图片
    for i in range(len(pic_l)):
        fp = open(pic_l[i], 'rb')
        msg_image = MIMEImage(fp.read())
        fp.close()
        msg_image.add_header('Content-ID', '<image' + str(i + 1) + '>')
        msg.attach(msg_image)

    subject = m_subject
    msg['Subject'] = Header(subject, 'utf-8')
    context = MIMEText(html, _subtype='html', _charset='utf-8')  # 解决乱码
    msg.attach(context)

    try:
        server = smtplib.SMTP()
        server.connect(mail_host, 25)  # 25 为 SMTP 端口号
        server.login(mail_user, mail_pass)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        return True
    except smtplib.SMTPException:
        return False


def cs_mail_send(m_subject, html):

    subject = m_subject
    msg['Subject'] = Header(subject, 'utf-8')
    context = MIMEText(html, _subtype='html', _charset='utf-8')  # 解决乱码
    msg.attach(context)

    try:
        server = smtplib.SMTP()
        server.connect(mail_host, 25)  # 25 为 SMTP 端口号
        server.login(mail_user, mail_pass)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        return True
    except smtplib.SMTPException:
        return False
#
# file_path = "image\\monitor\\robot\\"
# file_name = 'Monitor20170721185439244996.JPEG'
# mpn = file_path + file_name

# # 获取手机、app内存信息
# mt, mf, heap_size, heap_alloc, heap_free = fmxw_cs_cpi.cs_cpi()
# mt = str(mt)
# mf = str(mf)
# heap_size = str(heap_size)
# heap_alloc = str(heap_alloc)
# heap_free = str(heap_free)
#
# img = Image.open(mpn)
# im_resize = img.resize((360, 640))
# im_resize.save(mpn)
#
# # 读取图片
# fp = open(mpn, 'rb')
# msg_image = MIMEImage(fp.read())
# fp.close()
# msg_image.add_header('Content-ID', '<image1>')
# msg.attach(msg_image)
#
# # 发送邮件内容
# m_subject = 'APP自动化监控'
#
# # 构造html
# html = """\
# <html xmlns="http://www.w3.org/1999/xhtml">
# <head>
# <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
# <title>APP自动化监控</title>
# <body>
# <div id="container">
# <p><strong>监控到小冰机器人出现异常...</strong></p>
# <p>CPU、内存信息：</p>
# <p>MemTotal(手机内存)： """ + mt + """G</p>
# <p>MemFree(空闲内存): """ + mf + """G</p>
# <p>total_heap_size(系统分配App内存)： """ + heap_size + """M</p>
# <p>total_heap_alloc(App内存)： """ + heap_alloc + """M</p>
# <p>total_heap_free(App空闲内存): """ + heap_free + """M</p>
# <p><img src="cid:image1"></p>
# </div>
# </body>
# </html>
#       """
#
# try:
#     if cs_mail_sed(m_subject, html):
#         print('Send success')
#     else:
#         print('Send failure')
# except Exception as e:
#     raise e

