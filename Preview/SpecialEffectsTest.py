from BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class SpecialEffectsTest(BaseTest):
    # 从Preview_config导入所需的配置变量和常量
    from Preview_config import (
        HD_ENLARGE_ON_HOME_BUTTON_XPATH, HD_ENLARGE_UPLOAD_BUTTON_XPATH,
        TWO_TIMES_ENLARGE_BUTTON_XPATH, FOUR_TIMES_ENLARGE_BUTTON_XPATH,
        ENLARGE_BUTTON_XPATH, HD_REPAIR_ON_HOME_BUTTON_XPATH,
        HD_REPAIR_UPLOAD_BUTTON_XPATH, HD_REPAIR_BUTTON_XPATH,
        SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_AI_CUT,
        SWITCH_TO_CHINESE_LANGUAGE_XPATH_ON_AI_CUT_HOME
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