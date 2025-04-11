import unittest

from BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Image2ImageTest(BaseTest):

    def common_step_for_I2I(self, section_for_this_button_xpath,button_xpath,upload_image_absolute_path,stylc_choice):
        self.open_the_certain_function(section_for_this_button_xpath,button_xpath)

        self.upload_image(self.UPLOAD_IMAGE_BUTTON_XPATH_I2I,upload_image_absolute_path)

        # choose the style
        self.click_action_check_by_visibility(stylc_choice)

        # Select the size of generation
        self.click_action_check_by_visibility(self.SIZE_OF_GENERATION_BUTTON_XPATH_I2I)

        # Select the number of images to generate
        self.click_action_check_by_visibility(self.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_I2I)

        self.click_create_button_xpath(self.CREATE_BUTTON_XPATH_I2I)
        # Wait for the loading to finish
        self.wait_for_loading_to_finish(item_class_name="_pictureEditorLoading_anlig_1", process_time_limitation=60)
        # interact with the image
        self.interact_with_the_second_item_selected(self.SECOND_ITEM_SELECTED_XPATH)
        self.download_image(self.INTERACTED_IMAGE_1_XPATH, self.DOWNLOAD_BUTTON_XPATH_I2I)
        self.publish_on_haimeta_community(self.INTERACTED_IMAGE_1_XPATH, self.PUBLISH_BUTTON_XPATH_I2I,
                                          self.PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_I2I,
                                          self.CANCEL_PUBLISH_BUTTON_XPATH_I2I)
        self.report_the_image(self.INTERACTED_IMAGE_1_XPATH, self.THREE_DOTS_BUTTON_XPATH_I2I, self.REPORT_BUTTON_XPATH_I2I)
        self.delete_the_generated_image("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div",
                                        self.THREE_DOTS_BUTTON_XPATH_I2I, self.DELETE_BUTTON_XPATH_I2I)

    def common_step_for_I2I_character_texture(self, section_for_this_button_xpath,button_xpath,upload_image_absolute_path):
        self.open_the_certain_function(section_for_this_button_xpath, button_xpath)

        self.upload_image(self.UPLOAD_IMAGE_BUTTON_XPATH_I2I, upload_image_absolute_path)

        # choose the style
        self.click_action_check_by_visibility(self.STYLE_CHOICE_BUTTON_XPATH_I2I_TEXTURE_TRANSFER)
        # Select the rendering result
        self.click_action_check_by_visibility(self.RENDERING_RESULT_XPATH_I2I)

        # Select the number of images to generate
        self.click_action_check_by_visibility(self.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_I2I)
        self.click_create_button_xpath(self.CREATE_BUTTON_XPATH_I2I)
        # Wait for the loading to finish
        self.wait_for_loading_to_finish(item_class_name="_pictureEditorLoading_anlig_1", process_time_limitation=60)
        # interact with the image
        self.interact_with_the_second_item_selected(self.SECOND_ITEM_SELECTED_XPATH)
        self.download_image(self.INTERACTED_IMAGE_1_XPATH, self.DOWNLOAD_BUTTON_XPATH_I2I)
        self.publish_on_haimeta_community(self.INTERACTED_IMAGE_1_XPATH, self.PUBLISH_BUTTON_XPATH_I2I,
                                          self.PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_I2I,
                                          self.CANCEL_PUBLISH_BUTTON_XPATH_I2I)
        self.report_the_image(self.INTERACTED_IMAGE_1_XPATH, self.THREE_DOTS_BUTTON_XPATH_I2I, self.REPORT_BUTTON_XPATH_I2I)
        self.delete_the_generated_image("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div",
                                        self.THREE_DOTS_BUTTON_XPATH_I2I, self.DELETE_BUTTON_XPATH_I2I)

    def common_step_for_I2I_personal_avatar(self, section_for_this_button_xpath,button_xpath,upload_image_absolute_path):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        self.open_the_certain_function(section_for_this_button_xpath,button_xpath)


        self.upload_image(self.UPLOAD_IMAGE_BUTTON_XPATH_I2I, upload_image_absolute_path)

        # choose the style
        self.click_action_check_by_visibility(self.STYLE_CHOICE_BUTTON_XPATH_I2I)
        # Select the number of images to generate
        self.click_action_check_by_visibility(self.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_I2I_PERSONAL_AVATAR)
        self.click_create_button_xpath(self.CREATE_BUTTON_XPATH_I2I)
        # Wait for the loading to finish
        self.wait_for_loading_to_finish(item_class_name="_pictureEditorLoading_anlig_1", process_time_limitation=60)
        # interact with the image
        self.interact_with_the_second_item_selected(self.SECOND_ITEM_SELECTED_XPATH)
        self.download_image(self.INTERACTED_IMAGE_1_XPATH, self.DOWNLOAD_BUTTON_XPATH_I2I)
        self.publish_on_haimeta_community(self.INTERACTED_IMAGE_1_XPATH, self.PUBLISH_BUTTON_XPATH_I2I,
                                          self.PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_I2I,
                                          self.CANCEL_PUBLISH_BUTTON_XPATH_I2I)
        self.report_the_image(self.INTERACTED_IMAGE_1_XPATH, self.THREE_DOTS_BUTTON_XPATH_I2I, self.REPORT_BUTTON_XPATH_I2I)
        self.delete_the_generated_image("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div",
                                        self.THREE_DOTS_BUTTON_XPATH_I2I, self.DELETE_BUTTON_XPATH_I2I)

    def common_step_for_I2I_home_design(self, section_for_this_button_xpath,button_xpath,upload_image_absolute_path,style_choice):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        self.open_the_certain_function(section_for_this_button_xpath, button_xpath)


        self.upload_image(self.UPLOAD_IMAGE_BUTTON_XPATH_I2I, upload_image_absolute_path)

        # choose the style
        style_choice_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, style_choice))
        )
        style_choice_button_click.click()
        self.click_action_check_by_visibility(style_choice)

        # Select the number of images to generate
        self.click_action_check_by_visibility(self.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_I2I_HOME_DESIGN)
        
        self.click_create_button_xpath(self.CREATE_BUTTON_XPATH_I2I)
        # Wait for the loading to finish
        self.wait_for_loading_to_finish(item_class_name="_pictureEditorLoading_anlig_1", process_time_limitation=60)
        # interact with the image
        self.interact_with_the_second_item_selected(self.SECOND_ITEM_SELECTED_XPATH)
        self.download_image(self.INTERACTED_IMAGE_1_XPATH, self.DOWNLOAD_BUTTON_XPATH_I2I)
        self.publish_on_haimeta_community(self.INTERACTED_IMAGE_1_XPATH, self.PUBLISH_BUTTON_XPATH_I2I,
                                          self.PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_I2I,
                                          self.CANCEL_PUBLISH_BUTTON_XPATH_I2I)
        self.report_the_image(self.INTERACTED_IMAGE_1_XPATH, self.THREE_DOTS_BUTTON_XPATH_I2I, self.REPORT_BUTTON_XPATH_I2I)
        self.delete_the_generated_image("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div",
                                        self.THREE_DOTS_BUTTON_XPATH_I2I, self.DELETE_BUTTON_XPATH_I2I)

    def test_character_texture(self):
        self.common_step_for_I2I_character_texture(self.WORK_SECTION_BUTTON_XPATH,self.CHARACTER_TEXTURE_BUTTON_UNDER_WORK_SECTION_XPATH,self.TEST_IP_IMAGE)
    def test_personal_avatar(self):
        self.common_step_for_I2I_personal_avatar(self.ART_SECTION_BUTTON_XPATH,self.PERSONAL_AVATAR_BUTTON_UNDER_ART_SECTION_XPATH,self.TEST_MALE_PHOTO)
    def test_character_portrait_studio(self):
        self.common_step_for_I2I(self.WORK_SECTION_BUTTON_XPATH,self.CHARACTER_PORTRAIT_STUDIO_BUTTON_UNDER_WORK_SECTION_XPATH,self.TEST_IP_IMAGE,self.STYLE_CHOICE_BUTTON_XPATH_I2I)
    def test_create_product_photos(self):
        self.common_step_for_I2I(self.WORK_SECTION_BUTTON_XPATH,self.CREATE_PRODUCT_UNDER_WORK_BUTTON_XPATH, self.TEST_PRODUCT_IMAGE,self.STYLE_CHOICE_BUTTON_XPATH_I2I)
    def test_dream_home_design(self):
        self.common_step_for_I2I_home_design(self.BUZZ_SECTION_BUTTON_XPATH,self.DREAM_HOME_DESIGN_UNDER_BUZZ_SECTION_XPATH,self.TEST_HOME_DESIGN_IMAGE,self.STYLE_CHOICE_BUTTON_XPATH_I2I_HOME_DESIGN)
if __name__ == "__main__":
    unittest.main()