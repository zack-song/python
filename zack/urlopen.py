#用于处理从 urls 接收的数据的 urllib.request
from urllib.request import urlopen

for line in urlopen('http://m.jia.com/shanghai/'):
    print(line)

#用于发送电子邮件的 smtplib

# import smtplib
#
# server = smtplib.SMTP('localhost')
# server.sendmail('125009260@qq.com','ivan87528@163.com')
# server.quit()
