import unittest

from selenium.webdriver.common import action_chains, actions
from urllib3.util import wait
from BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from Preview_config import ElementLocators
from selenium.webdriver.support.ui import WebDriverWait

class Text2Image_Test(BaseTest):
    def common_step_for_T2I(self,section_for_this_button_xpath,button_xpath):
    
        driver = self.driver
        self.open_the_certain_function(section_for_this_button_xpath,button_xpath)

        self.input_prompt_box_XPATH(ElementLocators.INPUT_PROMPT_BOX_XPATH, " blue sky")

        # Refine your idea
        try:
            self.click_action_check_by_visibility(ElementLocators.REFINE_YOUR_IDEA_BUTTON_XPATH)
            # Wait for the loading to finish
            WebDriverWait(driver, 50).until(
                EC.visibility_of_element_located((By.XPATH, ElementLocators.REFINE_YOUR_IDEA_BUTTON_XPATH))
            )
        except TimeoutError:
            pass  # Skip if the button is not found

        # choose the style
        self.click_action_check_by_visibility(ElementLocators.STYLE_CHOICE_BUTTON_XPATH)
        # Select the size of generation 
        self.click_action_check_by_visibility(ElementLocators.SIZE_OF_GENERATION_BUTTON_XPATH)

        # Select the number of images to generate
        self.click_action_check_by_visibility(ElementLocators.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH)

        # self.click_create_button_xpath(ElementLocators.CREATE_BUTTON_XPATH )
        # # Wait for the loading to finish
        # self.wait_for_loading_to_finish(ElementLocators.PICTURE_EDITOR_LOADING_CLASS_NAME,process_time_limitation=60)
        # interact with the image
        self.interact_with_the_second_item_selected(ElementLocators.SECOND_ITEM_SELECTED_XPATH)
        self.download_image(ElementLocators.INTERACTED_IMAGE_1_XPATH,ElementLocators.DOWNLOAD_BUTTON_XPATH)
        self.publish_on_haimeta_community(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.PUBLISH_BUTTON_XPATH, ElementLocators.PUBLISH_INTERACTION_ELEMENT_ON_HAIMETA_COMMUNITY, ElementLocators.PUBLISH_INTERACTION_ELEMENT_ON_HAIMETA_COMMUNITY)
        self.report_the_image(ElementLocators.INTERACTED_IMAGE_1_XPATH,ElementLocators.THREE_DOTS_BUTTON_XPATH,ElementLocators.REPORT_BUTTON_XPATH)
        self.delete_the_generated_image(ElementLocators.INTERACTED_IMAGE_1_XPATH,ElementLocators.THREE_DOTS_BUTTON_XPATH,ElementLocators.DELETE_BUTTON_XPATH)

    def common_step_for_T2I_without_refining(self,section_for_this_button_xpath,button_xpath):
        self.open_the_certain_function(section_for_this_button_xpath,button_xpath)


        self.input_prompt_box_XPATH(ElementLocators.INPUT_PROMPT_BOX_XPATH, " blue sky")

        # choose the style
        self.click_action_check_by_visibility(ElementLocators.STYLE_CHOICE_BUTTON_XPATH)
        # Select the size of generation 
        self.click_action_check_by_visibility(ElementLocators.SIZE_OF_GENERATION_BUTTON_XPATH)


        # Select the number of images to generate
        self.click_action_check_by_visibility(ElementLocators.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH)
        # self.click_create_button_xpath(ElementLocators.CREATE_BUTTON_XPATH)
        # # Wait for the loading to finish
        # self.wait_for_loading_to_finish(ElementLocators.PICTURE_EDITOR_LOADING_CLASS_NAME,process_time_limitation=60)
        # interact with the image
        self.interact_with_the_second_item_selected(ElementLocators.SECOND_ITEM_SELECTED_XPATH)
        self.download_image(ElementLocators.INTERACTED_IMAGE_1_XPATH,ElementLocators.DOWNLOAD_BUTTON_XPATH)
        self.publish_on_haimeta_community(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.PUBLISH_BUTTON_XPATH, ElementLocators.PUBLISH_INTERACTION_ELEMENT_ON_HAIMETA_COMMUNITY, ElementLocators.PUBLISH_INTERACTION_ELEMENT_ON_HAIMETA_COMMUNITY)
        self.report_the_image(ElementLocators.INTERACTED_IMAGE_1_XPATH,ElementLocators.THREE_DOTS_BUTTON_XPATH,ElementLocators.REPORT_BUTTON_XPATH)
        self.delete_the_generated_image(ElementLocators.INTERACTED_IMAGE_1_XPATH,ElementLocators.THREE_DOTS_BUTTON_XPATH,ElementLocators.DELETE_BUTTON_XPATH)

    def test_create_nail_art(self):
        self.common_step_for_T2I_without_refining(ElementLocators.WORK_SECTION_BUTTON_XPATH,ElementLocators.CREATE_NAIL_ART_BUTTON_UNDER_WORK_SECTION_XPATH)
    def test_create_tattoo(self):
        self.common_step_for_T2I_without_refining(ElementLocators.WORK_SECTION_BUTTON_XPATH,ElementLocators.CREATE_TATTOO_BUTTON_UNDER_WORK_SECTION_XPATH)
    def test_create_toy(self):
        self.common_step_for_T2I(ElementLocators.WORK_SECTION_BUTTON_XPATH,ElementLocators.CREATE_TOY_BUTTON_UNDER_WORK_SECTION_XPATH)
    def test_create_character(self):
        self.common_step_for_T2I(ElementLocators.WORK_SECTION_BUTTON_XPATH,ElementLocators.CREATE_CHARACTER_BUTTON_UNDER_WORK_SECTION_XPATH)
    def test_create_logo(self):
        self.common_step_for_T2I(ElementLocators.WORK_SECTION_BUTTON_XPATH,ElementLocators.CREATE_LOGO_BUTTON_UNDER_WORK_SECTION_XPATH)
    
    def test_me_time(self):
        self.common_step_for_T2I(ElementLocators.WORK_SECTION_BUTTON_XPATH,ElementLocators.ME_TIME_BUTTON_UNDER_WORK_SECTION_XPATH)
    
    def test_stock_image(self):
        self.common_step_for_T2I(ElementLocators.WORK_SECTION_BUTTON_XPATH,ElementLocators.STOCK_IMAGE_BUTTON_UNDER_WORK_SECTION_XPATH)
    
    def test_texture_label(self):
        self.common_step_for_T2I(ElementLocators.ART_SECTION_BUTTON_XPATH,ElementLocators.TEXTURE_LABEL_BUTTON_UNDER_ART_SECTION_XPATH)
    
    def test_style(self):
        self.common_step_for_T2I(ElementLocators.ART_SECTION_BUTTON_XPATH,ElementLocators.STYLE_BUTTON_UNDER_ART_SECTION_XPATH)
    
    def test_create_wallpaper(self):
        self.common_step_for_T2I(ElementLocators.ART_SECTION_BUTTON_XPATH,ElementLocators.CREATE_WALLPAPER_BUTTON_UNDER_ART_SECTION_XPATH)
    
    def test_trendy_art(self):
        self.common_step_for_T2I(ElementLocators.ART_SECTION_BUTTON_XPATH,ElementLocators.TRENDY_ART_BUTTON_UNDER_ART_SECTION_XPATH)
    
    def test_pattern(self):
        self.common_step_for_T2I(ElementLocators.WORK_SECTION_BUTTON_XPATH,ElementLocators.PATTERN_BUTTON_UNDER_ART_SECTION_XPATH)

if __name__ == "__main__":
    unittest.main()