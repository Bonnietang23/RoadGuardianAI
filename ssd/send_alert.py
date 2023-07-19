#-*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message, smtp_server, smtp_port):
    # 创建邮件内容
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # 添加邮件正文
    msg.attach(MIMEText(message, 'plain'))

    try:
        # 登录到 SMTP 服务器
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # 发送邮件
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Mail sent successfully')

        # 关闭连接
        server.quit()
    except Exception as e:
        print('Email sending failed:', str(e))