import time
import unittest
import json
from selenium import webdriver
from selenium.common import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BaseTest(unittest.TestCase):
    # 从Test_config导入所需的配置变量和常量
    from Preview_config import (
        LOGIN_URL, VALID_EMAIL_ACCOUNT, VALID_PASSWORD, COOKIE_FILE,
        USER_DISPLAY_ClASS_NAME, EMAIL_INPUT_XPATH, CONTINUE_BUTTON_XPATH,
        PASSWORD_INPUT_XPATH, LOGIN_BUTTON_XPATH, HOME_URL,
        LANGUAGE_SELECTION_CLASS_NAME
    )

    @classmethod
    def setUpClass(cls):
        """Initialize the test environment and perform login."""
        # 启动浏览器
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        cls.driver = webdriver.Chrome(options=options)
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.actions = ActionChains(cls.driver)

        # 首次访问页面（为了后面能加Cookie）
        cls.driver.get(cls.LOGIN_URL)
        cls.do_login()
        cls.save_cookies()

    @classmethod
    def tearDownClass(cls):
        """Clean up the test environment."""
        cls.driver.quit()

    @classmethod
    def is_logged_in(cls):
        """Check if user is currently logged in."""
        try:
            cls.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, cls.USER_DISPLAY_ClASS_NAME))
            )
            return True
        except TimeoutException:
            return False

    @classmethod
    def do_login(cls):
        """执行真正的登录流程，包含重试机制"""
        max_retries = 3
        retry_count = 0
        wait = cls.wait
        driver = cls.driver

        while retry_count < max_retries:
            try:
                # 输入邮箱
                email_input = wait.until(
                    EC.presence_of_element_located((By.XPATH, cls.EMAIL_INPUT_XPATH))
                )
                email_input.clear()
                email_input.send_keys(cls.VALID_EMAIL_ACCOUNT)
                time.sleep(1)  # 等待输入完成

                # 点击继续按钮
                continue_button = wait.until(
                    EC.element_to_be_clickable((By.XPATH, cls.CONTINUE_BUTTON_XPATH))
                )
                continue_button.click()
                time.sleep(2)  # 等待页面切换

                # 输入密码
                password_input = wait.until(
                    EC.presence_of_element_located((By.XPATH, cls.PASSWORD_INPUT_XPATH))
                )
                password_input.clear()
                password_input.send_keys(cls.VALID_PASSWORD)
                time.sleep(1)  # 等待输入完成

                # 点击登录按钮
                login_button = wait.until(
                    EC.element_to_be_clickable((By.XPATH, cls.LOGIN_BUTTON_XPATH))
                )
                login_button.click()
                time.sleep(2)  # 等待登录响应

                # 等待用户名元素出现
                wait.until(
                    EC.presence_of_element_located((By.CLASS_NAME, cls.USER_DISPLAY_ClASS_NAME))
                )
                print("登录成功！")
                return  # 登录成功，退出重试循环

            except (TimeoutException, ElementClickInterceptedException, StaleElementReferenceException) as e:
                retry_count += 1
                print(f"登录尝试 {retry_count}/{max_retries} 失败: {str(e)}")
                if retry_count < max_retries:
                    print("等待5秒后重试...")
                    time.sleep(5)
                    driver.refresh()
                else:
                    raise Exception(f"登录失败，已重试{max_retries}次: {str(e)}")

    @classmethod
    def save_cookies(cls):
        """将当前浏览器的 Cookie 保存到本地文件"""
        cookies = cls.driver.get_cookies()
        with open(cls.COOKIE_FILE, "w", encoding="utf-8") as f:
            json.dump(cookies, f, ensure_ascii=False, indent=2)
        print("Cookies 已保存到", cls.COOKIE_FILE)

    def switch_tab(self, driver, wait):
        """切换到新标签页"""
        # 获取所有窗口句柄
        handles = driver.window_handles
        # 切换到最新打开的标签页
        driver.switch_to.window(handles[-1])
        return handles[-1]

    def check_history(self):
        """检查历史记录"""
        try:
            self.wait.until(
                EC.invisibility_of_element_located(
                    (By.CLASS_NAME, "carousel-secondtip")
                )
            )
        except TimeoutException:
            print("等待历史记录加载超时")

    def switch_language(self, target_language, language_selection_class_name,
                       language_switch_xpath, expected_title_text,
                       expected_title_class_name="default-box-title"):
        """切换语言并验证"""
        # 点击语言选择按钮
        language_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, language_selection_class_name))
        )
        language_button.click()

        # 选择目标语言
        language_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, language_switch_xpath))
        )
        language_option.click()

        # 验证标题文本
        title = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, expected_title_class_name))
        )
        assert title.text == expected_title_text, f"语言切换失败：期望标题为 {expected_title_text}，实际为 {title.text}"