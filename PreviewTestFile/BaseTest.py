# from os import wait
import time
import unittest
import json
from selenium import webdriver
from selenium.common import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import service
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
        EDITION_ON_HOME_BUTTON_XPATH, PICTURE_EDITION_UPLOAD_BUTTON_XPATH,
        LANGUAGE_SELECTION_CLASS_NAME, SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_PE,
        SWITCH_TO_CHINESE_LANGUAGE_PE_HOME_XPATH, BG_REMOVER_ON_HOME_BUTTON_XPATH,
        BG_REMOVER_UPLOAD_BUTTON_XPATH, SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_AI_CUT,
        SWITCH_TO_CHINESE_LANGUAGE_XPATH_ON_AI_CUT_HOME, SMART_ERASER_ON_HOME_BUTTON_XPATH,
        SMART_ERASER_UPLOAD_BUTTON_XPATH, SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_SE,
        SWITCH_TO_CHINESE_LANGUAGE_XPATH_ON_SE_HOME, HD_ENLARGE_ON_HOME_BUTTON_XPATH,
        HD_ENLARGE_UPLOAD_BUTTON_XPATH, TWO_TIMES_ENLARGE_BUTTON_XPATH,
        FOUR_TIMES_ENLARGE_BUTTON_XPATH, ENLARGE_BUTTON_XPATH,
        HD_REPAIR_ON_HOME_BUTTON_XPATH, HD_REPAIR_UPLOAD_BUTTON_XPATH,
        HD_REPAIR_BUTTON_XPATH, BUY_HAIBIT_BUTTON_ON_PE_XPATH,
        PURCHASE_HAIBIT_ON_BILLING_HISTORY, HAIBIT_PURCHASE_SELECTION_XPATH,
        COMFIRM_PAYMENT_IN_PURCHASE_HAIBIT_XPATH, PURCHASE_HAIBIT_INPUT_CARD_NUMBER_XPATH,
        PURCHASE_HAIBIT_INPUT_CARD_AVAILABLE_XPATH, PURCHASE_HAIBIT_INPUT_CARD_SECURE_NUMBER_XPATH,
        PURCHASE_HAIBIT_PAY_NOW_BUTTON_id, CREATE_AS_YOU_LIKE_UNDER_BUZZ_BUTTON_XPATH, 
        GENERATE_BUTTON_CLASS_NAME, INPUT_PROMPT_BOX_CLASS_NAME, REFINE_YOUR_IDEA_BUTTON_XPATH,
        SIZE_OF_GENERATION_BUTTON_XPATH, NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH,
        INTERACTED_IMAGE_1_XPATH, DOWNLOAD_BUTTON_XPATH_CAYL_AND_SINGLE_PHOTO_ABLUM, PUBLISH_BUTTON_XPATH_CAYL, PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_CAYL,
        TITLE_INPUT_XPATH, DESCRIPTION_INPUT_XPATH, CONFIRM_PUBLISH_BUTTON_XPATH, CANCEL_PUBLISH_BUTTON_XPATH_CAYL,
        PUBLISH_ON_STYLE_LIBRARY_BUTTON_XPATH, STYLE_NAME_INPUT_XPATH, AGREE_TERMS_BUTTON_XPATH,
        PUBLISH_ON_STYLE_LIBRARY_CONFIRM_BUTTON_XPATH, DOWNLOAD_BUTTON_XPATH_ID_PHOTO,
        REPORT_BUTTON_XPATH_CAYL, REPORT_TYPE_BUTTON_XPATH, REPORT_REASON_INPUT_XPATH, CONFIRM_REPORT_BUTTON_XPATH,
        REPORT_BUTTON_AFTER_PUBLISH_ON_STYLE_LIBRARY_XPATH,
        SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_CREATE_AS_U_LIKE, SWITCH_TO_CHINESE_LANGUAGE_XPATH_UNDER_CREATE_AS_U_LIKE,
        CHOOSE_PHOTO_GENERATION_STYLE_XPATH, THREE_DOTS_BUTTON_XPATH_CAYL,
        TEST_MALE_PHOTO, TEST_FEMALE_PHOTO, CONFIRM_DELETE_BUTTON_XPATH, PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,
        ID_PHOTO_IFRAME_XPATH, ITEM_TO_BE_INTERACTED_XPATH_ID,
        PHOTO_ALBUM_SECTION_BUTTON_XPATH, ID_PHOTO_BUTTON_XPATH, INPUT_SKIN_TEXTURE_ID_PHOTO_XPATH, CREATE_BUTTON_XPATH,
        PUBLISH_BUTTON_XPATH_ID_PHOTO, THREE_DOTS_BUTTON_XPATH_ID_PHOTO, PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_ID_PHOTO,
        CANCEL_PUBLISH_BUTTON_XPATH_ID_PHOTO, SET_SIZE_BUTTON_XPATH, INS_SIZE_BUTTON_XPATH, SET_LAYOUT_BUTTON_XPATH, FIVE_INCHES_LAYOUT_BUTTON_XPATH,
        EDITED_LAYOUT_PHOTO_LOCATION_XPATH, DOWNLOAD_EDITED_LAYOUT_PHOTO_BUTTON_XPATH, DELETE_BUTTON_XPATH_ID_PHOTO,
        SECOND_ITEM_SELECTED_XPATH, SINGLE_LAYOUT_BUTTON_XPATH,
        INPUT_SKIN_TEXTURE_SINGLE_PHOTO_ALBUM, NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_PHOTO_ALBUM,
        PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_SINGLE_PHOTO_ALBUM, CANCEL_PUBLISH_BUTTON_XPATH_SINGLE_PHOTO_ALBUM,
        THREE_DOTS_BUTTON_XPATH_SINGLE_PHOTO_ALBUM, DELETE_BUTTON_XPATH_SINGLE_PHOTO_ALBUM, PUBLISH_BUTTON_XPATH_SINGLE_PHOTO_ALBUM, ARABIAN_DREAMS_BUTTON_XPATH,
        NANYANG_MEMORY_UNDER_LIFE_BUTTON_XPATH, EAST_ASIAN_CULTURE_UNDER_LIFE_BUTTON_XPATH, CYBER_FUTURE_UNDER_LIFE_BUTTON_XPATH,
        GORGEOUS_ROAD_UNDER_LIFE_BUTTON_XPATH, FANTASY_TALES_UNDER_LIFE_BUTTON_XPATH, CHINESE_AESTHETICS_UNDER_LIFE_BUTTON_XPATH,
        REPORT_BUTTON_XPATH_ID_PHOTO_SINGLE_PHOTO_ALBUM, FIRST_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM, SECOND_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM,
        LOVE_IN_THE_AIR_BUTTON_UNDER_LIFE_BUTTON_XPATH, BFF_MOMENT_BUTTON_UNDER_LIFE_BUTTON_XPATH,
        BRO_SHOW_BUTTON_UNDER_LIFE_BUTTON_XPATH, TEST_IMAGE, DOWNLOAD_PATTERN_BUTTON_XPATH, ADD_NEW_IMAGE_BUTTON_XPATH, INTERACTED_IMAGE_2_XPATH,
        UPLOAD_IMAGE_CREATE_CLOTHES_XPATH, 
        WORK_SECTION_BUTTON_XPATH, CREATE_CLOTHES_BUTTON_UNDER_WORK_SECTION, REPORT_BUTTON_CREATE_CLOTHES_XPATH,
        PET_IMAGE_DATA_SET, PET_SECTION_BUTTON_XPATH, STYLE_YOUR_PET_ON_HOME_UNDER_PET_SECTION_XPATH, START_TRAINING_BUTTON_XPATH,
        CREATE_BUTTON_XPATH_STYLE_YOUR_PET, ADD_PET_DATA_SET_BUTTON_XPATH, UPLOAD_IMAGE_STYLE_YOUR_PET_XPATH,
        STYLE_CHOICE_BUTTON_XPATH, CREATE_BUTTON_XPATH_T2I, THREE_DOTS_BUTTON_XPATH_T2I, REPORT_BUTTON_XPATH_T2I, CANCEL_PUBLISH_BUTTON_XPATH_T2I,
        DELETE_BUTTON_XPATH_T2I, CREATE_NAIL_ART_BUTTON_UNDER_WORK_SECTION_XPATH, ART_SECTION_BUTTON_XPATH,
        CREATE_TATTOO_BUTTON_UNDER_WORK_SECTION_XPATH, CREATE_TOY_BUTTON_UNDER_WORK_SECTION_XPATH,
        CREATE_LOGO_BUTTON_UNDER_WORK_SECTION_XPATH, ME_TIME_BUTTON_UNDER_WORK_SECTION_XPATH,
        CREATE_CHARACTER_BUTTON_UNDER_WORK_SECTION_XPATH, STOCK_IMAGE_BUTTON_UNDER_WORK_SECTION_XPATH,
        TEXTURE_LABEL_BUTTON_UNDER_ART_SECTION_XPATH, PATTERN_BUTTON_UNDER_ART_SECTION_XPATH, STYLE_BUTTON_UNDER_ART_SECTION_XPATH,
        CREATE_WALLPAPER_BUTTON_UNDER_ART_SECTION_XPATH, TRENDY_ART_BUTTON_UNDER_ART_SECTION_XPATH,
        CHARACTER_TEXTURE_BUTTON_UNDER_WORK_SECTION_XPATH, STYLE_CHOICE_BUTTON_XPATH_T2I_WITHE_REFINING,
        SIZE_OF_GENERATION_BUTTON_XPATH_T2I_WITHE_REFINING, NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_T2I_WITHE_REFINING,
        PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_T2I_WITHE_REFINING, CANCEL_PUBLISH_BUTTON_XPATH_T2I_WITHE_REFINING,
        PUBLISH_BUTTON_XPATH_T2I_WITHE_REFINING, UPLOAD_IMAGE_BUTTON_XPATH_I2I,
        TEST_IP_IMAGE, TEST_PRODUCT_IMAGE, TEST_SKETCH_IMAGE, DOWNLOAD_BUTTON_XPATH_I2I, CREATE_BUTTON_XPATH_I2I,
        NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_I2I, SIZE_OF_GENERATION_BUTTON_XPATH_I2I, STYLE_CHOICE_BUTTON_XPATH_I2I,
        CHARACTER_PORTRAIT_STUDIO_BUTTON_UNDER_WORK_SECTION_XPATH, PUBLISH_BUTTON_XPATH_I2I, PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_I2I,
        CANCEL_PUBLISH_BUTTON_XPATH_I2I, THREE_DOTS_BUTTON_XPATH_I2I, REPORT_BUTTON_XPATH_I2I,
        DELETE_BUTTON_XPATH_I2I, CREATE_PRODUCT_UNDER_WORK_BUTTON_XPATH, RENDERING_RESULT_XPATH_I2I,
        STYLE_CHOICE_BUTTON_XPATH_I2I_TEXTURE_TRANSFER, PERSONAL_AVATAR_BUTTON_UNDER_ART_SECTION_XPATH,
        NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_I2I_PERSONAL_AVATAR, CHARACTER_STICKERS_UNDER_ART_BUTTON_XPATH,
        BUZZ_SECTION_BUTTON_XPATH,DREAM_HOME_DESIGN_UNDER_BUZZ_SECTION_XPATH,TEST_HOME_DESIGN_IMAGE,STYLE_CHOICE_BUTTON_XPATH_I2I_HOME_DESIGN,
        NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_I2I_HOME_DESIGN,SIZE_OF_GENERATION_BUTTON_XPATH_T2I,NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_T2I
    )



    @classmethod
    def setUpClass(cls):
        """Initialize the test environment and perform login."""
        # 启动浏览器
        service=Service(r'D:\PycharmProjects\PythonProject\chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument(r'--user-data-dir=E:\User Data') #加载本地文件
        options.add_experimental_option('excludeSwitches',["enable-logging","enable-automation"])
        cls.driver = webdriver.Chrome(service=service,options=options)
        cls.wait = WebDriverWait(cls.driver, 15)  # 增加默认等待时间
        cls.actions = ActionChains(cls.driver)
        
        # 先访问首页检查是否已登录
        cls.driver.get(cls.HOME_URL)
        try:
            if cls.is_logged_in():
                print("用户已登录，跳过登录步骤")
                return
        except TimeoutException:
            print("用户未登录，执行登录流程")
            
        # 执行登录流程
        max_retries = 3
        retry_count = 0
        while retry_count < max_retries:
            try:
                cls.driver.get(cls.LOGIN_URL)
                cls.do_login()
                if cls.is_logged_in():
                    print("登录成功")
                    return
            except Exception as e:
                retry_count += 1
                if retry_count < max_retries:
                    print(f"登录尝试 {retry_count}/{max_retries} 失败: {str(e)}，等待后重试...")
                    time.sleep(5)
                else:
                    raise Exception(f"登录失败，已重试{max_retries}次: {str(e)}")

    @classmethod
    def do_login(cls):
        """执行登录流程，使用显式等待替代固定时间等待"""
        wait = cls.wait
        driver = cls.driver

        try:
            # 等待页面加载完成
            wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
            
            # 等待邮箱输入框可见并可交互
            email_input = wait.until(
                EC.presence_of_element_located((By.XPATH, cls.EMAIL_INPUT_XPATH))
            )
            wait.until(EC.element_to_be_clickable((By.XPATH, cls.EMAIL_INPUT_XPATH)))
            email_input.clear()
            email_input.send_keys(cls.VALID_EMAIL_ACCOUNT)
            
            # 等待继续按钮可点击并点击
            continue_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, cls.CONTINUE_BUTTON_XPATH))
            )
            continue_button.click()
            
            # 等待密码输入框出现并可交互
            wait.until(EC.visibility_of_element_located((By.XPATH, cls.PASSWORD_INPUT_XPATH)))
            password_input = wait.until(
                EC.presence_of_element_located((By.XPATH, cls.PASSWORD_INPUT_XPATH))
            )
            wait.until(EC.element_to_be_clickable((By.XPATH, cls.PASSWORD_INPUT_XPATH)))
            password_input.clear()
            password_input.send_keys(cls.VALID_PASSWORD)
            
            # 等待登录按钮可点击并点击
            login_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, cls.LOGIN_BUTTON_XPATH))
            )
            login_button.click()
            
            # 等待登录成功标志
            wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, cls.USER_DISPLAY_ClASS_NAME)),
                "登录成功标志未出现"
            )
        except Exception as e:
            print(f"登录过程出错: {str(e)}")
            raise

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


    def switch_language(self, target_language="en", language_selection_class_name=None, language_switch_xpath=None, expected_title_text=None, expected_title_class_name=None):

        driver = self.driver
        wait = self.wait
        
        print(f"Switching to {target_language} language")
        try:
            # 检查参数是否为None
            if language_selection_class_name is None or language_switch_xpath is None:
                print(f"Error: language_selection_class_name or language_switch_xpath is None")
                return False
            # Wait for and click language selection button
            wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, language_selection_class_name))
            )
            ActionChains(driver).move_to_element(
                driver.find_element(By.CLASS_NAME, language_selection_class_name)
            ).perform()
            
            # Wait for and click specific language option
            self.click_action_check_by_element_to_be_clickable(language_switch_xpath)
            
            # Verify language switch
            check_language = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, str(expected_title_class_name))) if expected_title_class_name is not None else EC.visibility_of_element_located((By.CLASS_NAME, "default-box-title"))
            )
            # 检查expected_title_text是否为None
            if expected_title_text is None:
                print(f"Warning: expected_title_text is None, cannot verify language switch")
                return True  # 无法验证，默认返回成功
            elif check_language.text == expected_title_text:
                print(f"Switch to {target_language} language successfully")
                return True
            else:
                print(f"Switch to {target_language} language unsuccessfully")
                return False
        except TimeoutException:
            print(f"Switch to {target_language} language Failed")
            return False
    def check_history(self):
        """检查历史记录按钮和列表"""
        wait = self.wait
        HistoryCheck = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "collapse-btn")  # CHECK HISTORY BUTTON
            )
        )
        HistoryCheck.click()
        HistoryCheck_list = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]")  # HISTORY LIST
            )
        ).is_displayed()
        return HistoryCheck_list


    def perform_click_and_check_tab(self, element, max_retries=3):
        """点击元素并检查是否出现新标签页，如果失败则重试
        Args:
            element: 要点击的元素
            max_retries: 最大重试次数
        Returns:
            bool: 是否成功打开新标签页
        """
        retry_count = 0
        initial_handles = len(self.driver.window_handles)
        
        while retry_count < max_retries:
            try:
                self.actions.move_to_element(element).click().perform()
                # 等待新标签页出现
                self.wait.until(lambda driver: len(driver.window_handles) > initial_handles)
                # 切换到新标签页
                self.driver.switch_to.window(self.driver.window_handles[-1])
                return True
            except Exception as e:
                retry_count += 1
                if retry_count == max_retries:
                    print(f"Failed to open new tab after {max_retries} attempts: {str(e)}")
                    return False
                time.sleep(2)


    def switch_tab(self, driver, wait):
        max_retries = 3
        retry_count = 0
        while retry_count < max_retries:
            try:
                # 等待新标签页出现
                wait.until(lambda driver: len(driver.window_handles) > 1)
                all_tabs = driver.window_handles
                # 切换到最新打开的标签页
                driver.switch_to.window(all_tabs[-1])
                return driver.current_window_handle
            except Exception as e:
                retry_count += 1
                if retry_count == max_retries:
                    raise Exception(f"Failed to switch to new tab after {max_retries} retries: {str(e)}")
                time.sleep(2)



    def TOP_UP_ON_PE_actions(self):
        driver = self.driver
        wait = self.wait

        # 测试充值界面跳转
        self.click_action_check_by_visibility(self.BUY_HAIBIT_BUTTON_ON_PE_XPATH)
        self.click_action_check_by_visibility(self.PURCHASE_HAIBIT_ON_BILLING_HISTORY)
        self.click_action_check_by_visibility(self.HAIBIT_PURCHASE_SELECTION_XPATH)

        self.click_action_check_by_visibility(self.COMFIRM_PAYMENT_IN_PURCHASE_HAIBIT_XPATH)

        wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div/div[5]/div[2]/div[1]/form/div/div/iframe")))
        driver.switch_to.frame(driver.find_element(By.XPATH,"/html/body/div[1]/div/div[5]/div[2]/div[1]/form/div/div/iframe"))
        
        self.switch_frame_by_xpath("/html/body/div[1]/div/div[5]/div[2]/div[1]/form/div/div/iframe")

        input_card_number=wait.until(EC.visibility_of_element_located((By.XPATH,self.PURCHASE_HAIBIT_INPUT_CARD_NUMBER_XPATH)))
        ActionChains(driver).double_click(driver.find_element(By.XPATH, self.PURCHASE_HAIBIT_INPUT_CARD_NUMBER_XPATH)).perform()
        input_card_number.send_keys("4242 4242 4242 4242")
        ActionChains(driver).double_click(driver.find_element(By.XPATH, self.PURCHASE_HAIBIT_INPUT_CARD_AVAILABLE_XPATH)).perform()
        driver.find_element(By.XPATH,self.PURCHASE_HAIBIT_INPUT_CARD_AVAILABLE_XPATH).send_keys("04 / 52")
        ActionChains(driver).double_click(driver.find_element(By.XPATH, self.PURCHASE_HAIBIT_INPUT_CARD_SECURE_NUMBER_XPATH)).perform()
        driver.find_element(By.XPATH,self.PURCHASE_HAIBIT_INPUT_CARD_SECURE_NUMBER_XPATH).send_keys("245")
        wait.until(EC.visibility_of_element_located((By.ID,self.PURCHASE_HAIBIT_PAY_NOW_BUTTON_id)))
        driver.find_element(By.ID,self.PURCHASE_HAIBIT_PAY_NOW_BUTTON_id).click()
        try:
            payment_feedback = wait.until(
                EC.visibility_of_element_located((By.XPATH,"/html/body/div[7]/div/div/div/span"))
            )
            if payment_feedback.text=="支付成功":
                print("Payment Successful")
            else:
                print("Payment Failed")
        except TimeoutException:
            print("No feedback found")

        driver.switch_to.default_content()
    def delete_history_item(self, item_xpath):
        """删除历史记录中的指定项目
        Args:
            item_xpath: 要删除的历史记录项的xpath路径
        Returns:
            bool: 删除是否成功
        """
        try:
            ActionChains(self.driver).move_to_element(self.driver.find_element(By.XPATH, item_xpath)).perform()
            self.driver.find_element(By.CLASS_NAME, "item-box-delete").click()
            delete_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button.global-font-mask-medium.confirm"))
            )
            delete_button.click()
            delete_success_message = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div[7]/div/div/div/span[2]")
                )
            )
            print(delete_success_message.text)
            return True
        except Exception as e:
            print(f"删除历史记录项失败: {str(e)}")
            return False
    def wait_for_loading_to_finish(self,item_class_name,process_time_limitation):
        """等待loading消失"""
        try:
            WebDriverWait(self.driver, process_time_limitation).until(
            EC.visibility_of_element_located((By.CLASS_NAME, item_class_name))
        )
            WebDriverWait(self.driver, process_time_limitation).until(
            EC.invisibility_of_element((By.CLASS_NAME, item_class_name))
        )
            print("Process finished")
        except TimeoutException:
            print("Process failed")
            return False
    def publish_on_haimeta_community(self,item_to_publish_XPATH, publish_button_Xpath, publish_on_community_Xpath, cancel_button_Xpath):
        """发布到Haimeta社区"""
        wait = self.wait
        driver = self.driver
        actions = self.actions
        # Publish the image
        actions.move_to_element(
            driver.find_element(By.XPATH, item_to_publish_XPATH)
        ).perform()
        self.click_action_check_by_visibility(publish_button_Xpath)
        # Publish on HAIMETA community
        self.click_action_check_by_visibility(publish_on_community_Xpath)
        
        # Input the title
        title_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.TITLE_INPUT_XPATH))
        )
        title_input.send_keys("Test")
        # Input the description
        description_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.DESCRIPTION_INPUT_XPATH))
        )
        description_input.send_keys("Test")
        # Click the publish button
        self.click_action_check_by_visibility(self.CONFIRM_PUBLISH_BUTTON_XPATH)

        # Cancel the publish
        actions.move_to_element(
            driver.find_element(By.XPATH, item_to_publish_XPATH)
        ).perform()
        self.click_action_check_by_visibility(publish_button_Xpath)
        # cancel publish button click
        self.click_action_check_by_visibility(cancel_button_Xpath)
    def download_image(self,item_to_download_XPATH,download_button_xpath):
        """下载图片"""
        wait = self.wait
        driver = self.driver
        actions = self.actions
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, item_to_download_XPATH)
            )
        )
        actions.move_to_element(
            driver.find_element(By.XPATH, item_to_download_XPATH)
        ).pause(3).perform()
        self.click_action_check_by_visibility(download_button_xpath)

    def publish_on_style_library(self,item_to_publish_XPATH):
        """发布到风格库"""
        wait = self.wait
        driver = self.driver
        actions = self.actions
        actions.move_to_element(
            driver.find_element(By.XPATH, item_to_publish_XPATH)
        ).perform()
        publish_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.PUBLISH_BUTTON_XPATH_CAYL))
        )
        actions.move_to_element(publish_button_click).click().perform()
        publick_on_style_library_button_click = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.PUBLISH_ON_STYLE_LIBRARY_BUTTON_XPATH))
        )
        actions.move_to_element(publick_on_style_library_button_click).click().perform()
        # Input the style name
        style_name_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.STYLE_NAME_INPUT_XPATH))
        )
        style_name_input.send_keys("Test")
    
        # Agree the terms
        self.click_action_check_by_element_to_be_clickable(self.AGREE_TERMS_BUTTON_XPATH)

        # Click the publish button
        self.click_action_check_by_visibility(self.PUBLISH_ON_STYLE_LIBRARY_CONFIRM_BUTTON_XPATH)

    def report_the_image(self,item_to_report_XPATH,three_dots_button_Xpath,report_button_Xpath):
        """举报图片"""
        wait = self.wait
        driver = self.driver
        actions = self.actions
        actions.move_to_element(
            driver.find_element(By.XPATH, item_to_report_XPATH)
        ).perform()
        three_dots_button_click=wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,three_dots_button_Xpath)
            )
        )
        actions.move_to_element(
           three_dots_button_click
        ).click().perform()
        
        # click report button
        self.click_action_check_by_element_to_be_clickable(report_button_Xpath)
        
        # Select the report type
        self.click_action_check_by_visibility(self.REPORT_TYPE_BUTTON_XPATH)
        # Input the report reason
        report_reason_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.REPORT_REASON_INPUT_XPATH))
        )
        report_reason_input.send_keys("Test")
        time.sleep(3)
        # Click the report button
        self.click_action_check_by_visibility( self.CONFIRM_REPORT_BUTTON_XPATH)

    def upload_image(self, upload_way_XPATH, upload_image_paths):
        """上传单张或多张图片
        Args:
            upload_way_XPATH: 上传按钮的XPATH
            upload_image_paths: 可以是单个图片路径的字符串，或是多个图片路径的列表/元组
        """
        wait = self.wait
        # Upload the image(s)
        upload_button = wait.until(
            EC.presence_of_element_located((By.XPATH, upload_way_XPATH))
        )
        
        # 处理多图片上传
        if isinstance(upload_image_paths, (list, tuple)):
            # 将多个路径用 \n 连接，Selenium会将其识别为多文件上传
            paths = '\n'.join(upload_image_paths)
            upload_button.send_keys(paths)
        else:
            # 单图片上传
            upload_button.send_keys(upload_image_paths)
            
        self.wait_for_loading_to_finish("upload-loading", 20)
        print("Upload image(s) successfully")

    def choose_style_skin_texture_of_generated_image(self, style_selection_XPATH,skin_texture_input_XPATH):
        wait = self.wait
        driver = self.driver
        actions= self.actions
        # Choose the style of generated image
        self.click_action_check_by_visibility(style_selection_XPATH)
        # Input the SKIN TEXTURE
        skin_texture_input= self.click_action_check_by_visibility(skin_texture_input_XPATH)
        skin_texture_input.send_keys("0.67")  
    def click_create_button_xpath(self, button_Xpath):
        self.click_action_check_by_element_to_be_clickable(button_Xpath)
    
    def click_create_button_class_name(self, button_class_name):
        wait = self.wait
        self.click_action_check_by_element_to_be_clickable(button_class_name)

    def set_up_the_size_of_the_generated_image(self,size_button_Xpath,certain_size_Xpath):
        # Set up the size of the generated image
        self.click_action_check_by_visibility(size_button_Xpath)
        self.click_action_check_by_visibility(certain_size_Xpath)

    def set_up_the_layout_of_the_generated_image(self,layout_button_Xpath,certain_layout_Xpath):
        wait = self.wait
        driver = self.driver
        actions = self.actions
        # Set up the layout of the generated image
        self.click_action_check_by_visibility(layout_button_Xpath)
        self.click_action_check_by_visibility(certain_layout_Xpath)

    def adjust_the_position_of_the_generated_image(self,adjusted_image_XPATH):
        wait = self.wait
        driver = self.driver
        actions = self.actions

        actions.move_to_element(
            driver.find_element(By.XPATH, adjusted_image_XPATH)
        ).perform()
        # adjust_button_click = wait.until(
        #     EC.visibility_of_element_located((By.XPATH, self.ADJUST_BUTTON_XPATH))
        # )
        # adjust_button_click.click()
        
        self.switch_frame_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/iframe")
        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/flutter-view")))
        actions.click_and_hold(driver.find_element(By.XPATH, "/html/body/flutter-view"))  # 点击并按住元素
        actions.move_by_offset(10, 20)  # 移动到目标元素
        actions.pause(3)
        actions.release()  # 释放鼠标
        actions.perform()
        # can not locate th save button after adjusting the position of the generated image
        # end the code here


    def delete_the_generated_image(self,item_to_delete_XPATH,three_dots_button_Xpath,delete_button_Xpath):
        wait = self.wait
        driver = self.driver
        actions = self.actions
        actions.move_to_element(
            driver.find_element(By.XPATH, item_to_delete_XPATH)
        ).perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, three_dots_button_Xpath)))
        actions.move_to_element(
            driver.find_element(By.XPATH, three_dots_button_Xpath)
        ).click().perform()

        self.click_action_check_by_visibility(delete_button_Xpath)
        
        self.click_action_check_by_visibility(self.CONFIRM_DELETE_BUTTON_XPATH)

    def open_the_certain_function(self,section_for_this_function_xpath,function_button_xpath):
        driver = self.driver
        wait = self.wait
        driver.get(self.HOME_URL)
        self.click_action_check_by_visibility(section_for_this_function_xpath)
        time.sleep(2)
        function_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, function_button_xpath))
        )
        if not self.perform_click_and_check_tab(function_button_click):
            raise Exception("Failed to open ID Photo in new tab after 3 attempts")
        tab = self.switch_tab(driver, wait)

    def interact_with_single_photo_album(self):
        wait = self.wait
        actions = self.actions
        self.choose_style_skin_texture_of_generated_image(self.CHOOSE_PHOTO_GENERATION_STYLE_XPATH,self.INPUT_SKIN_TEXTURE_SINGLE_PHOTO_ALBUM)

        # set the number of images to generate
        number_of_images_to_generate_button_click = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_PHOTO_ALBUM))
        )
        number_of_images_to_generate_button_click.click()

        self.click_create_button_xpath(self.CREATE_BUTTON_XPATH)
        self.wait_for_loading_to_finish(item_class_name="_pictureEditorLoading_anlig_1",process_time_limitation=60)

        second_item_selected = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.SECOND_ITEM_SELECTED_XPATH))
        )
        actions.move_to_element(second_item_selected).double_click().perform()
        #interact with the generated images
        self.download_image(self.INTERACTED_IMAGE_1_XPATH,self.DOWNLOAD_BUTTON_XPATH_CAYL_AND_SINGLE_PHOTO_ABLUM)
        self.publish_on_haimeta_community(self.INTERACTED_IMAGE_1_XPATH, self.PUBLISH_BUTTON_XPATH_SINGLE_PHOTO_ALBUM, self.PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_SINGLE_PHOTO_ALBUM, self.CANCEL_PUBLISH_BUTTON_XPATH_SINGLE_PHOTO_ALBUM)
        self.report_the_image(self.INTERACTED_IMAGE_1_XPATH,self.THREE_DOTS_BUTTON_XPATH_SINGLE_PHOTO_ALBUM,self.REPORT_BUTTON_XPATH_ID_PHOTO_SINGLE_PHOTO_ALBUM)
        self.delete_the_generated_image("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div",self.THREE_DOTS_BUTTON_XPATH_SINGLE_PHOTO_ALBUM,self.DELETE_BUTTON_XPATH_SINGLE_PHOTO_ALBUM)
    
    def refine_your_idea(self):
        wait = self.wait
        driver = self.driver
        # Refine your idea
        Refine_your_idea_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.REFINE_YOUR_IDEA_BUTTON_XPATH))
        )
        Refine_your_idea_button_click.click()
        # Wait for the loading to finish
        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, self.REFINE_YOUR_IDEA_BUTTON_XPATH))
        )
    
    def select_the_size_of_the_generated_image(self,size_of_generation_button_xpath):
        self.click_action_check_by_visibility(size_of_generation_button_xpath)

    def input_prompt_box_CLASS_NAME(self,input_prompt_box_class_name,input_prompt_box_input_data):
        wait = self.wait
        Input_prompt_box = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, input_prompt_box_class_name))
        )
        Input_prompt_box.click()
        Input_prompt_box.send_keys(input_prompt_box_input_data)
    
    def set_number_of_images_to_generate(self,number_of_images_to_generate_button_xpath):
        self.click_action_check_by_visibility(number_of_images_to_generate_button_xpath)
    

    def click_action_check_by_visibility(self,action_button_xpath):
        wait = self.wait
        action_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, action_button_xpath))
        )
        action_button_click.click()
    
    def click_action_check_by_presence(self,action_button_xpath):
        wait = self.wait
        action_button_click = wait.until(
            EC.presence_of_element_located((By.XPATH, action_button_xpath))
        )
        action_button_click.click()

    def click_action_check_by_element_to_be_clickable(self,action_button_xpath):
        wait = self.wait
        action_button_click = wait.until(
            EC.element_to_be_clickable((By.XPATH, action_button_xpath))
        )
        action_button_click.click()

    def interact_with_the_second_item_selected(self,item_xpath):
        wait = self.wait
        actions = self.actions
        second_item_selected = wait.until(
            EC.element_to_be_clickable((By.XPATH, item_xpath))
        )
        actions.move_to_element(second_item_selected).double_click().perform()

    def switch_frame_by_xpath(self,frame_xpath):
        driver= self.driver
        wait = self.wait
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, frame_xpath)))
        driver.switch_to.frame(driver.find_element(By.XPATH,frame_xpath))