from functools import WRAPPER_ASSIGNMENTS
import time
import unittest
import json
from idlelib.search import find_selection

from selenium import webdriver
from selenium.common import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.network import set_data_size_limits_for_test
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.action_chains import ActionChains

from Test_config import INPUT_PROMPT_BOX_CLASS_NAME


# 定义一个测试类
class Test(unittest.TestCase):
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
        PURCHASE_HAIBIT_PAY_NOW_BUTTON_id, CREATE_AS_YOU_LIKE_UNDER_BUZZ_BUTTON_XPATH, INPUT_PROMPT_BOX_XPATH,
        GENERATE_BUTTON_CLASS_NAME, INPUT_PROMPT_BOX_CLASS_NAME, REFINE_YOUR_IDEA_BUTTON_XPATH,
        SIZE_OF_GENERATION_BUTTON_XPATH, NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH,
        FEEDBACK_XPATH, IMAGE_1_XPATH, DOWNLOAD_BUTTON_XPATH_CAYL_AND_SINGLE_PHOTO_ABLUM, PUBLISH_BUTTON_XPATH_CAYL,
        PUBLICK_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_CAYL,
        TITLE_INPUT_XPATH, DESCRIPTION_INPUT_XPATH, CONFIRM_PUBLISH_BUTTON_XPATH, CANCEL_PUBLISH_BUTTON_XPATH_CAYL,
        PUBLICK_ON_STYLE_LIBRARY_BUTTON_XPATH, STYLE_NAME_INPUT_XPATH, AGREE_TERMS_BUTTON_XPATH,
        PUBLISH_ON_STYLE_LIBRARY_CONFIRM_BUTTON_XPATH, DOWNLOAD_BUTTON_XPATH_ID_PHOTO,
        REPORT_BUTTON_XPATH_CAYL, REPORT_TYPE_BUTTON_XPATH, REPORT_REASON_INPUT_XPATH, CONFIRM_REPORT_BUTTON_XPATH,
        REPORT_BUTTON_XPATH_CAYL, REPORT_BUTTON_AFTER_PUBLISH_ON_STYLE_LIBRARY_XPATH,
        SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_CREATE_AS_U_LIKE,
        SWITCH_TO_CHINESE_LANGUAGE_XPATH_UNDER_CREATE_AS_U_LIKE,
        CHOOSE_PHOTO_GENERATION_STYLE_XPATH, THREE_DOTS_BUTTON_XPATH_CAYL,
        TEST_MALE_PHOTO, TEST_FEMALE_PHOTO, CONFRIM_DELETE_BUTTON_XPATH, PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,
        CHOOSE_PHOTO_GENERATION_STYLE_XPATH,
        ID_PHOTO_IFRAME_XPATH, ITEM_TO_BE_INTERACTED_XPATH_ID,
        PHOTO_ALBUM_SECTION_BUTTON_XPATH, ID_PHOTO_BUTTON_XPATH, INPUT_SKIN_TEXTURE_ID_PHOTO_XPATH, CREATE_BUTTON_XPATH,
        PUBLISH_BUTTON_XPATH_ID_PHOTO, THREE_DOTS_BUTTON_XPATH_ID_PHOTO,
        PUBLICK_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_ID_PHOTO,
        CANCEL_PUBLISH_BUTTON_XPATH_ID_PHOTO, SET_SIZE_BUTTON_XPATH, INS_SIZE_BUTTON_XPATH, SET_LAYOUT_BUTTON_XPATH,
        FIVE_INCHES_LAYOUT_BUTTON_XPATH,
        EDITED_LAYOUT_PHOTO_LOCATION_XPATH, DOWNLOAD_EDITED_LAYOUT_PHOTO_BUTTON_XPATH, DELETE_BUTTON_XPATH_ID_PHOTO,
        SECOND_ITEM_SELECTED_XPATH, SINGLE_LAYOUT_BUTTON_XPATH, CHINESE_AESTHETICS_BUTTON_XPATH,
        INPUT_SKIN_TEXTURE_SINGLE_PHOTO_ALBUM, NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_PHOTO_ALBUM,
        PUBLICK_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_SINGLE_PHOTO_ALBUM, CANCEL_PUBLISH_BUTTON_XPATH_SINGLE_PHOTO_ALBUM,
        THREE_DOTS_BUTTON_XPATH_SINGLE_PHOTO_ALBUM, DELETE_BUTTON_XPATH_SINGLE_PHOTO_ALBUM,
        PUBLISH_BUTTON_XPATH_SINGLE_PHOTO_ALBUM, ARABIAN_DREAMS_BUTTON_XPATH,
        NANYANG_MEMORY_UNDER_LIFE_BUTTON_XPATH, EAST_ASIAN_CULTURE_UNDER_LIFE_BUTTON_XPATH,
        CYBER_FUTURE_UNDER_LIFE_BUTTON_XPATH,
        GORGEOUS_ROAD_UNDER_LIFE_BUTTON_XPATH, FANTASY_TALES_UNDER_LIFE_BUTTON_XPATH,
        CHINESE_AESTHETICS_UNDER_LIFE_BUTTON_XPATH,
        REPORT_BUTTON_XPATH_ID_PHOTO_SINGLE_PHOTO_ALBUM, FIRST_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM,
        SECOND_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM,
        LOVE_IN_THE_AIR_BUTTON_UNDER_LIFE_BUTTON_XPATH, BFF_MOMENT_BUTTON_UNDER_LIFE_BUTTON_XPATH,
        BRO_SHOW_BUTTON_UNDER_LIFE_BUTTON_XPATH, TEST_IMAGE, DOWNLOAD_PATTERN_BUTTON_XPATH, ADD_NEW_IMAGE_BUTTON_XPATH,
        IMAGE_2_XPATH,
        UPLOAD_IMAGE_CREATE_CLOTHES_XPATH, DELETE_BUTTON_XPATH_CREATE_CLOTHES_XPATH,
        WORK_SECTION_BUTTON_XPATH, CREATE_CLOTHES_BUTTON_UNDER_WORK_SECTION, REPORT_BUTTON_CREATE_CLOTHES_XPATH,
        PET_IMAGE_DATA_SET, PET_SECTION_BUTTON_XPATH, STYLE_YOUR_PET_ON_HOME_UNDER_PET_SECTION_XPATH,
        START_TRAINING_BUTTON_XPATH,
        CREATE_BUTTON_XPATH_STYLE_YOUR_PET, ADD_PET_DATA_SET_BUTTON_XPATH, UPLOAD_IMAGE_STYLE_YOUR_PET_XPATH
    , STYLE_CHOICE_BUTTON_XPATH, SIZE_OF_GENERATION_BUTTON_XPATH_T2I, NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_T2I,
        CREATE_BUTTON_XPATH_T2I, THREE_DOTS_BUTTON_XPATH_T2I, REPORT_BUTTON_XPATH_T2I, CANCEL_PUBLISH_BUTTON_XPATH_T2I,
        DELETE_BUTTON_XPATH_T2I, CREATE_NAIL_ART_BUTTON_UNDER_WORK_SECTION_XPATH, ART_SECTION_BUTTON_XPATH,
        CREATE_TATTOO_BUTTON_UNDER_WORK_SECTION_XPATH, CREATE_TOY_BUTTON_UNDER_WORK_SECTION_XPATH,
        CREATE_LOGO_BUTTON_UNDER_WORK_SECTION_XPATH, ME_TIME_BUTTON_UNDER_WORK_SECTION_XPATH,
        CREATE_CHARACTER_BUTTON_UNDER_WORK_SECTION_XPATH, STOCK_IMAGE_BUTTON_UNDER_WORK_SECTION_XPATH,
        TEXTURE_LABEL_BUTTON_UNDER_ART_SECTION_XPATH, PATTERN_BUTTON_UNDER_ART_SECTION_XPATH,
        STYLE_BUTTON_UNDER_ART_SECTION_XPATH,
        CREATE_WALLPAPER_BUTTON_UNDER_ART_SECTION_XPATH, TRENDY_ART_BUTTON_UNDER_ART_SECTION_XPATH,
        CHARACTER_TEXTURE_BUTTON_UNDER_WORK_SECTION_XPATH, STYLE_CHOICE_BUTTON_XPATH_T2I_WITHE_REFINING,
        SIZE_OF_GENERATION_BUTTON_XPATH_T2I_WITHE_REFINING,
        NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_T2I_WITHE_REFINING,
        PUBLICK_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_T2I_WITHE_REFINING, CANCEL_PUBLISH_BUTTON_XPATH_T2I_WITHE_REFINING,
        PUBLISH_BUTTON_XPATH_T2I_WITHE_REFINING
    )
    # 类级别的初始化方法，在所有测试用例执行前执行一次
    @classmethod
    def setUpClass(cls):
        """Initialize the test environment and perform login."""
        # 启动浏览器
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        cls.driver = webdriver.Chrome(options=options)
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.actions=ActionChains(cls.driver)

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

    
                
    def test_picture_Edition(self):

        driver = self.driver
        wait = self.wait
        actions=self.actions
        driver.get(self.HOME_URL)
        edition_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.EDITION_ON_HOME_BUTTON_XPATH))
        )
        actions.move_to_element(edition_button_click).click().perform()
        # 切换到新标签页
        tab = self.switch_tab(driver, wait)

        self.upload_image(self.PICTURE_EDITION_UPLOAD_BUTTON_XPATH,r'D:\PycharmProjects\PythonProject\TestUpload.png')

        self.check_history()

        select_button_click = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "iconfont.ic_mouse.icon_style")
            )
        )
        select_button_click.click()

        driver.find_element(By.CLASS_NAME, "iconfont.ic_drag_storke.icon_style").click()  # MoveSpaceButtonCheck

        driver.switch_to.frame(
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/iframe"))
        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/flutter-view")))
        actions.click_and_hold(driver.find_element(By.XPATH, "/html/body/flutter-view"))  # 点击并按住元素
        actions.move_by_offset(10, 20)  # 移动到目标元素
        actions.move_by_offset(-10, -20)
        actions.pause(3)
        actions.release()  # 释放鼠标
        actions.perform()
        driver.switch_to.default_content()
        driver.find_element(By.CLASS_NAME, "iconfont.ic_text.icon_style").click()  # Add Text Button Check
        driver.find_element(By.CLASS_NAME, "iconfont.ic_Stickers.icon_style").click()  # Stickers Button Check

        driver.find_element(By.CLASS_NAME, "iconfont.ic_cancel.icon_style").click()  # Undo button Check

        driver.find_element(By.CLASS_NAME, "iconfont.ic_regain.icon_style").click()  # Redo Button Check

        driver.find_element(By.CLASS_NAME, "iconfont.ic_clean.icon_style").click()  # Reset Button Check

        driver.find_element(By.CLASS_NAME, "download-btn").click()  # Download Button Check

        driver.find_element(By.CLASS_NAME, "save-edit-image").click()  # Save File Online Check

        try:  # 检查是否能够正常
            check_save = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "ant-tooltip-inner"))
            )
            if check_save.is_displayed():
                print("✅ 成功保存！")
            else:
                print("❌ 保存失败！")
        except TimeoutException:
            print("❌ 超时，保存失败！")

        #Delete the Edited picture
        ActionChains(driver).move_to_element(driver.find_element(By.XPATH,
                                                                 "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div")).perform()
        driver.find_element(By.CLASS_NAME, "item-box-delete").click()
        delete_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "button.global-font-mask-medium.confirm"))
        )
        delete_button.click()
        delete_success_message = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[7]/div/div/div/span[2]")
            )
        )
        print(delete_success_message.text)

        # 界面下语言切换是否正常
        # Switch to English
        self.switch_language(
            target_language="English",
            language_selection_class_name=self.LANGUAGE_SELECTION_CLASS_NAME,
            language_switch_xpath=self.SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_PE,
            expected_title_text="Image Edit",
            expected_title_class_name="default-box-title"
        )
        
        # Switch to Chinese
        self.switch_language(
            target_language="Chinese",
            language_selection_class_name=self.LANGUAGE_SELECTION_CLASS_NAME,
            language_switch_xpath=self.SWITCH_TO_CHINESE_LANGUAGE_PE_HOME_XPATH,
            expected_title_text="图片编辑"
        )

    
                
    def test_BG_Remover(self):
        driver = self.driver
        wait= self.wait
        actions=self.actions
        driver.get(self.HOME_URL)
        BG_button_click=wait.until(
            EC.element_to_be_clickable((By.XPATH,self.BG_REMOVER_ON_HOME_BUTTON_XPATH))
        )
        actions.move_to_element(BG_button_click).click().perform()
        # 切换到新标签页
        tab = self.switch_tab(driver, wait)
        
        upload_button = wait.until(
            EC.presence_of_element_located((By.XPATH, self.BG_REMOVER_UPLOAD_BUTTON_XPATH))
        )
        upload_button.send_keys(r'D:\PycharmProjects\PythonProject\TestUpload.png')
        #存在的问题：工具栏界面还没加载完就可以点击，导致脚本执行了点击按钮的操作但是没有任何的效果
        wait.until(
            EC.invisibility_of_element_located(
                (By.CLASS_NAME, "carousel-secondtip")
            )
        )
        self.check_history()
        move_space_click=wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME,"fabric-action-bar-item.fabric-action-bar-move")
            )
        )
        move_space_click.click()  # MoveSpaceButtonCheck

        driver.find_element(By.CLASS_NAME,"fabric-action-bar-item.fabric-action-bar-item1").click()  # RepairButtonCheck
        actions.click_and_hold(driver.find_element(By.CLASS_NAME, "upper-canvas"))
        actions.move_by_offset(200, 50)  # 移动到目标元素
        actions.pause(3)
        actions.release()  # 释放鼠标
        actions.perform()

        driver.find_element(By.CLASS_NAME,"fabric-action-bar-item.fabric-action-bar-item1").click() #EraseButtonCheck
        actions.click_and_hold(driver.find_element(By.CLASS_NAME, "upper-canvas"))
        actions.move_by_offset(100, 50)  # 移动到目标元素
        actions.pause(3)
        actions.release()  # 释放鼠标
        actions.perform()

        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[6]").click()  # Undo button Check

        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[7]").click()  # Redo Button Check

        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[7]/div").click()  # Reset Button Check

        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/div[3]/span[1]").click()  # Download Button Check

        # Delete the Edited picture
        ActionChains(driver).move_to_element(driver.find_element(By.XPATH,
                                                                 "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div")).perform()
        actions.move_to_element(driver.find_element(By.CLASS_NAME,"item-box-delete")).click().perform()
        delete_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "button.global-font-mask-medium.confirm"))
        )
        delete_button.click()

        # Switch to English
        self.switch_language(
            target_language="English",
            language_selection_class_name=self.LANGUAGE_SELECTION_CLASS_NAME,
            language_switch_xpath=self.SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_AI_CUT,
            expected_title_text="Background elimination",
            expected_title_class_name="upload-top-title"
        )

        # Switch to Chinese
        self.switch_language(
            target_language="Chinese",
            language_selection_class_name=self.LANGUAGE_SELECTION_CLASS_NAME,
            language_switch_xpath=self.SWITCH_TO_CHINESE_LANGUAGE_XPATH_ON_AI_CUT_HOME,
            expected_title_text="背景消除",
            expected_title_class_name="upload-top-title"
        )
    def test_smart_Eraser(self):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        driver.get(self.HOME_URL)
        Smart_Eraser_button_click = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.SMART_ERASER_ON_HOME_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(Smart_Eraser_button_click):
            raise Exception("Failed to open Smart Eraser in new tab after 3 attempts")
        # 切换到新标签页
        tab = self.switch_tab(driver, wait)
        upload_button = wait.until(
            EC.presence_of_element_located((By.XPATH, self.SMART_ERASER_UPLOAD_BUTTON_XPATH))
        )
        upload_button.send_keys(r'D:\PycharmProjects\PythonProject\TestUpload.png')
        self.check_history()

        move_space_click = wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "iconfont.ic_drag_storke")
            )
        )
        move_space_click.click()  # MoveSpaceButtonCheck
        driver.find_element(By.CLASS_NAME, "fabric-action-bar-item.fabric-action-bar-item1").click()  # RepairButtonCheck
        actions.click_and_hold(driver.find_element(By.CLASS_NAME, "upper-canvas"))
        actions.move_by_offset(50, 50)  # 移动到目标元素
        actions.pause(3)
        actions.release()  # 释放鼠标
        actions.perform()

        driver.find_element(By.CLASS_NAME, "fabric-action-bar-item-icon.ins-icon-eraser").click()  # EraseButtonCheck
        actions.click_and_hold(driver.find_element(By.CLASS_NAME, "upper-canvas"))
        actions.move_by_offset(200, 50)  # 移动到目标元素
        actions.pause(3)
        actions.release()  # 释放鼠标
        actions.perform()

        # driver.find_element(By.CLASS_NAME, "deduction-points-container").click()  # BeginEleminationButtonCheck 
        # wait.until(
        #     EC.invisibility_of_element_located(
        #         (By.CLASS_NAME, "_RowLoading_1mww2_1.generate-row-loading")
        #     )
        # )
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[6]/div/div").click()  # Undo button Check
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[7]/div/div").click()  # Redo Button Check    
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[8]").click()  # Reset Button Check
        driver.find_element(By.CLASS_NAME, "header-Download").click()  # Download Button Check
        # Delete the Edited picture
        # ActionChains(driver).move_to_element(driver.find_element(By.XPATH,
        #                                                          "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div")).perform()

        # delete_button = wait.until(
        #     EC.visibility_of_element_located(
        #         (By.CLASS_NAME, "item-box-delete")
        #     )
        # )
        # actions.move_to_element(delete_button).click().perform()
        # confirm_button = wait.until(
        #     EC.visibility_of_element_located((By.XPATH, "/html/body/div[7]/div/div/div/div/div/div[2]/button[2]"))
        # )
        # actions.move_to_element(confirm_button).click().perform()
        # Switch to English
        self.switch_language(
            target_language="English",
            language_selection_class_name=self.LANGUAGE_SELECTION_CLASS_NAME,
            language_switch_xpath=self.SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_SE,
            expected_title_text="Local elimination",
            expected_title_class_name="default-box-title"
        )
        # Switch to Chinese
        self.switch_language(
            target_language="Chinese",
            language_selection_class_name=self.LANGUAGE_SELECTION_CLASS_NAME,
            language_switch_xpath=self.SWITCH_TO_CHINESE_LANGUAGE_XPATH_ON_SE_HOME,
            expected_title_text="局部消除",
            expected_title_class_name="default-box-title"
        )

    def test_HD_enlarge(self):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        driver.get(self.HOME_URL)
        HD_enlarge_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.HD_ENLARGE_ON_HOME_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(HD_enlarge_button_click):
            raise Exception("Failed to open HD Enlarge in new tab after 3 attempts")
        
        tab = self.switch_tab(driver, wait)

        upload_button = wait.until(
            EC.presence_of_element_located((By.XPATH, self.HD_ENLARGE_UPLOAD_BUTTON_XPATH))
        )
        upload_button.send_keys(r'D:\PycharmProjects\PythonProject\TestUpload.png')
        self.check_history()
        
        #Choose enlarge 2x
        two_times_enlarge_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.TWO_TIMES_ENLARGE_BUTTON_XPATH))
        )
        two_times_enlarge_button_click.click()
        #Click the enlarge button
        enlarge_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.ENLARGE_BUTTON_XPATH))
        ).click()
        # Wait for the loading to finish
        wait.until(
            EC.invisibility_of_element((By.CLASS_NAME, "carousel-secondtip"))
        )

        #chose the 4x enlarge
        four_times_enlarge_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.FOUR_TIMES_ENLARGE_BUTTON_XPATH))
        )
        four_times_enlarge_button_click.click()
        #Click the enlarge button
        enlarge_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.ENLARGE_BUTTON_XPATH)) 
        ).click()
        # Wait for the loading to finish
        wait.until(
            EC.invisibility_of_element((By.CLASS_NAME, "carousel-secondtip"))
        )
        #delete the edited picture
        ActionChains(driver).move_to_element(driver.find_element(By.XPATH,
                                                                 "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]")).perform()
        delete_button = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "item-box-delete")
            )
        )
        actions.move_to_element(delete_button).click().perform()
        confirm_button = wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[7]/div/div/div/div/div/div[2]/button[2]"))
        )
        actions.move_to_element(confirm_button).click().perform()
        # Switch to English
        self.switch_language(
            target_language="English",
            language_selection_class_name=self.LANGUAGE_SELECTION_CLASS_NAME,
            language_switch_xpath=self.SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_AI_CUT,
            expected_title_text="Lossless amplification",
            expected_title_class_name="default-box-title"  
        )

        # Switch to Chinese
        self.switch_language(
            target_language="Chinese",
            language_selection_class_name=self.LANGUAGE_SELECTION_CLASS_NAME,
            language_switch_xpath=self.SWITCH_TO_CHINESE_LANGUAGE_XPATH_ON_AI_CUT_HOME,
            expected_title_text="无损放大",
            expected_title_class_name="default-box-title"
        )
    
    def test_HD_repair(self):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        driver.get(self.HOME_URL)
        HD_repair_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.HD_REPAIR_ON_HOME_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(HD_repair_button_click):
            raise Exception("Failed to open HD Repair in new tab after 3 attempts")
        
        tab = self.switch_tab(driver, wait)

        upload_button = wait.until(
            EC.presence_of_element_located((By.XPATH, self.HD_REPAIR_UPLOAD_BUTTON_XPATH))
        )
        upload_button.send_keys(r'D:\PycharmProjects\PythonProject\TestUpload.png')
        self.check_history()

        #Click HD repair button
        HD_repair_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.HD_REPAIR_BUTTON_XPATH))
        )
        HD_repair_button_click.click()
        # Wait for the loading to finish
        wait.until(
            EC.invisibility_of_element((By.CLASS_NAME, "carousel-secondtip"))
        )
        #delete the edited picture
        # self.check_history()
        # wait.until(
        #     EC.visibility_of_element_located(
        #         (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]")
        #     )
        # )
        # ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]")).perform()
        # delete_button = wait.until(
        #     EC.visibility_of_element_located(
        #         (By.CLASS_NAME, "item-box-delete")
        #     )
        # )
        # actions.move_to_element(delete_button).click().perform()
        # confirm_button = wait.until(
        #     EC.visibility_of_element_located((By.XPATH, "/html/body/div[7]/div/div/div/div/div/div[2]/button[2]"))
        # )
        # actions.move_to_element(confirm_button).click().perform()
        # Switch to English
        self.switch_language(
            target_language="English",
            language_selection_class_name=self.LANGUAGE_SELECTION_CLASS_NAME,
            language_switch_xpath=self.SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_AI_CUT,
            expected_title_text="HD repair",
            expected_title_class_name="default-box-title"
        )

        # Switch to Chinese
        self.switch_language(
            target_language="Chinese",
            language_selection_class_name=self.LANGUAGE_SELECTION_CLASS_NAME,
            language_switch_xpath=self.SWITCH_TO_CHINESE_LANGUAGE_XPATH_ON_AI_CUT_HOME,
            expected_title_text="高清修复",
            expected_title_class_name="default-box-title"
        )

    def test_create_as_you_like(self):
        driver = self.driver
        wait = self.wait
        driver.get(self.HOME_URL)
        create_as_you_like_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.CREATE_AS_YOU_LIKE_UNDER_BUZZ_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(create_as_you_like_button_click):
            raise Exception("Failed to open Create as you like in new tab after 3 attempts")
        tab = self.switch_tab(driver, wait)

        Input_prompt_box = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, INPUT_PROMPT_BOX_CLASS_NAME))
        )
        Input_prompt_box.click()
        Input_prompt_box.send_keys("A beautiful girl")

        # Refine your idea
        Refine_your_idea_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.REFINE_YOUR_IDEA_BUTTON_XPATH))
        )
        Refine_your_idea_button_click.click()
        # Wait for the loading to finish
        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, self.REFINE_YOUR_IDEA_BUTTON_XPATH))
        )
        # Select the size of generation 
        size_of_generation_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.SIZE_OF_GENERATION_BUTTON_XPATH))
        )
        size_of_generation_button_click.click()

        # Select the number of images to generate
        number_of_images_to_generate_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH))
        )
        number_of_images_to_generate_button_click.click()

        # Click the generate button
        generate_button_click = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, self.GENERATE_BUTTON_CLASS_NAME))
        )
        generate_button_click.click()
        # Wait for the loading to finish
        self.wait_for_loading_to_finish(item_class_name="_pictureEditorLoading_anlig_1",process_time_limitation=30)

        # Interact with the generated images
        # Download the image
        self.download_image(self.IMAGE_1_XPATH, self.DOWNLOAD_BUTTON_XPATH_CAYL_AND_SINGLE_PHOTO_ABLUM)
        # Publish the image
        self.publish_on_haimeta_community(self.IMAGE_1_XPATH,self.PUBLISH_BUTTON_XPATH_CAYL,self.PUBLICK_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_CAYL,self.CANCEL_PUBLISH_BUTTON_XPATH_CAYL)
        # Publish the image on style library
        self.publish_on_style_library(item_to_publish_XPATH=self.IMAGE_1_XPATH)
        
        # Report the image
        self.report_the_image(self.IMAGE_1_XPATH,self.THREE_DOTS_BUTTON_XPATH_CAYL,self.REPORT_BUTTON_AFTER_PUBLISH_ON_STYLE_LIBRARY_XPATH)

        # Switch to English
        self.switch_language(
            target_language="English",
            language_selection_class_name=self.LANGUAGE_SELECTION_CLASS_NAME,
            language_switch_xpath=self.SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_CREATE_AS_U_LIKE,
            expected_title_text="Create As You Like",
            expected_title_class_name="title-item.global-font-title-small"
        )
        # Switch to Chinese
        self.switch_language(
            target_language="Chinese",
            language_selection_class_name=self.LANGUAGE_SELECTION_CLASS_NAME,
            language_switch_xpath=self.SWITCH_TO_CHINESE_LANGUAGE_XPATH_UNDER_CREATE_AS_U_LIKE,
            expected_title_text="风格创作",
            expected_title_class_name="title-item.global-font-title-small"
        )

    
    def test_id_photo(self):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        driver.get(self.HOME_URL)
        photo_album_section_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.PHOTO_ALBUM_SECTION_BUTTON_XPATH))
        )
        photo_album_section_button_click.click()
        time.sleep(1)
        id_photo_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.ID_PHOTO_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(id_photo_button_click):
            raise Exception("Failed to open ID Photo in new tab after 3 attempts")
        tab = self.switch_tab(driver, wait)
        self.upload_image(self.PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,self.TEST_FEMALE_PHOTO)
        self.choose_style_skin_texture_of_generated_image(self.CHOOSE_PHOTO_GENERATION_STYLE_XPATH,self.INPUT_SKIN_TEXTURE_ID_PHOTO_XPATH)
        self.click_create_button(self.CREATE_BUTTON_XPATH)
        # self.wait_for_loading_to_finish(item_class_name="_pictureEditorLoading_anlig_1",process_time_limitation=50)

        second_item_selected = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.SECOND_ITEM_SELECTED_XPATH))
        )
        actions.move_to_element(second_item_selected).click().perform()

        #interact with the generated images
        self.download_image(self.ITEM_TO_BE_INTERACTED_XPATH_ID,self.DOWNLOAD_BUTTON_XPATH_ID_PHOTO)
        self.publish_on_haimeta_community(self.ITEM_TO_BE_INTERACTED_XPATH_ID,self.PUBLISH_BUTTON_XPATH_ID_PHOTO,self.PUBLICK_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_ID_PHOTO,self.CANCEL_PUBLISH_BUTTON_XPATH_ID_PHOTO)
        self.report_the_image(self.IMAGE_1_XPATH,self.THREE_DOTS_BUTTON_XPATH_ID_PHOTO,self.REPORT_BUTTON_XPATH_ID_PHOTO_SINGLE_PHOTO_ALBUM)
        
        # Set up the Size of the generated image
        self.set_up_the_size_of_the_generated_image(self.SET_SIZE_BUTTON_XPATH,self.INS_SIZE_BUTTON_XPATH)
        # Set up the Layout of the generated image
        self.set_up_the_layout_of_the_generated_image(self.SET_LAYOUT_BUTTON_XPATH,self.FIVE_INCHES_LAYOUT_BUTTON_XPATH)

        # Download the generated images
        self.download_image(self.EDITED_LAYOUT_PHOTO_LOCATION_XPATH,self.DOWNLOAD_EDITED_LAYOUT_PHOTO_BUTTON_XPATH)

        self.set_up_the_layout_of_the_generated_image(self.SET_LAYOUT_BUTTON_XPATH,self.SINGLE_LAYOUT_BUTTON_XPATH)

        # Delete the generated images
        self.delete_the_generated_image("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div",self.THREE_DOTS_BUTTON_XPATH_ID_PHOTO,self.DELETE_BUTTON_XPATH_ID_PHOTO)


    def test_chinese_aesthetics(self):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        driver.get(self.HOME_URL)
        photo_album_section_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.PHOTO_ALBUM_SECTION_BUTTON_XPATH))
        )
        photo_album_section_button_click.click()
        chinese_aesthetics_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.CHINESE_AESTHETICS_UNDER_LIFE_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(chinese_aesthetics_button_click):
            raise Exception("Failed to open Chinese Aesthetics in new tab after 3 attempts")
        tab = self.switch_tab(driver, wait)
        
        self.upload_image(self.PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,self.TEST_FEMALE_PHOTO)
        # following up steps are the sam eas the signle photo album
        self.choose_style_skin_texture_of_generated_image(self.CHOOSE_PHOTO_GENERATION_STYLE_XPATH,self.INPUT_SKIN_TEXTURE_SINGLE_PHOTO_ALBUM)

        # set the number of images to generate
        self.interact_with_signle_photo_album()

    def test_arabian_dreams(self):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        driver.get(self.HOME_URL)
        photo_album_section_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.PHOTO_ALBUM_SECTION_BUTTON_XPATH))
        )
        photo_album_section_button_click.click()
        arabian_dreams_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.ARABIAN_DREAMS_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(arabian_dreams_button_click):
            raise Exception("Failed to open Arabian Dreams in new tab after 3 attempts")
        tab = self.switch_tab(driver, wait)
        self.upload_image(self.PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,self.TEST_FEMALE_PHOTO)
        self.interact_with_signle_photo_album()


    
    def test_nanyang_memory(self):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        driver.get(self.HOME_URL)
        photo_album_section_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.PHOTO_ALBUM_SECTION_BUTTON_XPATH))
        )
        photo_album_section_button_click.click()
        nanyang_memory_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.NANYANG_MEMORY_UNDER_LIFE_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(nanyang_memory_button_click):
            raise Exception("Failed to open Nanyang Memory in new tab after 3 attempts")
        tab = self.switch_tab(driver, wait)
        self.upload_image(self.PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,self.TEST_MALE_PHOTO)
        self.interact_with_signle_photo_album()

        
    def test_gorgeous_road(self):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        driver.get(self.HOME_URL)
        photo_album_section_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.PHOTO_ALBUM_SECTION_BUTTON_XPATH))
        )
        photo_album_section_button_click.click()
        gorgeous_road_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.GORGEOUS_ROAD_UNDER_LIFE_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(gorgeous_road_button_click):
            raise Exception("Failed to open Gorgeous Road in new tab after 3 attempts")
        tab = self.switch_tab(driver, wait)
        self.upload_image(self.PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,self.TEST_FEMALE_PHOTO)
        self.interact_with_signle_photo_album()

    def test_east_asian_culture(self):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        driver.get(self.HOME_URL)
        photo_album_section_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.PHOTO_ALBUM_SECTION_BUTTON_XPATH))
        )
        photo_album_section_button_click.click()
        east_asian_culture_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.EAST_ASIAN_CULTURE_UNDER_LIFE_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(east_asian_culture_button_click):
            raise Exception("Failed to open East Asian Culture in new tab after 3 attempts")
        tab = self.switch_tab(driver, wait)
        self.upload_image(self.PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,self.TEST_MALE_PHOTO)
        self.interact_with_signle_photo_album()


    def test_cyber_future(self):
        driver = self.driver
        wait = self.wait
        driver.get(self.HOME_URL)
        photo_album_section_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.PHOTO_ALBUM_SECTION_BUTTON_XPATH))
        )
        photo_album_section_button_click.click()
        cuber_future_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.CYBER_FUTURE_UNDER_LIFE_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(cuber_future_button_click):
            raise Exception("Failed to open Cuber Future in new tab after 3 attempts")
        tab = self.switch_tab(driver, wait)
        self.upload_image(self.PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,self.TEST_FEMALE_PHOTO)
        self.interact_with_signle_photo_album()


    def test_fantasy_tales(self):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        driver.get(self.HOME_URL)
        photo_album_section_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.PHOTO_ALBUM_SECTION_BUTTON_XPATH))
        )
        photo_album_section_button_click.click()
        fantasy_tales_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.FANTASY_TALES_UNDER_LIFE_BUTTON_XPATH))
        )       
        if not self.perform_click_and_check_tab(fantasy_tales_button_click):    
            raise Exception("Failed to open Fantasy Tales in new tab after 3 attempts")
        tab = self.switch_tab(driver, wait)
        self.upload_image(self.PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,self.TEST_FEMALE_PHOTO)
        self.interact_with_signle_photo_album()
    
    def test_love_in_the_air(self):
        driver = self.driver
        wait = self.wait
        driver.get(self.HOME_URL)
        photo_album_section_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.PHOTO_ALBUM_SECTION_BUTTON_XPATH))
        )
        photo_album_section_button_click.click()
        love_in_the_air_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.LOVE_IN_THE_AIR_BUTTON_UNDER_LIFE_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(love_in_the_air_button_click):
            raise Exception("Failed to open Love in the Air in new tab after 3 attempts")
        tab = self.switch_tab(driver, wait)
        self.upload_image(self.FIRST_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM,self.TEST_MALE_PHOTO)
        self.upload_image(self.SECOND_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM,self.TEST_FEMALE_PHOTO)
        self.interact_with_signle_photo_album()

    
    def test_BFF_moments(self):
        driver = self.driver
        wait = self.wait
        driver.get(self.HOME_URL)
        photo_album_section_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.PHOTO_ALBUM_SECTION_BUTTON_XPATH))
        )
        photo_album_section_button_click.click()
        BFF_moments_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.BFF_MOMENT_BUTTON_UNDER_LIFE_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(BFF_moments_button_click):
            raise Exception("Failed to open BFF Moments in new tab after 3 attempts")
        tab = self.switch_tab(driver, wait)
        self.upload_image(self.FIRST_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM,self.TEST_FEMALE_PHOTO)
        self.upload_image(self.SECOND_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM,self.TEST_FEMALE_PHOTO)
        self.interact_with_signle_photo_album()

    def test_bro_show(self):
        driver = self.driver
        wait = self.wait
        driver.get(self.HOME_URL)
        photo_album_section_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.PHOTO_ALBUM_SECTION_BUTTON_XPATH))
        )
        photo_album_section_button_click.click()
        BFF_moments_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.BRO_SHOW_BUTTON_UNDER_LIFE_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(BFF_moments_button_click):
            raise Exception("Failed to open BFF Moments in new tab after 3 attempts")
        tab = self.switch_tab(driver, wait)
        self.upload_image(self.FIRST_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM,self.TEST_MALE_PHOTO)
        self.upload_image(self.SECOND_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM,self.TEST_MALE_PHOTO)
        self.interact_with_signle_photo_album()


    def test_create_logo(self):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        driver.get(self.HOME_URL)
        create_logo_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.CREATE_LOGO_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(create_logo_button_click):
            raise Exception("Failed to open Create Logo in new tab after 3 attempts")
        tab = self.switch_tab(driver, wait)

    def test_character_portrait(self):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        driver.get(self.HOME_URL)
        character_portrait_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.CHARACTER_PORTRAIT_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(character_portrait_button_click):
            raise Exception("Failed to open Character Portrait in new tab after 3 attempts")
        tab = self.switch_tab(driver, wait)
    
    def test_pet_masterpiece_poster(self):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        driver.get(self.HOME_URL)
        pet_masterpiece_poster_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.PET_MASTERPIECE_POSTER_BUTTON_XPATH))
        )
        if not self.perform_click_and_check_tab(pet_masterpiece_poster_button_click):
            raise Exception("Failed to open Pet Masterpiece Poster in new tab after 3 attempts")
        tab = self.switch_tab(driver, wait)
        # Upload the image

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
            wait.until(
                EC.element_to_be_clickable((By.XPATH, language_switch_xpath))
            )
            driver.find_element(By.XPATH, language_switch_xpath).click()
            
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
        wait.until(EC.visibility_of_element_located((By.XPATH,self.BUY_HAIBIT_BUTTON_ON_PE_XPATH)))
        driver.find_element(By.XPATH,self.BUY_HAIBIT_BUTTON_ON_PE_XPATH).click()
        purchase_haibit_click = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH,self.PURCHASE_HAIBIT_ON_BILLING_HISTORY)
            )
        )
        purchase_haibit_click.click()

        wait.until(EC.visibility_of_element_located((By.XPATH, self.HAIBIT_PURCHASE_SELECTION_XPATH)))
        driver.find_element(By.XPATH, self.HAIBIT_PURCHASE_SELECTION_XPATH).click()

        driver.find_element(By.XPATH, self.COMFIRM_PAYMENT_IN_PURCHASE_HAIBIT_XPATH).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div/div[5]/div[2]/div[1]/form/div/div/iframe")))
        driver.switch_to.frame(driver.find_element(By.XPATH,"/html/body/div[1]/div/div[5]/div[2]/div[1]/form/div/div/iframe"))
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
    def publish_on_haimeta_community(self,item_to_publish_XPATH, publish_button_Xpath, publick_on_community_Xpath, cancel_button_Xpath):
        """发布到Haimeta社区"""
        wait = self.wait
        driver = self.driver
        actions = self.actions
        # Publish the image
        actions.move_to_element(
            driver.find_element(By.XPATH, item_to_publish_XPATH)
        ).perform()
        publish_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, publish_button_Xpath))
        )
        publish_button_click.click()
        # Publish on HAIMETA community
        Publick_on_HAIMETA_community_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, publick_on_community_Xpath))
        )
        Publick_on_HAIMETA_community_button_click.click()
        
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
        confirm_publish_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.CONFIRM_PUBLISH_BUTTON_XPATH))
        )
        confirm_publish_button_click.click()

        # Cancel the publish
        actions.move_to_element(
            driver.find_element(By.XPATH, item_to_publish_XPATH)
        ).perform()
        publish_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, publish_button_Xpath))
        )
        publish_button_click.click()
        cancel_publish_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, cancel_button_Xpath))
        )
        cancel_publish_button_click.click()
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
        download_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, download_button_xpath))
        )
        download_button_click.click()
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
            EC.element_to_be_clickable((By.XPATH, self.PUBLICK_ON_STYLE_LIBRARY_BUTTON_XPATH))
        )
        actions.move_to_element(publick_on_style_library_button_click).click().perform()
        # Input the style name
        style_name_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.STYLE_NAME_INPUT_XPATH))
        )
        style_name_input.send_keys("Test")
    
        # Agree the terms
        agree_terms_button_click = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.AGREE_TERMS_BUTTON_XPATH))
        )
        agree_terms_button_click.click()
        # Click the publish button
        confirm_publish_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.PUBLISH_ON_STYLE_LIBRARY_CONFIRM_BUTTON_XPATH))
        )
        confirm_publish_button_click.click()
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
        report_button_click = wait.until(
            EC.element_to_be_clickable((By.XPATH, report_button_Xpath))
        )
        report_button_click.click()
        
        # Select the report type
        report_type_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.REPORT_TYPE_BUTTON_XPATH))
        )
        report_type_button_click.click()
        # Input the report reason
        report_reason_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.REPORT_REASON_INPUT_XPATH))
        )
        report_reason_input.send_keys("Test")
        time.sleep(3)
        # Click the report button
        confirm_report_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.CONFIRM_REPORT_BUTTON_XPATH))
        )
        confirm_report_button_click.click()
    def upload_image(self,upload_way_XPATH,upload_image_absolute_path):
        """上传图片"""
        wait = self.wait
        # Upload the image
        upload_button = wait.until(
            EC.presence_of_element_located((By.XPATH, upload_way_XPATH))
        )
        upload_button.send_keys(upload_image_absolute_path)
        self.wait_for_loading_to_finish("upload-loading",20)
        print("Upload image successfully")
    def choose_style_skin_texture_of_generated_image(self, style_selection_XPATH,skin_texture_input_XPATH):
        wait = self.wait
        driver = self.driver
        actions= self.actions
        # Choose the style of generated image
        style_skin_texture_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, style_selection_XPATH))
        )
        style_skin_texture_button_click.click()
        # Input the SKIN TEXTURE
        skin_texture_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, skin_texture_input_XPATH))
        )
        skin_texture_input.clear()
        skin_texture_input.send_keys("0.67")  
    def click_create_button(self, button_Xpath):
        wait = self.wait
        driver = self.driver
        actions = self.actions
        create_button_click = wait.until(
            EC.element_to_be_clickable((By.XPATH, button_Xpath))
        )
        create_button_click.click()
    def set_up_the_size_of_the_generated_image(self,size_button_Xpath,certain_size_Xpath):
        wait = self.wait
        driver = self.driver
        actions = self.actions
        # Set up the size of the generated image
        size_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, size_button_Xpath))
        )
        size_button_click.click()
        certain_size_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, certain_size_Xpath))
        )
        certain_size_click.click()
    def set_up_the_layout_of_the_generated_image(self,layout_button_Xpath,certain_layout_Xpath):
        wait = self.wait
        driver = self.driver
        actions = self.actions
        # Set up the layout of the generated image
        layout_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, layout_button_Xpath))
        )
        layout_button_click.click()
        certain_layout_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, certain_layout_Xpath))
        )
        certain_layout_click.click()
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
        driver.switch_to.frame(
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/iframe"))
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
        ).perform()
        driver.find_element(By.XPATH, three_dots_button_Xpath).click()

        delete_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, delete_button_Xpath))
        )
        delete_button_click.click()
        confirm_delete_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.CONFRIM_DELETE_BUTTON_XPATH))
        )
        confirm_delete_button_click.click()
    def interact_with_signle_photo_album(self):
        wait = self.wait
        actions = self.actions
        self.choose_style_skin_texture_of_generated_image(self.CHOOSE_PHOTO_GENERATION_STYLE_XPATH,self.INPUT_SKIN_TEXTURE_SINGLE_PHOTO_ALBUM)

        # set the number of images to generate
        number_of_images_to_generate_button_click = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_PHOTO_ALBUM))
        )
        number_of_images_to_generate_button_click.click()

        self.click_create_button(self.CREATE_BUTTON_XPATH)
        self.wait_for_loading_to_finish(item_class_name="_pictureEditorLoading_anlig_1",process_time_limitation=60)

        second_item_selected = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.SECOND_ITEM_SELECTED_XPATH))
        )
        actions.move_to_element(second_item_selected).double_click().perform()
        #interact with the generated images
        self.download_image(self.IMAGE_1_XPATH,self.DOWNLOAD_BUTTON_XPATH_CAYL_AND_SINGLE_PHOTO_ABLUM)
        self.publish_on_haimeta_community(self.IMAGE_1_XPATH,self.PUBLISH_BUTTON_XPATH_SINGLE_PHOTO_ALBUM,self.PUBLICK_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_SINGLE_PHOTO_ALBUM,self.CANCEL_PUBLISH_BUTTON_XPATH_SINGLE_PHOTO_ALBUM)
        self.report_the_image(self.IMAGE_1_XPATH,self.THREE_DOTS_BUTTON_XPATH_SINGLE_PHOTO_ALBUM,self.REPORT_BUTTON_XPATH_ID_PHOTO_SINGLE_PHOTO_ALBUM)
        self.delete_the_generated_image("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div",self.THREE_DOTS_BUTTON_XPATH_SINGLE_PHOTO_ALBUM,self.DELETE_BUTTON_XPATH_SINGLE_PHOTO_ALBUM)

if __name__ == "__main__":
    unittest.main()


