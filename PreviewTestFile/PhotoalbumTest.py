from BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class Photo_Album_Test(BaseTest):
    def test_id_photo(self):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        self.open_the_certain_function(self.PHOTO_ALBUM_SECTION_BUTTON_XPATH,self.ID_PHOTO_BUTTON_XPATH)
        self.upload_image(self.PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,self.TEST_FEMALE_PHOTO)
        self.choose_style_skin_texture_of_generated_image(self.CHOOSE_PHOTO_GENERATION_STYLE_XPATH,self.INPUT_SKIN_TEXTURE_ID_PHOTO_XPATH)
        self.click_create_button_xpath(self.CREATE_BUTTON_XPATH)
        self.wait_for_loading_to_finish(item_class_name="_pictureEditorLoading_anlig_1",process_time_limitation=50)

        second_item_selected = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.SECOND_ITEM_SELECTED_XPATH))
        )
        actions.move_to_element(second_item_selected).click().perform()

        #interact with the generated images
        self.download_image(self.ITEM_TO_BE_INTERACTED_XPATH_ID,self.DOWNLOAD_BUTTON_XPATH_ID_PHOTO)
        self.publish_on_haimeta_community(self.ITEM_TO_BE_INTERACTED_XPATH_ID, self.PUBLISH_BUTTON_XPATH_ID_PHOTO, self.PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_ID_PHOTO, self.CANCEL_PUBLISH_BUTTON_XPATH_ID_PHOTO)
        self.report_the_image(self.INTERACTED_IMAGE_1_XPATH,self.THREE_DOTS_BUTTON_XPATH_ID_PHOTO,self.REPORT_BUTTON_XPATH_ID_PHOTO_SINGLE_PHOTO_ALBUM)
        
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
        self.open_the_certain_function(self.PHOTO_ALBUM_SECTION_BUTTON_XPATH,self.CHINESE_AESTHETICS_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(self.PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,self.TEST_FEMALE_PHOTO)
        # following up steps are the sam eas the signle photo album
        self.choose_style_skin_texture_of_generated_image(self.CHOOSE_PHOTO_GENERATION_STYLE_XPATH,self.INPUT_SKIN_TEXTURE_SINGLE_PHOTO_ALBUM)

        # set the number of images to generate
        self.interact_with_single_photo_album()

    def test_arabian_dreams(self):
        self.open_the_certain_function(self.PHOTO_ALBUM_SECTION_BUTTON_XPATH,self.ARABIAN_DREAMS_BUTTON_XPATH)
        self.upload_image(self.PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,self.TEST_FEMALE_PHOTO)
        self.interact_with_single_photo_album()


    
    def test_nanyang_memory(self):
        self.open_the_certain_function(self.PHOTO_ALBUM_SECTION_BUTTON_XPATH,self.NANYANG_MEMORY_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(self.PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,self.TEST_MALE_PHOTO)
        self.interact_with_single_photo_album()

        
    def test_gorgeous_road(self):
        self.open_the_certain_function(self.PHOTO_ALBUM_SECTION_BUTTON_XPATH,self.GORGEOUS_ROAD_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(self.PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,self.TEST_FEMALE_PHOTO)
        self.interact_with_single_photo_album()

    def test_east_asian_culture(self):
        self.open_the_certain_function(self.PHOTO_ALBUM_SECTION_BUTTON_XPATH,self.EAST_ASIAN_CULTURE_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(self.PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,self.TEST_MALE_PHOTO)
        self.interact_with_single_photo_album()


    def test_cyber_future(self):
        self.open_the_certain_function(self.PHOTO_ALBUM_SECTION_BUTTON_XPATH,self.CYBER_FUTURE_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(self.PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,self.TEST_FEMALE_PHOTO)
        self.interact_with_single_photo_album()


    def test_fantasy_tales(self):
        self.open_the_certain_function(self.PHOTO_ALBUM_SECTION_BUTTON_XPATH,self.FANTASY_TALES_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(self.PHOTO_ALBUM_UPLOAD_BUTTON_XPATH,self.TEST_FEMALE_PHOTO)
        self.interact_with_single_photo_album()
    
    def test_love_in_the_air(self):
        self.open_the_certain_function(self.PHOTO_ALBUM_SECTION_BUTTON_XPATH,self.LOVE_IN_THE_AIR_BUTTON_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(self.FIRST_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM,self.TEST_MALE_PHOTO)
        self.upload_image(self.SECOND_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM,self.TEST_FEMALE_PHOTO)
        self.interact_with_single_photo_album()

    
    def test_BFF_moments(self):
        self.open_the_certain_function(self.PHOTO_ALBUM_SECTION_BUTTON_XPATH,self.BFF_MOMENT_BUTTON_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(self.FIRST_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM,self.TEST_FEMALE_PHOTO)
        self.upload_image(self.SECOND_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM,self.TEST_FEMALE_PHOTO)
        self.interact_with_single_photo_album()

    def test_bro_show(self):
        self.open_the_certain_function(self.PHOTO_ALBUM_SECTION_BUTTON_XPATH,self.BRO_SHOW_BUTTON_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(self.FIRST_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM,self.TEST_MALE_PHOTO)
        self.upload_image(self.SECOND_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM,self.TEST_MALE_PHOTO)
        self.interact_with_single_photo_album()