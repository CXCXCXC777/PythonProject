from BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait

class Special_Tool_Test(BaseTest):
    def test_create_as_you_like(self):
        driver = self.driver
        wait = self.wait
        self.open_the_certain_function(self.BUZZ_SECTION_BUTTON_XPATH,self.CREATE_AS_YOU_LIKE_UNDER_BUZZ_BUTTON_XPATH)

        self.input_prompt_box_CLASS_NAME(self.INPUT_PROMPT_BOX_CLASS_NAME,"a beautiful girl")
        self.refine_your_idea()

        self.select_the_size_of_the_generated_image(self.SIZE_OF_GENERATION_BUTTON_XPATH)

        # Select the number of images to generate
        self.set_number_of_images_to_generate(self.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH)
        # Click the generate button
        self.click_create_button_class_name(self.GENERATE_BUTTON_CLASS_NAME)
        # Wait for the loading to finish
        self.wait_for_loading_to_finish(item_class_name="_pictureEditorLoading_anlig_1",process_time_limitation=30)

        # Interact with the generated images
        # Download the image
        self.download_image(self.INTERACTED_IMAGE_1_XPATH, self.DOWNLOAD_BUTTON_XPATH_CAYL_AND_SINGLE_PHOTO_ABLUM)
        # Publish the image
        self.publish_on_haimeta_community(self.INTERACTED_IMAGE_1_XPATH, self.PUBLISH_BUTTON_XPATH_CAYL, self.PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_CAYL, self.CANCEL_PUBLISH_BUTTON_XPATH_CAYL)
        # Publish the image on style library
        self.publish_on_style_library(item_to_publish_XPATH=self.INTERACTED_IMAGE_1_XPATH)
        
        # Report the image
        self.report_the_image(self.INTERACTED_IMAGE_1_XPATH,self.THREE_DOTS_BUTTON_XPATH_CAYL,self.REPORT_BUTTON_AFTER_PUBLISH_ON_STYLE_LIBRARY_XPATH)

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


    def test_create_clothes(self):
        driver=self.driver
        wait= self.wait
        actions= self.actions
        self.open_the_certain_function(self.WORK_SECTION_BUTTON_XPATH,self.CREATE_CLOTHES_BUTTON_UNDER_WORK_SECTION)
        

        self.input_prompt_box_CLASS_NAME(self.INPUT_PROMPT_BOX_CLASS_NAME,"A big and cut lion")
        
        self.refine_your_idea()
        # Wait for the loading to finish
        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, self.REFINE_YOUR_IDEA_BUTTON_XPATH))
        )

        # Click the generate button
        generate_button_click = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, self.GENERATE_BUTTON_CLASS_NAME))
        )
        generate_button_click.click()
        self.click_create_button_class_name(self.GENERATE_BUTTON_CLASS_NAME)
        # Wait for the loading to finish
        self.wait_for_loading_to_finish(item_class_name="_pictureEditorLoading_anlig_1",process_time_limitation=50)

        #interact with the generated images

        self.interact_with_the_second_item_selected(self.SECOND_ITEM_SELECTED_XPATH)


        # Download the image
        self.download_image(self.INTERACTED_IMAGE_1_XPATH, self.DOWNLOAD_BUTTON_XPATH_CAYL_AND_SINGLE_PHOTO_ABLUM)
        # Publish the image
        self.publish_on_haimeta_community(self.INTERACTED_IMAGE_1_XPATH, self.PUBLISH_BUTTON_XPATH_CAYL, self.PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_CAYL, self.CANCEL_PUBLISH_BUTTON_XPATH_CAYL)
        # Report the image
        self.report_the_image(self.INTERACTED_IMAGE_1_XPATH,self.THREE_DOTS_BUTTON_XPATH_CAYL,self.REPORT_BUTTON_CREATE_CLOTHES_XPATH)

        # Download Pattern

        wait.until(EC.invisibility_of_element_located((By.XPATH, self.REPORT_TYPE_BUTTON_XPATH)))

        download_pattern_button_click = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.DOWNLOAD_PATTERN_BUTTON_XPATH))
        )
        download_pattern_button_click.click()

        # test image 2 image
        add_new_item_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.ADD_NEW_IMAGE_BUTTON_XPATH))
        )
        add_new_item_button_click.click()

        I2I_Button_click=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[2]")
        self.click_action_check_by_presence(I2I_Button_click)

        #upload image
        self.upload_image(self.UPLOAD_IMAGE_CREATE_CLOTHES_XPATH, self.TEST_IMAGE)
        
        self.click_action_check_by_element_to_be_clickable(self.GENERATE_BUTTON_CLASS_NAME)
        # Wait for the loading to finish
        self.wait_for_loading_to_finish(item_class_name="_pictureEditorLoading_anlig_1",process_time_limitation=30)

    def test_style_your_pet(self):
       driver=self.driver
       actions=self.actions
       wait=self.wait

       # open the pet section
       self.open_the_certain_function(self.PET_SECTION_BUTTON_XPATH,self.STYLE_YOUR_PET_ON_HOME_UNDER_PET_SECTION_XPATH)

       # add pet data set
       self.click_action_check_by_visibility(self.ADD_PET_DATA_SET_BUTTON_XPATH)
       # upload image
       self.upload_image(self.UPLOAD_IMAGE_STYLE_YOUR_PET_XPATH, self.PET_IMAGE_DATA_SET)
       # wait for the loading to finish
       wait.until(EC.element_to_be_clickable((By.XPATH, self.START_TRAINING_BUTTON_XPATH)))
       # start training
       self.click_action_check_by_visibility(self.START_TRAINING_BUTTON_XPATH)

       # 退出训练
       driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[3]/div/div[1]/div/div/div[1]/i").click()
       
        # set the style for the pet
       self.click_action_check_by_visibility("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div[1]/div")
       
       # set the number of image to generate
       driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[4]/div/div/div/div[1]").click()

       self.click_create_button_xpath(self.CREATE_BUTTON_XPATH_STYLE_YOUR_PET)
       # wait for the loading to finish
       self.wait_for_loading_to_finish(item_class_name="_pictureEditorLoading_anlig_1",process_time_limitation=50)

       #interact with the generated images
       self.interact_with_the_second_item_selected(self.SECOND_ITEM_SELECTED_XPATH)

       # Download the image
       self.download_image(self.INTERACTED_IMAGE_1_XPATH, self.DOWNLOAD_BUTTON_XPATH_CAYL_AND_SINGLE_PHOTO_ABLUM)
       # Publish the image
       self.publish_on_haimeta_community(self.INTERACTED_IMAGE_1_XPATH, self.PUBLISH_BUTTON_XPATH_SINGLE_PHOTO_ALBUM, self.PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_ID_PHOTO, self.PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_ID_PHOTO)
       # Report the image
       self.report_the_image(self.INTERACTED_IMAGE_1_XPATH,self.THREE_DOTS_BUTTON_XPATH_SINGLE_PHOTO_ALBUM,self.REPORT_BUTTON_XPATH_ID_PHOTO_SINGLE_PHOTO_ALBUM)

       self.delete_the_generated_image(self.INTERACTED_IMAGE_1_XPATH,self.THREE_DOTS_BUTTON_XPATH_SINGLE_PHOTO_ALBUM,"/html/body/div[9]/div/ul/li[1]/span/div/p")

    def test_character_stickers(self):
        self.open_the_certain_function(self.ART_SECTION_BUTTON_XPATH, self.CHARACTER_STICKERS_UNDER_ART_BUTTON_XPATH)

        self.upload_image(self.UPLOAD_IMAGE_BUTTON_XPATH_I2I, self.TEST_FEMALE_PHOTO)

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
        self.delete_the_generated_image(
            "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div",
            self.THREE_DOTS_BUTTON_XPATH_I2I, self.DELETE_BUTTON_XPATH_I2I)

