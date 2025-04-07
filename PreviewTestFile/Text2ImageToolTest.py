import unittest

from selenium.webdriver.common import action_chains, actions
from urllib3.util import wait
from BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait

class Text2Image_Test(BaseTest):
    def common_step_for_T2I(self,section_for_this_button_xpath,button_xpath):
    
        driver = self.driver
        wait = self.wait
        actions= self.actions
        self.open_the_certain_function(section_for_this_button_xpath,button_xpath)

        self.input_prompt_box_CLASS_NAME(self.INPUT_PROMPT_BOX_CLASS_NAME," blue sky")

        # Refine your idea
        try:
            Refine_your_idea_button_click = wait.until(
                EC.visibility_of_element_located((By.XPATH, self.REFINE_YOUR_IDEA_BUTTON_XPATH))
            )
            Refine_your_idea_button_click.click()
            # Wait for the loading to finish
            WebDriverWait(driver, 50).until(
                EC.visibility_of_element_located((By.XPATH, self.REFINE_YOUR_IDEA_BUTTON_XPATH))
            )
        except:
            pass  # Skip if the button is not found

        # choose the style
        self.click_action_check_by_visibility(self.STYLE_CHOICE_BUTTON_XPATH_T2I_WITHE_REFINING)
        # Select the size of generation 
        self.click_action_check_by_visibility(self.SIZE_OF_GENERATION_BUTTON_XPATH_T2I_WITHE_REFINING)

        # Select the number of images to generate
        self.click_action_check_by_visibility(self.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_T2I_WITHE_REFINING)
        self.click_create_button_xpath(self.CREATE_BUTTON_XPATH_T2I)
        # Wait for the loading to finish
        self.wait_for_loading_to_finish(item_class_name="_pictureEditorLoading_anlig_1",process_time_limitation=60)
        # interact with the image
        self.interact_with_the_second_item_selected(self.SECOND_ITEM_SELECTED_XPATH)
        self.download_image(self.INTERACTED_IMAGE_1_XPATH,self.DOWNLOAD_BUTTON_XPATH_CAYL_AND_SINGLE_PHOTO_ABLUM)
        self.publish_on_haimeta_community(self.INTERACTED_IMAGE_1_XPATH, self.PUBLISH_BUTTON_XPATH_T2I_WITHE_REFINING, self.PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_T2I_WITHE_REFINING, self.CANCEL_PUBLISH_BUTTON_XPATH_T2I_WITHE_REFINING)
        self.report_the_image(self.INTERACTED_IMAGE_1_XPATH,self.THREE_DOTS_BUTTON_XPATH_T2I,self.REPORT_BUTTON_XPATH_T2I)
        self.delete_the_generated_image("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div",self.THREE_DOTS_BUTTON_XPATH_T2I,self.DELETE_BUTTON_XPATH_T2I)

    def common_step_for_T2I_without_refining(self,section_for_this_button_xpath,button_xpath):
        driver = self.driver
        wait = self.wait
        actions= self.actions
        self.open_the_certain_function(section_for_this_button_xpath,button_xpath)


        self.input_prompt_box_CLASS_NAME(self.INPUT_PROMPT_BOX_CLASS_NAME," blue sky")

        # choos the sytle
        self.click_action_check_by_visibility(self.STYLE_CHOICE_BUTTON_XPATH)
        # Select the size of generation 
        self.click_action_check_by_visibility(self.SIZE_OF_GENERATION_BUTTON_XPATH_T2I)


        # Select the number of images to generate
        self.click_action_check_by_visibility(self.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_T2I)
        self.click_create_button_xpath(self.CREATE_BUTTON_XPATH_T2I)
        # Wait for the loading to finish
        self.wait_for_loading_to_finish(item_class_name="_pictureEditorLoading_anlig_1",process_time_limitation=60)
        # interact with the image
        self.interact_with_the_second_item_selected(self.SECOND_ITEM_SELECTED_XPATH)
        self.download_image(self.INTERACTED_IMAGE_1_XPATH,self.DOWNLOAD_BUTTON_XPATH_CAYL_AND_SINGLE_PHOTO_ABLUM)
        self.publish_on_haimeta_community(self.INTERACTED_IMAGE_1_XPATH, self.PUBLISH_BUTTON_XPATH_SINGLE_PHOTO_ALBUM, self.PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_ID_PHOTO, self.CANCEL_PUBLISH_BUTTON_XPATH_T2I)
        self.report_the_image(self.INTERACTED_IMAGE_1_XPATH,self.THREE_DOTS_BUTTON_XPATH_T2I,self.REPORT_BUTTON_XPATH_T2I)
        self.delete_the_generated_image("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div",self.THREE_DOTS_BUTTON_XPATH_T2I,self.DELETE_BUTTON_XPATH_T2I)

    def test_create_nail_art(self):
        self.common_step_for_T2I_without_refining(self.WORK_SECTION_BUTTON_XPATH,self.CREATE_NAIL_ART_BUTTON_UNDER_WORK_SECTION_XPATH)
    def test_create_tattoo(self):
        self.common_step_for_T2I_without_refining(self.WORK_SECTION_BUTTON_XPATH,self.CREATE_TATTOO_BUTTON_UNDER_WORK_SECTION_XPATH)
    def test_create_toy(self):
        self.common_step_for_T2I(self.WORK_SECTION_BUTTON_XPATH,self.CREATE_TOY_BUTTON_UNDER_WORK_SECTION_XPATH)
    def test_create_character(self):
        self.common_step_for_T2I(self.WORK_SECTION_BUTTON_XPATH,self.CREATE_CHARACTER_BUTTON_UNDER_WORK_SECTION_XPATH)
    def test_create_logo(self):
        self.common_step_for_T2I(self.WORK_SECTION_BUTTON_XPATH,self.CREATE_LOGO_BUTTON_UNDER_WORK_SECTION_XPATH)
    
    def test_me_time(self):
        self.common_step_for_T2I(self.WORK_SECTION_BUTTON_XPATH,self.ME_TIME_BUTTON_UNDER_WORK_SECTION_XPATH)
    
    def test_stock_image(self):
        self.common_step_for_T2I(self.WORK_SECTION_BUTTON_XPATH,self.STOCK_IMAGE_BUTTON_UNDER_WORK_SECTION_XPATH)
    
    def test_texture_label(self):
        self.common_step_for_T2I(self.ART_SECTION_BUTTON_XPATH,self.TEXTURE_LABEL_BUTTON_UNDER_ART_SECTION_XPATH)
    
    def test_style(self):
        self.common_step_for_T2I(self.ART_SECTION_BUTTON_XPATH,self.STYLE_BUTTON_UNDER_ART_SECTION_XPATH)
    
    def test_create_wallpaper(self):
        self.common_step_for_T2I(self.ART_SECTION_BUTTON_XPATH,self.CREATE_WALLPAPER_BUTTON_UNDER_ART_SECTION_XPATH)
    
    def test_trendy_art(self):
        self.common_step_for_T2I(self.ART_SECTION_BUTTON_XPATH,self.TRENDY_ART_BUTTON_UNDER_ART_SECTION_XPATH)
    
    def test_pattern(self):
        self.common_step_for_T2I(self.WORK_SECTION_BUTTON_XPATH,self.PATTERN_BUTTON_UNDER_ART_SECTION_XPATH)

if __name__ == "__main__":
    unittest.main()