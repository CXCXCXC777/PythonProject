from BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait


class Basic_Tool_Test(BaseTest):
    def test_picture_Edition(self):

        driver = self.driver
        wait = self.wait
        actions=self.actions
        self.open_the_certain_function(self.BUZZ_SECTION_BUTTON_XPATH, self.EDITION_ON_HOME_BUTTON_XPATH)    

        self.upload_image(self.PICTURE_EDITION_UPLOAD_BUTTON_XPATH,self.TEST_IMAGE)

        self.check_history()

        select_button_click = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "iconfont.ic_mouse.icon_style")
            )
        )
        select_button_click.click()

        driver.find_element(By.CLASS_NAME, "iconfont.ic_drag_storke.icon_style").click()  # MoveSpaceButtonCheck

        self.switch_frame_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/iframe")
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
        actions.move_to_element(driver.find_element(By.XPATH,
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
        self.open_the_certain_function(self.BUZZ_SECTION_BUTTON_XPATH, self.BG_REMOVER_ON_HOME_BUTTON_XPATH)
        
        self.upload_image(self.BG_REMOVER_UPLOAD_BUTTON_XPATH, self.TEST_IMAGE)
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


        self.open_the_certain_function(self.BUZZ_SECTION_BUTTON_XPATH, self.SMART_ERASER_ON_HOME_BUTTON_XPATH)
        self.upload_image(self.SMART_ERASER_UPLOAD_BUTTON_XPATH, self.TEST_IMAGE)
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
        self.open_the_certain_function(self.BUZZ_SECTION_BUTTON_XPATH, self.HD_ENLARGE_ON_HOME_BUTTON_XPATH)

        self.upload_image(self.HD_ENLARGE_UPLOAD_BUTTON_XPATH,self.TEST_IMAGE)
        self.click_action_check_by_presence(self.HD_ENLARGE_UPLOAD_BUTTON_XPATH)
        self.check_history()
        
        #Choose enlarge 2x
        self.click_action_check_by_visibility(self.TWO_TIMES_ENLARGE_BUTTON_XPATH)
        #Click the enlarge button
        self.click_action_check_by_visibility(self.ENLARGE_BUTTON_XPATH)
        # Wait for the loading to finish
        self.wait_for_loading_to_finish("carousel-secondtip",30)

        #chose the 4x enlarge
        self.click_action_check_by_visibility(self.FOUR_TIMES_ENLARGE_BUTTON_XPATH)
        #Click the enlarge button
        self.click_action_check_by_visibility(self.ENLARGE_BUTTON_XPATH)
        # Wait for the loading to finish
        self.wait_for_loading_to_finish("_pictureEditorLoading_anlig_1",30)
        #delete the edited picture
        actions.move_to_element(driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]")).perform()
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
        self.open_the_certain_function(self.BUZZ_SECTION_BUTTON_XPATH, self.HD_REPAIR_ON_HOME_BUTTON_XPATH)
        
        self.click_action_check_by_presence(self.HD_REPAIR_UPLOAD_BUTTON_XPATH)
        self.check_history()

        #Click HD repair button
        self.click_action_check_by_visibility(self.HD_REPAIR_BUTTON_XPATH)
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