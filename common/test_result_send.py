import smtplib
from email.mime.text import MIMEText
from email.header import Header


class SendEmail:
    def sendtext(self,text):
        mail_host = "smtp.qq.com"
        mail_user = "*****@qq.com"
        mail_pass = "邮箱开启SMTP后的授权码"

        sender = 'from@runoob.com'
        receivers = ['*******@qq.com']

        message = MIMEText(text, 'plain', 'utf-8')
        message['From'] = Header("Demo", 'utf-8')
        message['To'] = Header("测试", 'utf-8')

        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")
