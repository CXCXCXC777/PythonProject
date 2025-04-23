import os
from HAIMETA_data_driver_framework.excel_driver.excel_driver import run, sum_info

from HAIMETA_data_driver_framework.config.email_sender import EmailSender

if __name__ == '__main__':
    cases = []
    test_data_path = './test_data'

    for path, dirs, files in os.walk(test_data_path):
        for file in files:
            file_name, file_ext = os.path.splitext(file)  # 分离文件名和扩展名
            # 排除临时文件和特定标记的文件
            if file_ext == '.xlsx' and not file_name.startswith('~$'):
                if '_P' in file_name:
                    print(f'current file is pending: {file}')
                else:
                    # 添加完整的文件路径，包括扩展名
                    full_path = os.path.join(test_data_path, file)
                    cases.append(full_path)
            else:
                print(f'Current file is not a excel file: {file}')
    
    print(f"要执行的测试用例文件: {cases}")

    for case in cases:
        run(case)

    sum_info()

    # # 获取测试结果摘要
    # test_results = sum_info()

    # # 配置邮件发送
    # email_sender = EmailSender()
    # # 设置邮件配置（请替换为实际的邮箱信息）
    # email_sender.set_email_config(
    #     sender_email="volcanokdoething@163.com",  # 发件人邮箱
    #     sender_password="GTTUF33SZzR2qEAq",    # 发件人邮箱授权码
    #     receiver_email="tiejiayu@haimeta.com"  # 收件人邮箱
    # )
    #
    # # 发送测试报告
    # email_sender.send_report(test_results)