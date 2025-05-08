import unittest


from BaseTest import BaseTest
from Preview_config import ElementLocators


class Text2Image_Test(BaseTest):
    def common_step_for_T2I(self,section_for_this_button_xpath,button_xpath):
        self.open_the_certain_function(section_for_this_button_xpath,button_xpath)
        self.input_prompt("blue sky")
        self.refine_your_idea()
        # choose the style
        self.click_action_check_by_visibility(ElementLocators.STYLE_CHOICE_BUTTON_XPATH)
        # Select the size of generation
        self.click_action_check_by_visibility(ElementLocators.SIZE_OF_GENERATION_BUTTON_XPATH)
        # Select the number of images to generate
        self.click_action_check_by_visibility(ElementLocators.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH)
        self.start_creation()
        # interact with the image
        self.interact_with_the_generated_image()

    def common_step_for_T2I_without_size_extension(self,section_for_this_button_xpath,button_xpath):
        self.open_the_certain_function(section_for_this_button_xpath,button_xpath)
        self.input_prompt(" blue sky")
        # choose the style
        self.click_action_check_by_visibility(ElementLocators.STYLE_CHOICE_BUTTON_XPATH)
        # Select the number of images to generate
        self.click_action_check_by_visibility(ElementLocators.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH)
        self.start_creation()
        # interact with the image
        self.interact_with_the_generated_image()

    def common_step_for_T2I_without_refining(self,section_for_this_button_xpath,button_xpath):
        self.open_the_certain_function(section_for_this_button_xpath,button_xpath)
        self.input_prompt(" blue sky")
        # choose the style
        self.click_action_check_by_visibility(ElementLocators.STYLE_CHOICE_BUTTON_XPATH)
        # Select the size of generation 
        self.click_action_check_by_visibility(ElementLocators.SIZE_OF_GENERATION_BUTTON_XPATH)
        # Select the number of images to generate
        self.click_action_check_by_visibility(ElementLocators.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH)
        self.start_creation()
        # interact with the image
        self.interact_with_the_generated_image()

    def test_create_nail_art(self):
        self.common_step_for_T2I_without_size_extension(ElementLocators.WORK_SECTION_BUTTON_XPATH,ElementLocators.CREATE_NAIL_ART_BUTTON_UNDER_WORK_SECTION_XPATH)
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
        self.common_step_for_T2I(ElementLocators.ART_SECTION_BUTTON_XPATH,ElementLocators.PATTERN_BUTTON_UNDER_ART_SECTION_XPATH)

if __name__ == "__main__":
    unittest.main()