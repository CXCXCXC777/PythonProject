import time
import unittest
import json
import os

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Test(unittest.TestCase):
    # Login page locators
    EMAIL_INPUT_XPATH = "/html/body/div/div/div[3]/div/div/div/form/div[1]/div/input"
    CONTINUE_BUTTON_XPATH = "/html/body/div/div/div[3]/div/div/div/form/div[2]/button"
    PASSWORD_INPUT_XPATH = "/html/body/div/div/div[3]/div/div/div[1]/form/div[1]/div/div/input"
    LOGIN_BUTTON_XPATH = "/html/body/div/div/div[3]/div/div/div[1]/form/button"
    USER_DISPLAY_ClASS_NAME = "clip-path"
    
    # Third party login locators
    THIRD_PARTY_BUTTON_XPATH = "/html/body/div/div/div[3]/div/div/div/form/div[3]/div/div[2]/button"
    THIRD_PARTY_NEXT_BUTTON_XPATH = "/html/body/div/div/div[3]/div/div/div/button"
    
    # Privacy policy locators
    PRIVACY_POLICY_LINK_XPATH = "/html/body/div/div/div[3]/div/div/div/div[4]/div/div/span[2]"
    PRIVACY_POLICY_CHECK_MESSAGE = "/html/body/div/div/div/div/p[1]/span[37]"
    PRIVACY_POLICY_BACK_BUTTON = "/html/body/div/div/button"
    USER_SERVICE_PRIVACY_LINK_XPATH = "/html/body/div/div/div[3]/div/div/div/div[4]/div/div/span[1]"
    USER_SERVICE_PRIVACY_CHECK_MESSAGE = "/html/body/div/div/div/div/p[3]/span[44]"
    USER_SERVICE_BACK_BUTTON = "/html/body/div/div/button"
    ERROR_MESSAGE_ON_LOGIN_PAGE_XPATH = "/div/div/div/span[2]"
    
    # Home page locators
    GET_VERIFICATION_CODE_BUTTON_XPATH = "/html/body/div/div/div[3]/div/div/div[1]/div[2]"
    EDITION_ON_HOME_BUTTON_CLASS_NAME = "basic-item_child_text"
    PICTURE_EDITION_UPLOAD_BUTTON_ClASS_NAME = "ant-upload.ant-upload-btn"
    PICTURE_EDITION_UPLOAD_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/span/div/span/input"
    EDITION_TEXT_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]"
    
    # Language switch locators
    SWITCH_TO_ENGLISH_LANGUAGE = "/html/body/div[6]/div/div/div/div/div/div[1]/div/div[1]/i"
    SWITCH_TO_CHINESE_LANGUAGE = "/html/body/div[6]/div/div/div/div/div/div[2]/div/div[1]/i"
    
    # Test credentials
    VALID_EMAIL_ACCOUNT = "1974440719@qq.com"
    VALID_PASSWORD = "Tiejiayu666"
    
    # Configuration
    COOKIE_FILE = "cookies.json"
    LOGIN_URL = "https://test.haimeta.com/login"
    HOME_URL = "https://test.haimeta.com/"

    @classmethod
    def setUpClass(cls):
        """Initialize the test environment and perform login."""
        # 启动浏览器
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        cls.driver = webdriver.Chrome(options=options)
        cls.wait = WebDriverWait(cls.driver, 15)

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
        """执行真正的登录流程"""
        wait = cls.wait
        driver = cls.driver
        
        # 输入邮箱
        email_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, cls.EMAIL_INPUT_XPATH))
        )
        email_input.send_keys(cls.VALID_EMAIL_ACCOUNT)

        # 点击继续按钮
        driver.find_element(By.XPATH, cls.CONTINUE_BUTTON_XPATH).click()

        # 输入密码
        password_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, cls.PASSWORD_INPUT_XPATH))
        )
        password_input.clear()
        password_input.send_keys(cls.VALID_PASSWORD)

        # 点击登录按钮
        driver.find_element(By.XPATH, cls.LOGIN_BUTTON_XPATH).click()

        # 等待用户名元素出现
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, cls.USER_DISPLAY_ClASS_NAME))
        )
        print("登录成功！")

    @classmethod
    def save_cookies(cls):
        """将当前浏览器的 Cookie 保存到本地文件"""
        cookies = cls.driver.get_cookies()
        with open(cls.COOKIE_FILE, "w", encoding="utf-8") as f:
            json.dump(cookies, f, ensure_ascii=False, indent=2)
        print("Cookies 已保存到", cls.COOKIE_FILE)

    def test_login_with_email_password(self):
        """Test login functionality using email and password."""
        driver = self.driver
        wait = self.wait

        driver.get(self.LOGIN_URL)

        # 输入邮箱
        email_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT_XPATH))
        )
        email_input.send_keys(self.VALID_EMAIL_ACCOUNT)

        # 点击继续按钮
        next_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.CONTINUE_BUTTON_XPATH))
        )
        next_button.click()

        # 输入密码
        password_input = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.PASSWORD_INPUT_XPATH)
            )
        )
        password_input.send_keys(self.VALID_PASSWORD)

        # 点击登录按钮
        login_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON_XPATH))
        )
        login_button.click()

        # 首先定义元素，并等待其出现
        user_name_displayed = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, self.USER_DISPLAY_ClASS_NAME)
            )
        )

        # 然后再断言元素确实显示了
        self.assertTrue(user_name_displayed.is_displayed())
        print("邮箱密码登录成功！")

    def test_invalid_email_input(self):
        """测试用户输入超长错误邮箱后，是否出现错误提示，并阻止进入下一步"""
        driver = self.driver
        wait = self.wait

        # 重新进入登录页以便测试（假设项目允许随时访问登录页）
        driver.get(self.LOGIN_URL)

        invalid_email = "a" * 300 + "@invalid.com"  # 300个 'a' + @invalid.com
        email_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT_XPATH))
        )
        email_input.clear()
        email_input.send_keys(invalid_email)

        # 点击继续按钮
        next_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.CONTINUE_BUTTON_XPATH))
        )
        next_button.click()

        # 检查是否出现错误提示 (以CLASS_NAME为例，请根据实际弹窗定位进行调整)
        error_message = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "ant-message.ant-message-top.css-1vr7spz"))
        )
        self.assertIsNotNone(error_message, "错误邮箱输入后未显示错误提示！")

        # 检查是否仍停留在邮箱输入页面(判断密码输入是否出现)
        try:
            wait2 = WebDriverWait(driver, 3)
            _ = wait2.until(
                EC.presence_of_element_located((By.XPATH, self.PASSWORD_INPUT_XPATH))
            )
            self.fail("❌ 用户错误邮箱输入后却进入了密码输入界面，测试失败！")
        except TimeoutException:
            print("✅ 用户错误邮箱输入后未进入密码输入页面，符合预期。")

    def test_thirdparty_login(self):
        """测试第三方登录功能"""
        driver = self.driver
        wait = self.wait

        # 假设必须先访问登录页
        driver.get(self.LOGIN_URL)

        third_party_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.THIRD_PARTY_BUTTON_XPATH))
        )
        third_party_button.click()

        wait.until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])

        third_party_login_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.THIRD_PARTY_NEXT_BUTTON_XPATH))
        )
        third_party_login_button.click()

        self.assertIn("登录 - Google 账号", driver.title)
        print("✅ 第三方登录界面进入成功！")

    def test_privacy_policy(self):
        """测试隐私政策的查看与返回"""
        driver = self.driver
        wait = self.wait
        driver.get(self.LOGIN_URL)

        privacy_policy_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.PRIVACY_POLICY_LINK_XPATH))
        )
        privacy_policy_link.click()

        wait.until(EC.presence_of_element_located((By.XPATH, self.PRIVACY_POLICY_CHECK_MESSAGE)))
        Page_Message = driver.find_element(By.XPATH, "/html/body/div/div/div/div/p[1]/span[2]").text
        print("✅ 隐私政策页面成功打开！\n 页面展示内容:\n", Page_Message)

        driver.find_element(By.XPATH, self.PRIVACY_POLICY_BACK_BUTTON).click()
        print("✅ 已成功返回主界面")

    def test_user_service_privacy(self):
        """测试用户服务协议查看与返回"""
        driver = self.driver
        wait = self.wait
        driver.get(self.LOGIN_URL)

        user_service_privacy_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.USER_SERVICE_PRIVACY_LINK_XPATH))
        )
        user_service_privacy_link.click()

        wait.until(EC.presence_of_element_located((By.XPATH, self.USER_SERVICE_PRIVACY_CHECK_MESSAGE)))
        Page_Message = driver.find_element(By.XPATH, "/html/body/div/div/div/div/p[1]").text
        print("✅ 用户服务协议页面成功打开！\n 页面展示内容:\n", Page_Message)

        driver.find_element(By.XPATH, self.USER_SERVICE_BACK_BUTTON).click()
        print("✅ 已成功返回主界面")

    def test_invalid_email_format(self):
        """测试用户输入各种非邮箱格式时，是否出现错误提示，并阻止下一步"""
        driver = self.driver
        wait = self.wait
        driver.get(self.LOGIN_URL)

        invalid_emails = [
            "invalidemail.com",  # 缺少 @
            "invalid@com",       # 缺少 .
            "123456789",         # 纯数字
            "@invalid.com",      # 只包含 @
            "invalid@.com",      # @ 后面直接是 .
            "invalid@domain..com"
        ]

        for invalid_email in invalid_emails:
            print(f"\n🔍 正在测试非邮箱格式输入: {invalid_email}")
            email_input = wait.until(
                EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT_XPATH))
            )
            email_input.clear()
            email_input.send_keys(invalid_email)

            next_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, self.CONTINUE_BUTTON_XPATH))
            )
            next_button.click()

            # 检查错误提示
            try:
                error_message = wait.until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "error-text.global-font-body-small"))
                )
                self.assertIsNotNone(error_message, "❌ 非邮箱格式输入后未显示错误提示！")
                print(f"✅ 非邮箱 '{invalid_email}' 输入后，错误提示成功显示。")
            except TimeoutException:
                self.fail(f"❌ 非邮箱 '{invalid_email}' 输入后未出现错误提示，测试失败。")

            # 确保仍在邮箱输入页面
            try:
                wait2 = WebDriverWait(driver, 2)
                email_input_still_present = wait2.until(
                    EC.presence_of_element_located((By.XPATH, self.EMAIL_INPUT_XPATH))
                )
                self.assertIsNotNone(email_input_still_present, "❌ 错误邮箱输入后却进入了下一步，不符合预期。")
                print(f"✅ 非邮箱 '{invalid_email}' 输入后，未进入下一步，测试通过。")
            except TimeoutException:
                self.fail(f"❌ 非邮箱 '{invalid_email}' 输入后，页面跳转到下一步，测试失败。")

    def test_picture_Edition(self):

        driver = self.driver
        wait = self.wait
        driver.get(self.HOME_URL)
        edition_button_click = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.EDITION_ON_HOME_BUTTON_CLASS_NAME))
        )
        edition_button_click.click()
        all_tabs = driver.window_handles

        print(all_tabs)
        driver.switch_to.window(all_tabs[1])
        tab = driver.current_window_handle
        print(tab)

        self.perform_picture_edition_actions()
        # 界面下语言切换是否正常
        print("Switching to English language")
        driver.find_element(By.XPATH,self.SWITCH_TO_ENGLISH_LANGUAGE).click()
        try:
            check_language = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "default-box-title"))
            )
            if check_language.text =="Image Edit":
                print("Switch to English language successfully")
            else:
                print("Switch to English language unsuccessfully")
        except TimeoutException:
            print("Switch to English language Failed")

        print("Switching to Chinese Language")
        driver.find_element(By.XPATH,self.SWITCH_TO_CHINESE_LANGUAGE).click()
        try:
            check_language = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "default-box-title"))
            )
            if check_language.text =="图片编辑":
                print("Switch to Chinese language successfully")
            else:
                print("Switch to Chinese language unsuccessfully")
        except TimeoutException:
            print("Switch to Chinese language Failed")

        time.sleep(5)

    def perform_picture_edition_actions(self):
        driver = self.driver
        wait = self.wait
        upload_button = wait.until(
            EC.presence_of_element_located((By.XPATH, self.PICTURE_EDITION_UPLOAD_BUTTON_XPATH))
        )
        upload_button.send_keys(r'D:\PycharmProjects\PythonProject\TestUpload.png')

        HistoryCheck = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/div/i")
            )
        )
        HistoryCheck.click()
        HistoryCheck = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/div/i")
            )
        )
        HistoryCheck.click()
        HistoryListcheck=wait.until(
            EC.visibility_of_element_located(
                (By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]")
            )
        )

        driver.find_element(By.CLASS_NAME, "iconfont.ic_mouse.icon_style").click() #SelelctButtonUnderPE
        driver.find_element(By.CLASS_NAME,"iconfont.ic_drag_storke.icon_style").click()#MoveSpaceButtonCheck
        driver.switch_to.frame(driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/iframe"))
        actions = ActionChains(driver)

        actions.click_and_hold(driver.find_element(By.XPATH,"/html/body/flutter-view"))  # 点击并按住元素
        actions.move_by_offset(10,20)  # 移动到目标元素
        actions.move_by_offset(-10,-20)
        actions.pause(3)
        actions.release()  # 释放鼠标
        actions.perform()
        driver.switch_to.default_content()
        driver.find_element(By.CLASS_NAME,"iconfont.ic_text.icon_style").click()# Add Text Button Check
        driver.find_element(By.CLASS_NAME,"iconfont.ic_Stickers.icon_style").click()# Stickers Button Check

        driver.find_element(By.CLASS_NAME,"iconfont.ic_cancel.icon_style").click()# Undo button Check

        driver.find_element(By.CLASS_NAME,"iconfont.ic_regain.icon_style").click()# Redo Button Check

        driver.find_element(By.CLASS_NAME,"iconfont.ic_clean.icon_style").click()# Reset Button Check

        driver.find_element(By.CLASS_NAME,"download-btn").click()# Download Button Check

        driver.find_element(By.CLASS_NAME,"save-edit-image").click() # Save File Online Check

        try: #检查是否能够正常
            check_save = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "ant-tooltip-inner"))
            )
            if check_save.is_displayed():
                print("✅ 成功保存！")
            else:
                print("❌ 保存失败！")
        except TimeoutException:
            print("❌ 超时，保存失败！")

        driver

if __name__ == "__main__":
    unittest.main()
