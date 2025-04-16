import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import datetime
import ssl


class EmailSender:
    def __init__(self):
        # SMTP服务器配置
        self.smtp_server = "smtp.163.com"  # 使用163邮箱的SMTP服务器
        self.smtp_port = 465  # SMTP SSL端口
        self.sender_email = ""  # 发件人邮箱
        self.sender_password = ""  # 发件人邮箱授权码（请在163邮箱设置中开启SMTP服务并获取授权码）
        self.receiver_email = ""  # 收件人邮箱

    def set_email_config(self, sender_email, sender_password, receiver_email):
        """设置邮件配置信息"""
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email = receiver_email

    def create_test_report(self, test_results):
        """创建测试报告内容"""
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 创建邮件正文
        email_content = f"""\n测试报告
执行时间：{current_time}

测试结果摘要：
{test_results}
"""
        
        return email_content

    def send_report(self, test_results, max_retries=3, retry_delay=5):
        """发送测试报告邮件
        Args:
            test_results: 测试结果
            max_retries: 最大重试次数
            retry_delay: 重试间隔（秒）
        """
        if not all([self.sender_email, self.sender_password, self.receiver_email]):
            raise ValueError("邮件配置信息不完整，请先设置邮件配置")

        # 创建邮件对象
        message = MIMEMultipart()
        message['From'] = Header(self.sender_email)
        message['To'] = Header(self.receiver_email)
        message['Subject'] = Header(f'自动化测试报告 - {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 'utf-8')

        # 添加邮件正文
        content = self.create_test_report(test_results)
        message.attach(MIMEText(content, 'plain', 'utf-8'))

        for attempt in range(max_retries):
            try:
                # 连接SMTP服务器并发送邮件
                context = ssl.create_default_context()
                smtp = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=context, timeout=30)  # 使用SSL连接
                smtp.login(self.sender_email, self.sender_password)
                smtp.sendmail(self.sender_email, [self.receiver_email], message.as_string())
                smtp.quit()
                print("测试报告邮件发送成功！")
                return True
            except smtplib.SMTPServerDisconnected as e:
                print(f"SMTP服务器连接断开 (尝试 {attempt + 1}/{max_retries}): {str(e)}")
            except smtplib.SMTPAuthenticationError as e:
                print(f"SMTP认证错误: {str(e)}")
                print("请确保：\n1. 已在163邮箱设置中开启SMTP服务\n2. 使用正确的授权码（不是邮箱密码）\n3. 发件人邮箱地址正确")
                return False  # 认证错误不需要重试
            except Exception as e:
                print(f"发送邮件时发生错误 (尝试 {attempt + 1}/{max_retries}): {str(e)}")
            
            if attempt < max_retries - 1:
                import time
                time.sleep(retry_delay)

        print(f"发送邮件失败: 已达到最大重试次数 {max_retries}")
        return False