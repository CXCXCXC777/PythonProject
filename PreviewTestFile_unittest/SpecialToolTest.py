from BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Preview_config import ElementLocators


class Special_Tool_Test(BaseTest):
    def test_create_as_you_like(self):
        self.open_the_certain_function(ElementLocators.BUZZ_SECTION_BUTTON_XPATH, ElementLocators.CREATE_AS_YOU_LIKE_UNDER_BUZZ_SECTION_XPATH)

        self.input_prompt("a BIG volcano")
        self.refine_your_idea()

        self.select_the_size_of_the_generated_image(ElementLocators.SIZE_OF_GENERATION_BUTTON_XPATH)

        # Select the number of images to generate
        self.set_number_of_images_to_generate(ElementLocators.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH)
        # Click the generate button
        self.start_creation()

        self.interact_with_the_second_item_selected(ElementLocators.SECOND_ITEM_SELECTED_XPATH)
        # Interact with the generated images
        # Download the image
        self.download_image(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.DOWNLOAD_BUTTON_XPATH)
        # Publish the image
        self.publish_on_haimeta_community(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.PUBLISH_BUTTON_XPATH, ElementLocators.PUBLISH_INTERACTION_ELEMENT_ON_HAIMETA_COMMUNITY, ElementLocators.PUBLISH_INTERACTION_ELEMENT_ON_HAIMETA_COMMUNITY)
        # Publish the image on style library
        self.publish_on_style_library(ElementLocators.INTERACTED_IMAGE_1_XPATH)
        
        # Report the image
        self.report_the_image(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.THREE_DOTS_BUTTON_XPATH, ElementLocators.REPORT_BUTTON_XPATH)

        # Switch to English
        self.switch_language(
            target_language="English",
            language_selection_XPATH=ElementLocators.LANGUAGE_SELECTION_XPATH,
            language_switch_xpath=ElementLocators.SWITCH_TO_ENGLISH_LANGUAGE_XPATH,
            expected_title_text="Create As You Like",
            expected_title_class_name="title-item.global-font-title-small"
        )
        # Switch to Chinese
        self.switch_language(
            target_language="Chinese",
            language_selection_XPATH=ElementLocators.LANGUAGE_SELECTION_XPATH,
            language_switch_xpath=ElementLocators.SWITCH_TO_SIMPLIFIED_CHINESE_LANGUAGE_XPATH,
            expected_title_text="风格创作",
            expected_title_class_name="title-item.global-font-title-small"
        )


    def test_create_clothes(self):
        driver=self.driver
        wait= self.wait
        actions= self.actions
        self.open_the_certain_function(ElementLocators.WORK_SECTION_BUTTON_XPATH,ElementLocators.CREATE_CLOTHES_BUTTON_UNDER_WORK_SECTION)
        self.input_prompt("Volcano")
        self.refine_your_idea()
        # select the pattern style
        self.click_action_check_by_visibility(ElementLocators.STYLE_CHOICE_BUTTON_XPATH)

        # select the clothing style
        self.click_action_check_by_presence(ElementLocators.CLOTHING_STYLE_BUTTON_XPATH)

        # Click the generate button
        self.start_creation()
        #interact with the generated images
        self.interact_with_the_generated_create_clothes_image()

        # test image 2 image
        add_new_item_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, ElementLocators.ADD_NEW_IMAGE_BUTTON_XPATH))
        )
        actions.move_to_element(add_new_item_button_click).double_click().perform()

        I2I_Button_click=driver.find_element(By.XPATH,ElementLocators.SWITCH_TASK_I2I_XPATH)
        actions.move_to_element(I2I_Button_click).double_click().perform()

        #upload image
        self.upload_image(ElementLocators.UPLOAD_BUTTON_XPATH, ElementLocators.TEST_IMAGE)
        # chose the clothing style
        self.click_action_check_by_visibility(ElementLocators.STYLE_CHOICE_BUTTON_XPATH)
        self.start_creation()
        self.interact_with_the_generated_image()

    def test_style_your_pet(self):
       # open the pet section
       self.open_the_certain_function(ElementLocators.PET_SECTION_BUTTON_XPATH,ElementLocators.STYLE_YOUR_PET_ON_HOME_UNDER_PET_SECTION_XPATH)
       # add pet data set
       self.click_action_check_by_visibility(ElementLocators.ADD_PET_DATA_SET_BUTTON_XPATH)
       # upload image
       self.upload_image(ElementLocators.UPLOAD_BUTTON_XPATH, ElementLocators.PET_IMAGE_DATA_SET)
       # 退出训练
       self.click_action_check_by_visibility(ElementLocators.CLOSE_WINDOWS_BUTTON_XPATH)
        # set the style for the pet
       self.click_action_check_by_visibility(ElementLocators.STYLE_CHOICE_BUTTON_XPATH)

       # set the number of image to generate
       self.click_action_check_by_element_to_be_clickable(ElementLocators.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH)

       self.start_creation()

       #interact with the generated images
       self.interact_with_the_generated_image()


    def test_character_stickers(self):
        self.open_the_certain_function(ElementLocators.ART_SECTION_BUTTON_XPATH, ElementLocators.CHARACTER_STICKERS_UNDER_ART_BUTTON_XPATH)
        self.upload_image(ElementLocators.UPLOAD_BUTTON_XPATH, ElementLocators.TEST_FEMALE_PHOTO)
        self.start_creation()
        # interact with the image
        self.interact_with_the_generated_image()

