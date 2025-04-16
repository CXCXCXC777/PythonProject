from BaseTest import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Preview_config import ElementLocators


class Photo_Album_Test(BaseTest):
    def test_id_photo(self):
        driver = self.driver
        wait = self.wait
        actions = self.actions
        self.open_the_certain_function(ElementLocators.PHOTO_ALBUM_SECTION_BUTTON_XPATH,ElementLocators.ID_PHOTO_BUTTON_XPATH)
        self.upload_image(ElementLocators.UPLOAD_BUTTON_XPATH,ElementLocators.TEST_FEMALE_PHOTO)
        self.choose_style_skin_texture_of_generated_image(ElementLocators.STYLE_CHOICE_BUTTON_XPATH,ElementLocators.INPUT_SKIN_TEXTURE)
        self.click_create_button_xpath(ElementLocators.CREATE_BUTTON_XPATH)
        self.wait_for_loading_to_finish(ElementLocators.PICTURE_EDITOR_LOADING_CLASS_NAME,process_time_limitation=50)

        second_item_selected = wait.until(
            EC.visibility_of_element_located((By.XPATH, ElementLocators.SECOND_ITEM_SELECTED_XPATH))
        )
        actions.move_to_element(second_item_selected).click().perform()

        #interact with the generated images
        self.download_image(ElementLocators.INTERACTED_IMAGE_1_XPATH,ElementLocators.DOWNLOAD_BUTTON_XPATH)
        self.publish_on_haimeta_community(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.PUBLISH_BUTTON_XPATH , ElementLocators.PUBLISH_INTERACTION_ELEMENT_ON_HAIMETA_COMMUNITY, ElementLocators.PUBLISH_INTERACTION_ELEMENT_ON_HAIMETA_COMMUNITY)
        self.report_the_image(ElementLocators.INTERACTED_IMAGE_1_XPATH,ElementLocators.THREE_DOTS_BUTTON_XPATH,ElementLocators.REPORT_BUTTON_XPATH)
        
        # Set up the Size of the generated image
        self.set_up_the_size_of_the_generated_image(ElementLocators.SET_SIZE_BUTTON_XPATH,ElementLocators.INS_SIZE_BUTTON_XPATH)
        # Set up the Layout of the generated image
        self.set_up_the_layout_of_the_generated_image(ElementLocators.SET_LAYOUT_BUTTON_XPATH,ElementLocators.FIVE_INCHES_LAYOUT_BUTTON_XPATH)

        # Download the generated images
        self.download_image(ElementLocators.INTERACTED_ITEM_PREVIEW_ITEM_XPATH, ElementLocators.DOWNLOAD_BUTTON_XPATH)
        self.set_up_the_layout_of_the_generated_image(ElementLocators.SET_LAYOUT_BUTTON_XPATH,ElementLocators.SINGLE_LAYOUT_BUTTON_XPATH)
        self.delete_the_generated_image(ElementLocators.INTERACTED_ITEM_PREVIEW_ITEM_XPATH,ElementLocators.THREE_DOTS_BUTTON_XPATH,ElementLocators.DELETE_BUTTON_XPATH)

    def test_chinese_aesthetics(self):
        self.open_the_certain_function(ElementLocators.PHOTO_ALBUM_SECTION_BUTTON_XPATH,ElementLocators.CHINESE_AESTHETICS_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(ElementLocators.UPLOAD_BUTTON_XPATH,ElementLocators.TEST_FEMALE_PHOTO)
        # set the number of images to generate
        self.interact_with_single_photo_album()

    def test_arabian_dreams(self):
        self.open_the_certain_function(ElementLocators.PHOTO_ALBUM_SECTION_BUTTON_XPATH,ElementLocators.ARABIAN_DREAMS_BUTTON_XPATH)
        self.upload_image(ElementLocators.UPLOAD_BUTTON_XPATH,ElementLocators.TEST_FEMALE_PHOTO)
        self.interact_with_single_photo_album()


    
    def test_nanyang_memory(self):
        self.open_the_certain_function(ElementLocators.PHOTO_ALBUM_SECTION_BUTTON_XPATH,ElementLocators.NANYANG_MEMORY_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(ElementLocators.UPLOAD_BUTTON_XPATH,ElementLocators.TEST_MALE_PHOTO)
        self.interact_with_single_photo_album()

        
    def test_gorgeous_road(self):
        self.open_the_certain_function(ElementLocators.PHOTO_ALBUM_SECTION_BUTTON_XPATH,ElementLocators.GORGEOUS_ROAD_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(ElementLocators.UPLOAD_BUTTON_XPATH,ElementLocators.TEST_FEMALE_PHOTO)
        self.interact_with_single_photo_album()

    def test_east_asian_culture(self):
        self.open_the_certain_function(ElementLocators.PHOTO_ALBUM_SECTION_BUTTON_XPATH,ElementLocators.EAST_ASIAN_CULTURE_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(ElementLocators.UPLOAD_BUTTON_XPATH,ElementLocators.TEST_MALE_PHOTO)
        self.interact_with_single_photo_album()


    def test_cyber_future(self):
        self.open_the_certain_function(ElementLocators.PHOTO_ALBUM_SECTION_BUTTON_XPATH,ElementLocators.CYBER_FUTURE_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(ElementLocators.UPLOAD_BUTTON_XPATH,ElementLocators.TEST_FEMALE_PHOTO)
        self.interact_with_single_photo_album()


    def test_fantasy_tales(self):
        self.open_the_certain_function(ElementLocators.PHOTO_ALBUM_SECTION_BUTTON_XPATH,ElementLocators.FANTASY_TALES_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(ElementLocators.UPLOAD_BUTTON_XPATH,ElementLocators.TEST_FEMALE_PHOTO)
        self.interact_with_single_photo_album()
    
    def test_love_in_the_air(self):
        self.open_the_certain_function(ElementLocators.PHOTO_ALBUM_SECTION_BUTTON_XPATH,ElementLocators.LOVE_IN_THE_AIR_BUTTON_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(ElementLocators.FIRST_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ALBUM,ElementLocators.TEST_MALE_PHOTO)
        self.upload_image(ElementLocators.SECOND_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ALBUM,ElementLocators.TEST_FEMALE_PHOTO)
        self.interact_with_single_photo_album()

    
    def test_BFF_moments(self):
        self.open_the_certain_function(ElementLocators.PHOTO_ALBUM_SECTION_BUTTON_XPATH,ElementLocators.BFF_MOMENT_BUTTON_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(ElementLocators.FIRST_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ALBUM,ElementLocators.TEST_FEMALE_PHOTO)
        self.upload_image(ElementLocators.SECOND_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ALBUM,ElementLocators.TEST_FEMALE_PHOTO)
        self.interact_with_single_photo_album()

    def test_bro_show(self):
        self.open_the_certain_function(ElementLocators.PHOTO_ALBUM_SECTION_BUTTON_XPATH,ElementLocators.BRO_SHOW_BUTTON_UNDER_LIFE_BUTTON_XPATH)
        self.upload_image(ElementLocators.FIRST_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ALBUM,ElementLocators.TEST_MALE_PHOTO)
        self.upload_image(ElementLocators.SECOND_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ALBUM,ElementLocators.TEST_MALE_PHOTO)
        self.interact_with_single_photo_album()