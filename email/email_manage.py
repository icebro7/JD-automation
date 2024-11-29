import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart


class EmailManage():
    def send_email(self,report_name):
        # 创建邮件服务器
        emailserver = 'smtp.qq.com'

        # 发送邮箱的账号密码
        username = '986807058@qq.com'
        password = 'gvszkzvtkknybdae'

        # 接收方
        receiver = '1915790282@qq.com'

        # 创建邮件对象
        message = MIMEMultipart('related')
        subject = '邮箱测试'
        fujian = MIMEText(open(report_name,'wb').read(),'html','utf-8')

        # 把邮件信息封装进邮件对象里
        message['from'] = username
        message['to'] = receiver
        message['subject'] = subject
        message.attach(fujian)

        # 登陆smtp服务器并发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(emailserver)
        smtp.login(username,password)
        smtp.sendmail(username,receiver,message.as_string())
        smtp.quit()

