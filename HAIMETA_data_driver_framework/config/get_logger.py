import logging.config
import pathlib

def get_logger():
    file = pathlib.Path(__file__).parents[0] / 'log.conf.ini'
    print(file)
    logging.config.fileConfig(file, encoding="utf-8")
    # 获取fileLogger而不是root logger，这样可以确保日志被正确记录到文件
    logger = logging.getLogger('fileLogger')
    return logger


def get_driver():
    driver = pathlib.Path(__file__).parents[0] / r'D:\PycharmProjects\PythonProject\HAIMETA_data_driver_framework\config\chromedriver.exe'
    return driver