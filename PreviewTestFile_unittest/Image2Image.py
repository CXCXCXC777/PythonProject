import unittest

from BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Preview_config import ElementLocators


class Image2ImageTest(BaseTest):

    def common_step_for_I2I(self, section_for_this_button_xpath,button_xpath,upload_image_absolute_path,stylc_choice):
        self.open_the_certain_function(section_for_this_button_xpath,button_xpath)

        self.upload_image(ElementLocators.UPLOAD_BUTTON_XPATH,upload_image_absolute_path)

        # choose the style
        self.click_action_check_by_visibility(stylc_choice)

        # Select the size of generation
        self.click_action_check_by_visibility(ElementLocators.SIZE_OF_GENERATION_BUTTON_XPATH)

        # Select the number of images to generate
        self.click_action_check_by_visibility(ElementLocators.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH)

        self.click_create_button_xpath(ElementLocators.CREATE_BUTTON_XPATH)
        # Wait for the loading to finish
        self.wait_for_loading_to_finish(ElementLocators.PICTURE_EDITOR_LOADING_CLASS_NAME, process_time_limitation=60)
        # interact with the image
        self.interact_with_the_second_item_selected(ElementLocators.SECOND_ITEM_SELECTED_XPATH)
        self.download_image(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.DOWNLOAD_BUTTON_XPATH)
        self.publish_on_haimeta_community(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.PUBLISH_BUTTON_XPATH,
                                          ElementLocators.PUBLISH_INTERACTION_ELEMENT_ON_HAIMETA_COMMUNITY,
                                          ElementLocators.PUBLISH_INTERACTION_ELEMENT_ON_HAIMETA_COMMUNITY)
        self.report_the_image(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.THREE_DOTS_BUTTON_XPATH, ElementLocators.REPORT_BUTTON_XPATH)
        self.delete_the_generated_image(ElementLocators.INTERACTED_IMAGE_1_XPATH,
                                        ElementLocators.THREE_DOTS_BUTTON_XPATH, ElementLocators.DELETE_BUTTON_XPATH)

    def common_step_for_I2I_character_texture(self, section_for_this_button_xpath,button_xpath,upload_image_absolute_path):
        self.open_the_certain_function(section_for_this_button_xpath, button_xpath)

        self.upload_image(ElementLocators.UPLOAD_BUTTON_XPATH, upload_image_absolute_path)

        # choose the style
        self.click_action_check_by_visibility(ElementLocators.STYLE_CHOICE_BUTTON_XPATH)
        # Select the rendering result
        self.click_action_check_by_visibility(ElementLocators.RENDERING_RESULT_XPATH_I2I)

        # Select the number of images to generate
        self.click_action_check_by_visibility(ElementLocators.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH)
        self.click_create_button_xpath(ElementLocators.CREATE_BUTTON_XPATH)
        # Wait for the loading to finish
        self.wait_for_loading_to_finish(ElementLocators.PICTURE_EDITOR_LOADING_CLASS_NAME, process_time_limitation=60)
        # interact with the image
        self.interact_with_the_second_item_selected(ElementLocators.SECOND_ITEM_SELECTED_XPATH)
        self.download_image(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.DOWNLOAD_BUTTON_XPATH)
        self.publish_on_haimeta_community(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.PUBLISH_BUTTON_XPATH ,
                                          ElementLocators.PUBLISH_INTERACTION_ELEMENT_ON_HAIMETA_COMMUNITY ,
                                          ElementLocators.PUBLISH_INTERACTION_ELEMENT_ON_HAIMETA_COMMUNITY)
        self.report_the_image(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.THREE_DOTS_BUTTON_XPATH, ElementLocators.REPORT_BUTTON_XPATH)
        self.delete_the_generated_image(ElementLocators.INTERACTED_IMAGE_1_XPATH,
                                        ElementLocators.THREE_DOTS_BUTTON_XPATH, ElementLocators.DELETE_BUTTON_XPATH)

    def common_step_for_I2I_personal_avatar(self, section_for_this_button_xpath,button_xpath,upload_image_absolute_path):
        self.open_the_certain_function(section_for_this_button_xpath,button_xpath)
        self.upload_image(ElementLocators.UPLOAD_BUTTON_XPATH, upload_image_absolute_path)
        # choose the style
        self.click_action_check_by_visibility(ElementLocators.STYLE_CHOICE_BUTTON_XPATH)
        # Select the number of images to generate
        self.click_action_check_by_visibility(ElementLocators.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH)
        self.click_create_button_xpath(ElementLocators.CREATE_BUTTON_XPATH)
        # Wait for the loading to finish
        self.wait_for_loading_to_finish(ElementLocators.PICTURE_EDITOR_LOADING_CLASS_NAME, process_time_limitation=60)
        # interact with the image
        self.interact_with_the_second_item_selected(ElementLocators.SECOND_ITEM_SELECTED_XPATH)
        self.download_image(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.DOWNLOAD_BUTTON_XPATH)
        self.publish_on_haimeta_community(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.PUBLISH_BUTTON_XPATH ,
                                          ElementLocators.PUBLISH_INTERACTION_ELEMENT_ON_HAIMETA_COMMUNITY ,
                                          ElementLocators.PUBLISH_INTERACTION_ELEMENT_ON_HAIMETA_COMMUNITY)
        self.report_the_image(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.THREE_DOTS_BUTTON_XPATH, ElementLocators.REPORT_BUTTON_XPATH)
        self.delete_the_generated_image(ElementLocators.INTERACTED_IMAGE_1_XPATH,ElementLocators.THREE_DOTS_BUTTON_XPATH, ElementLocators.DELETE_BUTTON_XPATH)

    def common_step_for_I2I_home_design(self, section_for_this_button_xpath,button_xpath,upload_image_absolute_path,style_choice):
        self.open_the_certain_function(section_for_this_button_xpath, button_xpath)


        self.upload_image(ElementLocators.UPLOAD_BUTTON_XPATH, upload_image_absolute_path)

        # choose the style
        self.click_action_check_by_visibility(style_choice)

        # Select the number of images to generate
        self.click_action_check_by_visibility(ElementLocators.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH)
        
        # self.click_create_button_xpath(ElementLocators.CREATE_BUTTON_XPATH)
        # Wait for the loading to finish
        # self.wait_for_loading_to_finish(ElementLocators.PICTURE_EDITOR_LOADING_CLASS_NAME, process_time_limitation=60)
        # interact with the image
        self.interact_with_the_second_item_selected(ElementLocators.SECOND_ITEM_SELECTED_XPATH)
        self.download_image(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.DOWNLOAD_BUTTON_XPATH)
        self.publish_on_haimeta_community()
        self.report_the_image(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.THREE_DOTS_BUTTON_XPATH, ElementLocators.REPORT_BUTTON_XPATH)
        self.delete_the_generated_image(ElementLocators.INTERACTED_IMAGE_1_XPATH,
                                        ElementLocators.THREE_DOTS_BUTTON_XPATH, ElementLocators.DELETE_BUTTON_XPATH)

    def test_character_texture(self):
        self.common_step_for_I2I_character_texture(ElementLocators.WORK_SECTION_BUTTON_XPATH,ElementLocators.CHARACTER_TEXTURE_BUTTON_UNDER_WORK_SECTION_XPATH,ElementLocators.TEST_IP_IMAGE)
    def test_personal_avatar(self):
        self.common_step_for_I2I_personal_avatar(ElementLocators.ART_SECTION_BUTTON_XPATH,ElementLocators.PERSONAL_AVATAR_BUTTON_UNDER_ART_SECTION_XPATH,ElementLocators.TEST_MALE_PHOTO)
    def test_character_portrait_studio(self):
        self.common_step_for_I2I(ElementLocators.WORK_SECTION_BUTTON_XPATH,ElementLocators.CHARACTER_PORTRAIT_STUDIO_BUTTON_UNDER_WORK_SECTION_XPATH,ElementLocators.TEST_IP_IMAGE,ElementLocators.STYLE_CHOICE_BUTTON_XPATH)
    def test_create_product_photos(self):
        self.common_step_for_I2I(ElementLocators.WORK_SECTION_BUTTON_XPATH,ElementLocators.CREATE_PRODUCT_UNDER_WORK_BUTTON_XPATH, ElementLocators.TEST_PRODUCT_IMAGE,ElementLocators.STYLE_CHOICE_BUTTON_XPATH)
    def test_dream_home_design(self):
        self.common_step_for_I2I_home_design(ElementLocators.BUZZ_SECTION_BUTTON_XPATH,ElementLocators.DREAM_HOME_DESIGN_UNDER_BUZZ_SECTION_XPATH,ElementLocators.TEST_HOME_DESIGN_IMAGE,ElementLocators.STYLE_CHOICE_BUTTON_XPATH)
if __name__ == "__main__":
    unittest.main()