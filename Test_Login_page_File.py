import unittest
import json
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTest(unittest.TestCase):

    EMAIL_INPUT_XPATH = "/html/body/div/div/div[3]/div/div/div/form/div[1]/div/input"
    CONTINUE_BUTTON_XPATH = "/html/body/div/div/div[3]/div/div/div/form/div[2]/button"
    PASSWORD_INPUT_XPATH = "/html/body/div/div/div[3]/div/div/div[1]/form/div[1]/div/div/input"
    LOGIN_BUTTON_XPATH = "/html/body/div/div/div[3]/div/div/div[1]/form/button"
    USER_DISPLAY_XPATH = "/html/body/div[1]/div/div[1]/div/div[1]/div/i"
    THIRD_PARTY_BUTTON_XPATH = "/html/body/div/div/div[3]/div/div/div/form/div[3]/div/div[2]/button"
    PRIVACY_POLICY_LINK_XPATH = "/html/body/div/div/div[3]/div/div/div/div[4]/div/div/span[2]"
    PRIVACY_POLICY_CHECK_MESSAGE="/html/body/div/div/div/div/p[1]/span[37]"
    PRIVACY_POLICY_BACK_BUTTON="/html/body/div/div/button"
    USER_SERVICE_PRIVACY_LINK_XPATH = "/html/body/div/div/div[3]/div/div/div/div[4]/div/div/span[1]"
    USER_SERVICE_PRIVACY_CHECK_MESSAGE="/html/body/div/div/div/div/p[3]/span[44]"
    USER_SERVICE_BACK_BUTTON="/html/body/div/div/button"
    ERROR_MESSAGE_ON_LOGIN_PAGE_XPATH="/div/div/div/span[2]"
    THIRD_PARTY_NEXT_BUTTON_XPATH="/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span"
    # 每次测试前运行一次，打开浏览器
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        # options.add_argument('--headless')  # 如需无界面运行
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.get("https://test.haimeta.com/login")

    # 测试结束后运行，关闭浏览器
    def tearDown(self):
        self.driver.quit()

    def save_cookies(self):
        """将当前的cookies保存到文件"""
        cookies = self.driver.get_cookies()
        with open("cookies.json", "w", encoding="utf-8") as file:
            json.dump(cookies, file)
        print("Cookies 已保存到 cookies.json 文件")

    # 测试用例1：测试邮箱密码登录功能,输入正确的邮箱账号和密码
    def test_login_with_email_password(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 输入邮箱
        email_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT_XPATH))
        )
        email_input.send_keys("1974440719@qq.com")

        # 点击继续按钮
        driver.find_element(By.XPATH, self.CONTINUE_BUTTON_XPATH).click()

        # 输入密码
        password_input = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.PASSWORD_INPUT_XPATH)
            )
        )
        password_input.send_keys("Tiejiayu666")

        # 点击登录按钮
        driver.find_element(By.XPATH, self.LOGIN_BUTTON_XPATH).click()

        # 首先定义元素，并等待其出现
        user_name_displayed = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.USER_DISPLAY_XPATH)
            )
        )

        # 然后再断言元素确实显示了
        self.assertTrue(user_name_displayed.is_displayed())
        print("邮箱密码登录成功！")
        self.save_cookies()

    #用例2：异常输入超长且没有测试资格的用户
    def test_invalid_email_input(self):
        # 测试用户输入超长错误邮箱后，是否出现错误提示，并阻止进入下一步
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # **输入超长错误邮箱**
        invalid_email = "a" * 300 + "@invalid.com"  # 300个 'a' + @invalid.com
        email_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT_XPATH))
        )
        email_input.clear()
        email_input.send_keys(invalid_email)

        # **点击继续按钮**
        next_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.CONTINUE_BUTTON_XPATH))
        )
        next_button.click()

        # **检查是否出现错误提示**
        error_message = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "ant-message.ant-message-top.css-1vr7spz"))
        )
        # **检查用户是否仍然停留在邮箱输入页面**
        try:
            wait=WebDriverWait(driver, 3)
            email_input_still_present = wait.until(
                EC.presence_of_element_located((By.XPATH, self.PASSWORD_INPUT_XPATH))
            )
            self.fail("❌ 用户错误邮箱输入后仍然进入了密码输入界面！测试失败！")
        except TimeoutException:
            print("✅ 用户错误邮箱输入后未进入密码输入界面，符合预期！")
        print("✅ 输入超长无效邮箱后，未进入下一步，测试通过！")

    # 测试用例3：测试第三方登录，能够进入第三方界面
    def test_thirdparty_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        third_party_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.THIRD_PARTY_BUTTON_XPATH))
        )
        third_party_button.click()

        wait.until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])

        third_party_login_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, self.THIRD_PARTY_NEXT_BUTTON_XPATH)
            )
        )
        third_party_login_button.click()

        self.assertIn("登录 - Google 账号", driver.title)
        print("第三方登录成功！")

    # 测试用例4：测试隐私界面，能够正常进入该界面然后回到主界面
    def test_privacy_policy(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        privacy_policy_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.PRIVACY_POLICY_LINK_XPATH))
        )
        privacy_policy_link.click()

        wait.until(EC.presence_of_element_located((By.XPATH, self.PRIVACY_POLICY_CHECK_MESSAGE)))
        Page_Message=driver.find_element(By.XPATH, "/html/body/div/div/div/div/p[1]/span[2]").text
        print("✅ 隐私政策页面成功打开！\n 打印页面出现内容:\n "+Page_Message)
        driver.find_element(By.XPATH, self.PRIVACY_POLICY_BACK_BUTTON).click()
        print("并且成功返回主界面")

    # 测试用例5：用户协议界面进入测试，能够正常进入该界面然后回到主界面
    def test_user_service_privacy(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # 进入用户服务协议页面（保持等待）
        user_service_privacy_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.USER_SERVICE_PRIVACY_LINK_XPATH))
        )
        user_service_privacy_link.click()

        wait.until(EC.presence_of_element_located((By.XPATH, self.USER_SERVICE_PRIVACY_CHECK_MESSAGE)))
        Page_Message=driver.find_element(By.XPATH, "/html/body/div/div/div/div/p[1]").text
        print("用户服务协议页面打开成功！\n 打印页面出现内容\n "+Page_Message)

        # 直接点击返回按钮（不等待元素可点击）
        driver.find_element(By.XPATH, self.USER_SERVICE_BACK_BUTTON).click()
        print("并且成功返回主界面")

    def test_invalid_email_format(self):
        """
        测试用户输入非邮箱格式时，是否出现错误提示，并阻止进入下一步
        """
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # **测试的非邮箱格式**
        invalid_emails = [
            "invalidemail.com",  # 缺少 @
            "invalid@com",  # 缺少 .
            "123456789",  # 纯数字
            "@invalid.com",  # 只包含 @
            "invalid@.com",  # @ 后面直接是 .
            "invalid@domain..com"  # 连续两个点
        ]

        for invalid_email in invalid_emails:
            print(f"🔍 正在测试非邮箱格式输入: {invalid_email}")

            # **输入错误邮箱**
            email_input = wait.until(
                EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT_XPATH))
            )
            email_input.clear()
            email_input.send_keys(invalid_email)

            # **点击继续按钮**
            next_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, self.CONTINUE_BUTTON_XPATH))
            )
            next_button.click()

            # **检查是否出现错误提示**
            try:
                error_message = wait.until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "error-text.global-font-body-small"))
                )
                self.assertIsNotNone(error_message, "❌ 非邮箱格式输入后未显示错误提示！")
                print(f"✅ 非邮箱格式输入 '{invalid_email}' 后，错误提示成功显示！")
            except TimeoutException:
                self.fail(f"❌ 非邮箱格式输入 '{invalid_email}' 后，未出现错误提示，测试失败！")

            # **确保用户仍然停留在邮箱输入界面**
            try:
                email_input_still_present = wait.until(
                    EC.presence_of_element_located((By.XPATH, self.EMAIL_INPUT_XPATH))
                )
                self.assertIsNotNone(email_input_still_present, "❌ 用户错误邮箱输入后仍然进入了下一步，不符合预期！")
                print(f"✅ 非邮箱格式输入 '{invalid_email}' 后，未进入下一步，测试通过！")
            except TimeoutException:
                self.fail(f"❌ 非邮箱格式输入 '{invalid_email}' 后，系统跳转到了下一步，测试失败！")

    # def test_login_By_Captcha(self):
    #     wait = WebDriverWait(driver, 20)
    #
    #     # 输入邮箱
    #     email_input = wait.until(
    #         EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT_XPATH))
    #     )
    #     email_input.send_keys("1974440719@qq.com")
    #
    #     # 点击继续按钮
    #     driver.find_element(By.XPATH, self.CONTINUE_BUTTON_XPATH).click()
    #
    #     # 输入密码
    #     password_input = wait.until(
    #         EC.visibility_of_element_located(
    #             (By.XPATH, self.PASSWORD_INPUT_XPATH)
    #         )
    #     )
    #     password_input.send_keys("Tiejiayu666")
    #
    #     # 点击登录按钮
    #     # driver.find_element(By.XPATH, self.LOGIN_BUTTON_XPATH).click()
    #     # 等待登录按钮可点击后点击
    #     login_button = wait.until(
    #         EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON_XPATH))
    #     )
    #     login_button.click()
    #     # 首先定义元素，并等待其出现
    #     user_name_displayed = wait.until(
    #         EC.visibility_of_element_located(
    #             (By.XPATH, self.USER_DISPLAY_XPATH)
    #         )
    #     )
    #     # 然后再断言元素确实显示了
    #     self.assertTrue(user_name_displayed.is_displayed())
    #     print("邮箱密码登录成功！")



# 执行所有测试
if __name__ == "__main__":
    unittest.main()
