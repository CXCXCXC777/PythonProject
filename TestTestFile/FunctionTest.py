import json
import unittest
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FunctionTest(unittest.TestCase):
    BASE_URL = "https://test.haimeta.com"

    @classmethod
    def setUpClass(cls):
        # 初始化浏览器
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        cls.driver = webdriver.Chrome(options=options)
        cls.wait = WebDriverWait(cls.driver, 10)  # Increased wait time

        # 访问主页面，让浏览器能够识别当前站点（重要！）
        cls.driver.get(cls.BASE_URL)
        # 加载并注入已保存的 Cookies
        cls._load_cookies()

    @classmethod
    def _load_cookies(cls):
        """从 cookies.json 加载 cookies 并注入到浏览器"""
        try:
            with open("cookies.json", "r", encoding='utf-8') as file:
                cookies = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("cookies.json 文件不存在，请先运行 LoginTest.py 获取 Cookies")

        # 注入 Cookies 到浏览器
        for cookie in cookies:
            cls.driver.add_cookie(cookie)

        # 刷新页面，确保 Cookies 注入生效
        cls.driver.refresh()
        time.sleep(10)  # Wait to ensure page load

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.driver.quit()

    def test_function1(self):
        """测试已登录用户访问功能页面"""
        driver = self.driver
        wait = self.wait

        cookies = self.driver.get_cookies()
        print(cookies)  # Print cookies to ensure they are loaded

        # 访问需要登录才能访问的页面
        driver.get(self.BASE_URL + "/setting")

        try:
            # 增加等待机制，确保页面加载完成
            protected_content = wait.until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[5]/div/div/div/div[1]/div/form/div[1]/div/div/div/div/div/div[1]/div/div/div/div/div/div/span/div/span"))
            )
            self.assertTrue(protected_content.is_displayed())
            print("功能页面访问成功，内容可见。")
        except TimeoutException:
            print("加载页面超时，检查页面是否已经正确加载！")
            print(driver.page_source)  # Print the page source for debugging

    # def test_function2(self):
    #     """测试另一项功能：检查用户个人信息"""
    #     driver = self.driver
    #     wait = self.wait
    #
    #     driver.get(self.BASE_URL + "/pictureEditor/imageEdit")
    #     time.sleep(10)
    #
    #     try:
    #         # 等待直到个人信息加载完成
    #         profile_info = wait.until(
    #             EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]"))
    #         )
    #         self.assertTrue(profile_info.is_displayed())
    #         print("用户个人信息页面加载成功！")
    #     except TimeoutException:
    #         print("加载页面超时，检查页面是否正确加载！")
    #         print(driver.page_source)  # Print the page source for debugging

if __name__ == "__main__":
    unittest.main()
