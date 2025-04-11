import traceback
import openpyxl

from HAIMETA_data_driver_framework.config.get_logger import get_logger
from HAIMETA_data_driver_framework.excel_driver.excel_styles import pass_, fail_
from HAIMETA_data_driver_framework.web_keys.web_keys import WebKeys
from HAIMETA_data_driver_framework.config.element_config import ElementLocators

log= get_logger()

success=0
fail=0
failed_cases=[]

def arguments(data):
    temp_data = {}  # Changed from list to dictionary
    if data:
        str_temp = data.split(";")
        for temp in str_temp:
            t = temp.split("=", 1)
            if len(t) == 2:  # Make sure we have both key and value
                if t[1].startswith('self.'):
                    # 从ElementLocators类中获取对应的xpath值
                    attr_name = t[1].replace('self.', '')
                    if hasattr(ElementLocators, attr_name):
                        temp_data[t[0]] = getattr(ElementLocators, attr_name)
                else:
                    temp_data[t[0]] = t[1]
    return temp_data

def run(file_name):
    global success, fail, failed_cases
    try:
        # 读取excel
        excel = openpyxl.load_workbook(file_name)
        # 考虑多个sheet页面需要执行，所以获取全部sheet页面
        sheets = excel.sheetnames
        for name in sheets:
            sheet =excel[name]
            log.info(f'正在执行{name}测试用例')
            for values in sheet.values:
                if type(values[0]) is int :
                    test_data = arguments(values[2])
                    if values[1]=='open_browser':
                        wk=WebKeys(**test_data)
                    elif values[1]=='assert_text':
                        status=getattr(wk, values[1])(**test_data, expected=values[4])
                        if status:
                            pass_(sheet.cell(row=values[0]+2,column=6))
                            success += 1
                        else:
                            fail_(sheet.cell(row=values[0]+2,column=6))
                            fail += 1
                            failed_cases.append(file_name+':'+name)
                        excel.save(file_name)
                    else:
                        getattr(wk, values[1])(**test_data)
    except Exception as e:
        log.error(traceback.format_exc())
        fail += 1
        failed_cases.append(file_name+':'+name)
    finally:
        if 'excel' in locals():  # 确保 excel 变量已定义
            excel.close()


# 在测试结束后输出结果
def sum_info():
    log.warning(f'''
成功用例数：{success}条
失败用例数：{fail}条
失败用例具体情况如下：{failed_cases}
    
    ''')
    return f'''
成功用例数：{success}条
失败用例数：{fail}条
失败用例具体情况如下：{failed_cases}
'''
    