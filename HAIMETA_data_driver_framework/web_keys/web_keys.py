import time
import traceback

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from HAIMETA_data_driver_framework.config.config import options as chrome_options
from selenium.webdriver.common.by import By
from HAIMETA_data_driver_framework.config.element_config import ElementLocators

from HAIMETA_data_driver_framework.config.get_logger import get_logger

log=get_logger()

def open_browser(type_):
    # 基于反射实现浏览器生成
    log.info(f"正在打开浏览器: {type_}")
    try:
        if type_ == "chrome":
            chrom_service = Service(r'D:\PycharmProjects\PythonProject\HAIMETA_data_driver_framework\config\chromedriver.exe')
            driver = webdriver.Chrome(service=chrom_service, options=chrome_options())
            log.info("Chrome浏览器已成功启动")
        else:
            log.info(f"尝试启动{type_}浏览器")
            driver=getattr(webdriver, type_.lower())()
            log.info(f"{type_}浏览器已成功启动")
    except Exception as e:
        log.error(f"启动浏览器失败: {str(e)}")
        log.info("尝试使用Chrome浏览器作为备选")
        chrom_service = Service(r'D:\PycharmProjects\PythonProject\HAIMETA_data_driver_framework\config\chromedriver.exe')
        driver=webdriver.Chrome(service=chrom_service, options=chrome_options())
        log.info("备选Chrome浏览器已成功启动")
    return driver


class WebKeys:

    def __init__(self, type_):
        self.HOME_URL = "https://preview.haimeta.com/"
        log.info("初始化WebKeys实例")
        self.driver = open_browser(type_)
        self.driver.implicitly_wait(5)
        log.info("设置隐式等待时间: 5秒")
        self.wait=WebDriverWait(self.driver, 10)
        log.info("设置显式等待时间: 10秒")
        self.action=ActionChains(self.driver)
        log.info("WebKeys实例初始化完成")

    def click(self, by, value):
        log.info(f"点击元素: {by}={value}")
        try:
            self.locator(by,value).click()
            log.info(f"元素点击成功: {by}={value}")
        except Exception as e:
            log.error(f"元素点击失败: {by}={value}, 错误: {str(e)}")
            raise

    def input(self,by, value, text):
        log.info(f"输入文本: {by}={value}, 文本内容: {text}")
        try:
            self.locator(by,value).send_keys(text)
            log.info(f"文本输入成功: {by}={value}")
        except Exception as e:
            log.error(f"文本输入失败: {by}={value}, 错误: {str(e)}")
            raise
    
    def open(self, url):
        log.info(f"打开URL: {url}")
        try:
            self.driver.get(url)
            log.info(f"URL打开成功: {url}")
        except Exception as e:
            log.error(f"URL打开失败: {url}, 错误: {str(e)}")
            raise

    def locator(self, by, value):
        log.info(f"定位元素: {by}={value}")
        try:
            element = self.driver.find_element(by, value)
            log.info(f"元素定位成功: {by}={value}")
            return element
        except Exception as e:
            log.error(f"元素定位失败: {by}={value}, 错误: {str(e)}")
            raise
    
    def quit(self):
        log.info("关闭浏览器")
        try:
            self.driver.quit()
            log.info("浏览器已成功关闭")
        except Exception as e:
            log.error(f"关闭浏览器失败: {str(e)}")
            raise

    def wait_sleep(self):
        log.info("等待2秒")
        time.sleep(1000)
        log.info("等待完成")

    def wait_visible(self, by, value):
        log.info(f"等待元素可见: {by}={value}")
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            log.info(f"元素已可见: {by}={value}")
            return element
        except Exception as e:
            log.error(f"等待元素可见超时: {by}={value}, 错误: {str(e)}")
            raise
    
    def wait_presence(self, by, value):
        log.info(f"等待元素存在: {by}={value}")
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            log.info(f"元素已存在: {by}={value}")
            return element
        except Exception as e:
            log.error(f"等待元素存在超时: {by}={value}, 错误: {str(e)}")
            raise

    def wait_clickable(self, by, value):
        log.info(f"等待元素可点击: {by}={value}")
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            log.info(f"元素已可点击: {by}={value}")
            return element
        except Exception as e:
            log.error(f"等待元素可点击超时: {by}={value}, 错误: {str(e)}")
            raise

    def wait_invisibility(self, by, value):
        log.info(f"等待元素不可见: {by}={value}")
        try:
            result = self.wait.until(EC.invisibility_of_element_located((by, value)))
            log.info(f"元素已不可见: {by}={value}")
            return result
        except Exception as e:
            log.error(f"等待元素不可见超时: {by}={value}, 错误: {str(e)}")
            raise

    def move_to_element(self, by, value):
        log.info(f"移动到元素: {by}={value}")
        try:
            element = self.locator(by, value)
            ActionChains(self.driver).move_to_element(element).perform()
            log.info(f"已成功移动到元素: {by}={value}")
        except Exception as e:
            log.error(f"移动到元素失败: {by}={value}, 错误: {str(e)}")
            raise
    
    def get_text(self, by, value):
        log.info(f"获取元素文本: {by}={value}")
        try:
            text = self.locator(by, value).text
            log.info(f"获取到元素文本: {by}={value}, 文本内容: {text}")
            return text
        except Exception as e:
            log.error(f"获取元素文本失败: {by}={value}, 错误: {str(e)}")
            raise

    def get_attribute(self, by, value, attribute):
        log.info(f"获取元素属性: {by}={value}, 属性名: {attribute}")
        try:
            attr_value = self.locator(by, value).get_attribute(attribute)
            log.info(f"获取到元素属性: {by}={value}, 属性名: {attribute}, 属性值: {attr_value}")
            return attr_value
        except Exception as e:
            log.error(f"获取元素属性失败: {by}={value}, 属性名: {attribute}, 错误: {str(e)}")
            raise
    
    def assert_text(self, by, value, expected):
        log.info(f"断言元素文本: {by}={value}, 预期文本: {expected}")
        self.wait_visible(by, value)
        try:
            reality=self.get_text(by, value)
            log.info(f"获取到实际文本: {reality}")
            assert reality == expected, f'''
            预期结果：{expected}
            实际结果：{reality}
            断言结果：{reality} != {expected}
            '''
            log.info(f"断言成功: 预期文本 '{expected}' 与实际文本 '{reality}' 匹配")
            return True
        except AssertionError as e:
            log.error(f"断言失败: 预期文本 '{expected}' 与实际文本 '{reality}' 不匹配")
            log.error(traceback.format_exc())
            return False
        except Exception as e:
            log.error(f"断言过程中发生异常: {str(e)}")
            log.error(traceback.format_exc())
            return False

    def click_visible(self, by, value):
        log.info(f"等待元素可见并点击: {by}={value}")
        try:
            self.wait_visible(by, value)
            self.click(by, value)
            log.info(f"元素可见并已成功点击: {by}={value}")
            return True, "操作成功"
        except Exception as e:
            log.error(f"等待元素可见并点击失败: {by}={value}, 错误: {str(e)}")
            log.error(traceback.format_exc())
            return False, f"发生未预期的错误: {str(e)}"

    def click_presence(self, by, value):
        log.info(f"等待元素存在并点击: {by}={value}")
        try:
            self.wait_presence(by, value)
            self.click(by, value)
            log.info(f"元素存在并已成功点击: {by}={value}")
            return True, "操作成功"
        except Exception as e:
            log.error(f"等待元素存在并点击失败: {by}={value}, 错误: {str(e)}")
            log.error(traceback.format_exc())
            return False, f"发生未预期的错误: {str(e)}"

    def click_clickable(self, by, value):
        log.info(f"等待元素存在并点击: {by}={value}")
        try:
            self.wait_clickable(by, value)
            self.click(by, value)
            log.info(f"元素存在并已成功点击: {by}={value}")
        except Exception as e:
            traceback.print_exc()
            return False, f"发生未预期的错误: {str(e)}"

    def input_visible(self, by, value, text):
        log.info(f"等待元素存在并输入: {text}")
        try:
            self.wait_visible(by, value)
            self.input(by, value, text)
            log.info(f"元素存在并已成功输入: {text}")
        except Exception as e:
            traceback.print_exc()
            return False, f"发生未预期的错误: {str(e)}"

    def input_presence(self, by, value, text):
        log.info(f"等待元素存在并输入: {text}")
        try:
            self.wait_presence(by, value)
            self.input(by, value, text)
            log.info(f"元素存在并已成功输入: {text}")
        except Exception as e:
            traceback.print_exc()
            return False, f"发生未预期的错误: {str(e)}"

    def input_clickable(self, by, value,text):
        log.info(f"等待元素存在并输入: {text}")
        try:
            self.wait_clickable(by, value)
            self.input(by, value, text)
            log.info(f"元素存在并已成功输入: {text}")
        except Exception as e:
            traceback.print_exc()
            return False, f"发生未预期的错误: {str(e)}"
    
    def Hover_to_the_button(self, by, value):
        log.info(f"移动到元素: {by}={value}")
        try:
            self.wait_visible(by, value)
            self.action.move_to_element(self.locator(by, value)).perform()
        except Exception as e:
            traceback.print_exc()
            return False, f"发生未预期的错误: {str(e)}"

    
    def switch_language(self, target_language="en", language_selection_class_name=None, language_switch_xpath=None, expected_title_text=None, expected_title_class_name=None):
        wait = self.wait
        
        log.info(f"Switching to {target_language} language")
        try:
            # 检查参数是否为None
            if language_selection_class_name is None or language_switch_xpath is None:
                log.info(f"Error: language_selection_class_name or language_switch_xpath is None")
                return False
            # Wait for and click language selection button
            self.Hover_to_the_button( 'class name',language_selection_class_name )
            
            # Wait for and click specific language option
            self.click_clickable( 'xpath',language_switch_xpath )

            # Verify language switch
            check_language = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, str(expected_title_class_name))) if expected_title_class_name is not None else EC.visibility_of_element_located((By.CLASS_NAME, "default-box-title"))
            )
            # 检查expected_title_text是否为None
            if expected_title_text is None:
                log.info(f"Warning: expected_title_text is None, cannot verify language switch")
                return True  # 无法验证，默认返回成功
            elif check_language.text == expected_title_text:
                log.info(f"Switch to {target_language} language successfully")
                return True
            else:
                log.info(f"Switch to {target_language} language unsuccessfully")
                return False
        except TimeoutException:
            log.info(f"Switch to {target_language} language Failed")
            return False

    def check_history(self):
        """检查历史记录按钮和列表"""
        wait = self.wait
        HistoryCheck=self.wait_visible('class name', "collapse-btn")
        HistoryCheck.click()
        HistoryCheck_list = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]")  # HISTORY LIST
            )
        ).is_displayed()
    
    def perform_click_and_check_tab(self, element, max_retries=3):
        """点击元素并检查是否出现新标签页，如果失败则重试
        Args:
            element: 要点击的元素
            max_retries: 最大重试次数
        Returns:
            bool: 是否成功打开新标签页
        """
        retry_count = 0
        initial_handles = len(self.driver.window_handles)
        
        while retry_count < max_retries:
            try:
                (self.action.move_to_element(element).
                 click().perform())
                # 等待新标签页出现
                self.wait.until(lambda driver: len(driver.window_handles) > initial_handles)
                # 切换到新标签页
                self.driver.switch_to.window(self.driver.window_handles[-1])
                return True
            except Exception as e:
                retry_count += 1
                if retry_count == max_retries:
                    log.info(f"Failed to open new tab after {max_retries} attempts: {str(e)}")
                    return False
                time.sleep(2)
            
    def open_the_certain_function(self,section_for_this_function_xpath,function_button_xpath):
        driver = self.driver
        wait = self.wait
        self.open(self.HOME_URL)
        self.click_clickable('xpath',section_for_this_function_xpath)
        time.sleep(2)
        function_button_click = self.wait_visible('xpath',function_button_xpath)
        if not self.perform_click_and_check_tab(function_button_click):
            raise Exception("Failed to open the section in new tab after 3 attempts")
        self.switch_tab(driver, wait)

    def switch_tab(self, driver, wait):
        max_retries = 3
        retry_count = 0
        while retry_count < max_retries:
            try:
                # 等待新标签页出现
                wait.until(lambda driver: len(driver.window_handles) > 1)
                all_tabs = driver.window_handles
                # 切换到最新打开的标签页
                driver.switch_to.window(all_tabs[-1])
                return driver.current_window_handle
            except Exception as e:
                retry_count += 1
                if retry_count == max_retries:
                    raise Exception(f"Failed to switch to new tab after {max_retries} retries: {str(e)}")
                time.sleep(2)

    def delete_history_item(self, item_xpath):
        """删除历史记录中的指定项目
        Args:
            item_xpath: 要删除的历史记录项的xpath路径
        Returns:
            bool: 删除是否成功
        """
        try:
            self.Hover_to_the_button('xpath',item_xpath)
            self.driver.find_element(By.CLASS_NAME, "item-box-delete").click()
            delete_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button.global-font-mask-medium.confirm"))
            )
            delete_button.click()
            delete_success_message=self.wait_visible('xpath', "/html/body/div[7]/div/div/div/span[2]")
            print(delete_success_message.text)
            return True
        except Exception as e:
            print(f"删除历史记录项失败: {str(e)}")
            return False

    def wait_for_loading_to_finish(self, item_class_name, process_time_limitation):
        """等待loading消失"""
        try:
            self.wait_visible('class name', item_class_name)
            self.wait_visible('class name', item_class_name)
            print("Process finished")
        except TimeoutException:
            print("Process failed")
            return False

    def publish_on_haimeta_community(self, item_to_publish_XPATH, publish_button_Xpath, publish_on_community_Xpath,
                                     cancel_button_Xpath):
        """发布到Haimeta社区"""
        driver = self.driver
        actions = self.action
        # Publish the image
        actions.move_to_element(
            driver.find_element(By.XPATH, item_to_publish_XPATH)
        ).perform()
        self.click_visible('xpath',publish_button_Xpath)
        # Publish on HAIMETA community
        self.click_visible('xpath',publish_on_community_Xpath)

        # Input the title
        self.input_visible('xpath',ElementLocators.TITLE_INPUT_XPATH,"Test")
        # Input the description
        self.input_visible('xpath',ElementLocators.DESCRIPTION_INPUT_XPATH,"Test")

        # Click the publish button
        self.click_visible('xpath',ElementLocators.CONFIRM_PUBLISH_BUTTON_XPATH)

        # Cancel the publish
        self.Hover_to_the_button('xpath', item_to_publish_XPATH)
        self.click_visible('xpath',publish_button_Xpath)
        # cancel publish button click
        self.click_visible('xpath',cancel_button_Xpath)

    def download_image(self, item_to_download_XPATH, download_button_xpath):
        """下载图片"""
        wait = self.wait
        driver = self.driver
        actions = self.action
        self.wait_visible('xpath', item_to_download_XPATH)

        actions.move_to_element(
            driver.find_element(By.XPATH, item_to_download_XPATH)
        ).pause(3).perform()

        self.click_action_check_by_visibility(download_button_xpath)

    def publish_on_style_library(self, item_to_publish_XPATH):
        """发布到风格库"""
        wait = self.wait
        driver = self.driver
        actions = self.action
        actions.move_to_element(
            driver.find_element(By.XPATH, item_to_publish_XPATH)
        ).perform()
        publish_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, ElementLocators.PUBLISH_BUTTON_XPATH_CAYL))
        )
        actions.move_to_element(publish_button_click).click().perform()
        publish_on_style_library_button_click = wait.until(
            EC.element_to_be_clickable((By.XPATH, ElementLocators.PUBLISH_ON_STYLE_LIBRARY_BUTTON_XPATH))
        )
        actions.move_to_element(publish_on_style_library_button_click).click().perform()
        # Input the style name
        style_name_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, ElementLocators.STYLE_NAME_INPUT_XPATH))
        )
        style_name_input.send_keys("Test")

        # Agree the terms
        self.click_action_check_by_element_to_be_clickable(ElementLocators.AGREE_TERMS_BUTTON_XPATH)

        # Click the publish button
        self.click_action_check_by_visibility(ElementLocators.PUBLISH_ON_STYLE_LIBRARY_CONFIRM_BUTTON_XPATH)

    def report_the_image(self, item_to_report_XPATH, three_dots_button_Xpath, report_button_Xpath):
        """举报图片"""
        wait = self.wait
        driver = self.driver
        actions = self.action
        actions.move_to_element(
            driver.find_element(By.XPATH, item_to_report_XPATH)
        ).perform()
        three_dots_button_click = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, three_dots_button_Xpath)
            )
        )
        actions.move_to_element(
            three_dots_button_click
        ).click().perform()

        # click report button
        self.click_action_check_by_element_to_be_clickable(report_button_Xpath)

        # Select the report type
        self.click_action_check_by_visibility(ElementLocators.REPORT_TYPE_BUTTON_XPATH)
        # Input the report reason
        report_reason_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, ElementLocators.REPORT_REASON_INPUT_XPATH))
        )
        report_reason_input.send_keys("Test")
        time.sleep(3)
        # Click the report button
        self.click_action_check_by_visibility(ElementLocators.CONFIRM_REPORT_BUTTON_XPATH)

    def upload_image(self, upload_way_XPATH, upload_image_paths):
        """上传单张或多张图片
        Args:
            upload_way_XPATH: 上传按钮的XPATH
            upload_image_paths: 可以是单个图片路径的字符串，或是多个图片路径的列表/元组
        """
        wait = self.wait
        # Upload the image(s)
        upload_button = wait.until(
            EC.presence_of_element_located((By.XPATH, upload_way_XPATH))
        )

        # 处理多图片上传
        if isinstance(upload_image_paths, (list, tuple)):
            # 将多个路径用 \n 连接，Selenium会将其识别为多文件上传
            paths = '\n'.join(upload_image_paths)
            upload_button.send_keys(paths)
        else:
            # 单图片上传
            upload_button.send_keys(upload_image_paths)

        self.wait_for_loading_to_finish("upload-loading", 20)
        print("Upload image(s) successfully")

    def choose_style_skin_texture_of_generated_image(self, style_selection_XPATH, skin_texture_input_XPATH):

        # Choose the style of generated image
        self.click_action_check_by_visibility(style_selection_XPATH)
        # Input the SKIN TEXTURE
        skin_texture_input = self.click_action_check_by_visibility(skin_texture_input_XPATH)
        skin_texture_input.send_keys("0.67")

    def click_create_button_xpath(self, button_Xpath):
        self.click_action_check_by_element_to_be_clickable(button_Xpath)

    def click_create_button_class_name(self, button_class_name):
        wait = self.wait
        self.click_action_check_by_element_to_be_clickable(button_class_name)

    def set_up_the_size_of_the_generated_image(self, size_button_Xpath, certain_size_Xpath):
        # Set up the size of the generated image
        self.click_action_check_by_visibility(size_button_Xpath)
        self.click_action_check_by_visibility(certain_size_Xpath)

    def set_up_the_layout_of_the_generated_image(self, layout_button_Xpath, certain_layout_Xpath):
        # Set up the layout of the generated image
        self.click_action_check_by_visibility(layout_button_Xpath)
        self.click_action_check_by_visibility(certain_layout_Xpath)

    def adjust_the_position_of_the_generated_image(self, adjusted_image_XPATH):
        wait = self.wait
        driver = self.driver
        actions = self.action

        actions.move_to_element(
            driver.find_element(By.XPATH, adjusted_image_XPATH)
        ).perform()
        # adjust_button_click = wait.until(
        #     EC.visibility_of_element_located((By.XPATH, self.ADJUST_BUTTON_XPATH))
        # )
        # adjust_button_click.click()

        self.switch_frame_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/iframe")
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/flutter-view")))
        actions.click_and_hold(driver.find_element(By.XPATH, "/html/body/flutter-view"))  # 点击并按住元素
        actions.move_by_offset(10, 20)  # 移动到目标元素
        actions.pause(3)
        actions.release()  # 释放鼠标
        actions.perform()
        # can not locate th save button after adjusting the position of the generated image
        # end the code here

    def delete_the_generated_image(self, item_to_delete_XPATH, three_dots_button_Xpath, delete_button_Xpath):
        wait = self.wait
        driver = self.driver
        actions = self.action
        actions.move_to_element(
            driver.find_element(By.XPATH, item_to_delete_XPATH)
        ).perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, three_dots_button_Xpath)))
        actions.move_to_element(
            driver.find_element(By.XPATH, three_dots_button_Xpath)
        ).click().perform()

        self.click_action_check_by_visibility(delete_button_Xpath)

        self.click_action_check_by_visibility(ElementLocators.CONFIRM_DELETE_BUTTON_XPATH)


    def interact_with_single_photo_album(self):
        wait = self.wait
        actions = self.action
        self.choose_style_skin_texture_of_generated_image(ElementLocators.CHOOSE_PHOTO_GENERATION_STYLE_XPATH,
                                                          ElementLocators.INPUT_SKIN_TEXTURE_SINGLE_PHOTO_ALBUM)

        # set the number of images to generate
        number_of_images_to_generate_button_click = wait.until(
            EC.element_to_be_clickable((By.XPATH, ElementLocators.NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_PHOTO_ALBUM))
        )
        number_of_images_to_generate_button_click.click()

        self.click_create_button_xpath(ElementLocators.CREATE_BUTTON_XPATH)
        self.wait_for_loading_to_finish(item_class_name="_pictureEditorLoading_anlig_1", process_time_limitation=60)

        second_item_selected = wait.until(
            EC.element_to_be_clickable((By.XPATH, ElementLocators.SECOND_ITEM_SELECTED_XPATH))
        )
        actions.move_to_element(second_item_selected).double_click().perform()
        # interact with the generated images
        self.download_image(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.DOWNLOAD_BUTTON_XPATH_CAYL_AND_SINGLE_PHOTO_ABLUM)
        self.publish_on_haimeta_community(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.PUBLISH_BUTTON_XPATH_SINGLE_PHOTO_ALBUM,
                                          ElementLocators.PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_SINGLE_PHOTO_ALBUM,
                                          ElementLocators.CANCEL_PUBLISH_BUTTON_XPATH_SINGLE_PHOTO_ALBUM)
        self.report_the_image(ElementLocators.INTERACTED_IMAGE_1_XPATH, ElementLocators.THREE_DOTS_BUTTON_XPATH_SINGLE_PHOTO_ALBUM,
                              ElementLocators.REPORT_BUTTON_XPATH_ID_PHOTO_SINGLE_PHOTO_ALBUM)
        self.delete_the_generated_image("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div",
                                        ElementLocators.THREE_DOTS_BUTTON_XPATH_SINGLE_PHOTO_ALBUM,
                                        ElementLocators.DELETE_BUTTON_XPATH_SINGLE_PHOTO_ALBUM)

    def refine_your_idea(self):
        wait = self.wait
        driver = self.driver
        # Refine your idea
        Refine_your_idea_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, ElementLocators.REFINE_YOUR_IDEA_BUTTON_XPATH))
        )
        Refine_your_idea_button_click.click()
        # Wait for the loading to finish
        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, ElementLocators.REFINE_YOUR_IDEA_BUTTON_XPATH))
        )

    def select_the_size_of_the_generated_image(self, size_of_generation_button_xpath):
        self.click_action_check_by_visibility(size_of_generation_button_xpath)

    def input_prompt_box_CLASS_NAME(self, input_prompt_box_class_name, input_prompt_box_input_data):
        wait = self.wait
        Input_prompt_box = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, input_prompt_box_class_name))
        )
        Input_prompt_box.click()
        Input_prompt_box.send_keys(input_prompt_box_input_data)

    def set_number_of_images_to_generate(self, number_of_images_to_generate_button_xpath):
        self.click_action_check_by_visibility(number_of_images_to_generate_button_xpath)

    def click_action_check_by_visibility(self, action_button_xpath):
        wait = self.wait
        action_button_click = wait.until(
            EC.visibility_of_element_located((By.XPATH, action_button_xpath))
        )
        action_button_click.click()
        return action_button_click

    def click_action_check_by_presence(self, action_button_xpath):
        wait = self.wait
        action_button_click = wait.until(
            EC.presence_of_element_located((By.XPATH, action_button_xpath))
        )
        action_button_click.click()

    def click_action_check_by_element_to_be_clickable(self, action_button_xpath):
        wait = self.wait
        action_button_click = wait.until(
            EC.element_to_be_clickable((By.XPATH, action_button_xpath))
        )
        action_button_click.click()

    def interact_with_the_second_item_selected(self, item_xpath):
        wait = self.wait
        actions = self.action
        second_item_selected = wait.until(
            EC.element_to_be_clickable((By.XPATH, item_xpath))
        )
        actions.move_to_element(second_item_selected).double_click().perform()

    def switch_frame_by_xpath(self, frame_xpath):
        driver = self.driver
        wait = self.wait
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, frame_xpath)))
        driver.switch_to.frame(driver.find_element(By.XPATH, frame_xpath))

    def thirdparty_switch(self):
        wait = self.wait
        driver = self.driver
        wait.until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])