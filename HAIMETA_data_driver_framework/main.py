import os
from HAIMETA_data_driver_framework.excel_driver.excel_driver import run, sum_info

if __name__ == '__main__':
    cases = []
    test_data_path = r'D:\PycharmProjects\PythonProject\HAIMETA_data_driver_framework\test_data'

    for path, dirs, files in os.walk(test_data_path):
        for file in files:
            file_name, file_ext = os.path.splitext(file)  # 分离文件名和扩展名
            if file_ext == '.xlsx' and '_hcc' not in file_name:
                # 添加完整的文件路径，包括扩展名
                full_path = os.path.join(test_data_path, file)
                cases.append(full_path)
            else:
                print(f'Current file is not a excel file: {file}')
    
    print(f"要执行的测试用例文件: {cases}")

    for case in cases:
        run(case)

    sum_info()