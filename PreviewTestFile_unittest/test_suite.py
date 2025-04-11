import unittest
import multiprocessing
from functools import partial
from BaseTest import BaseTest
from PreviewTestFile_unittest.BasicToolTest import Basic_Tool_Test
from SpecialToolTest import Special_Tool_Test
from Text2ImageToolTest import Text2Image_Test
from PhotoalbumTest import Photo_Album_Test

def run_test(test_case):
     # # 创建测试加载器
    # loader = unittest.TestLoader()
    # # 加载测试用例并添加到测试套件
    # # suite.addTest(loader.loadTestsFromTestCase(Text2Image_Test))
    # suite.addTests(loader.loadTestsFromTestCase(Photo_Album_Test))

    # 创建测试用例列表，指定要执行的测试方法
    """运行单个测试用例的函数"""
    suite = unittest.TestSuite()
    suite.addTest(test_case)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

def create_test_suite():
    # 创建测试用例列表
    test_cases = [
        Photo_Album_Test('test_id_photo'),
        Photo_Album_Test('test_chinese_aesthetics'),
        Photo_Album_Test('test_arabian_dreams'),
        Photo_Album_Test('test_nanyang_memory'),
        Photo_Album_Test('test_gorgeous_road'),
        Photo_Album_Test('test_east_asian_culture'),
        Photo_Album_Test('test_cyber_future'),
        Photo_Album_Test('test_fantasy_tales'),
        Photo_Album_Test('test_love_in_the_air'),
        Photo_Album_Test('test_BFF_moments'),
        Photo_Album_Test('test_bro_show')
    ]
    return test_cases

if __name__ == '__main__':
    # 设置并行进程数，可以根据CPU核心数和实际需求调整
    process_count = 4
    
    # 创建进程池
    with multiprocessing.Pool(processes=process_count) as pool:
        # 获取测试用例列表
        test_cases = create_test_suite()
        # 并行执行测试用例
        pool.map(run_test, test_cases)