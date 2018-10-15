# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 17:47:35 2018

@author: hany
"""

import smtplib  #加载smtplib模块
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

def auto_mail(att1path,att2path):
    my_sender='yishuitianhan1@163.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
    my_user='786670164@qq.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
    
    msg=MIMEMultipart('alternative')
    msg['From']=formataddr(["发件人邮箱昵称 from",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To']=formataddr(["收件人邮箱昵称 to",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject']="主题subject{}".format(datetime.today().date()) #邮件的主题，也可以说是标题
    
    # 构造附件1，传送当前目录下的 test.txt 文件
#    att1path = r'F:\Task\20180921 tanzhen_data_analysis\zhentan_xinyan_ltv_report.xlsx'
#    att2path = r'F:\Task\20180921 tanzhen_data_analysis\zhentan_xinyan_ltv_report.xlsx'
    
    att1 = MIMEText(open(att1path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Disposition"] = 'attachment; filename="test1.xlsx"'
    msg.attach(att1)
    
    att2 = MIMEText(open(att2path, 'rb').read(), 'base64', 'utf-8')
    att2["Content-Disposition"] = 'attachment; filename="test2.xlsx"'
    msg.attach(att2)
    
    server=smtplib.SMTP("smtp.163.com",25)  #发件人邮箱中的SMTP服务器，端口是25
    server.login(my_sender,"sqm123")    #括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(my_sender,[my_user],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()   #这句是关闭连接的意思
    
att1path = r'F:\Task\20180921 tanzhen_data_analysis\zhentan_xinyan_ltv_report.xlsx'
att2path = r'F:\Task\20180921 tanzhen_data_analysis\zhentan_xinyan_ltv_report.xlsx'
auto_mail(att1path,att2path)
