class ElementLocators:
    # Login page locators
    EMAIL_INPUT_XPATH = "//input[@id='first-email']"
    CONTINUE_BUTTON_XPATH = "//div[@id='first-page']/form/div[2]/button"
    PASSWORD_INPUT_XPATH = "//input[@id='login-password']"
    LOGIN_BUTTON_XPATH = "//form[@class='login-form']/button"
    USER_DISPLAY_ClASS_NAME = "clip-path"
    FORGET_PASSWORD_BUTTON_XPATH="//form[@class='login-form']/div[2]"
    FORGET_EMAIL_INPUT_XPATH="//input[@id='forget-email']"
    FORGET_SEND_VERI_CODE_BUTTON_XPATH="//div[@class='code-button']"
    CHECK_IN_VERFICATION_PAGE_XPATH = "//div[@class='notice global-font-body-medium']/text()[2]"

    LOGOUT_BUTTON_XPATH = '/html/body/div[3]/div/div/div/div/div/ul/li[4]/span'
    # Third party login locators
    THIRD_PARTY_BUTTON_XPATH = "//*[@id='first-page']/button"
    THIRD_PARTY_NEXT_BUTTON_XPATH = "/html/body/div/div/div[3]/div/div/div/button"

    # PE page locators


    # Privacy policy and USER SERVICE locators
    PRIVACY_POLICY_LINK_XPATH = "//*[@id='first-page']/div[4]/div/div/span[2]"
    PRIVACY_POLICY_CHECK_MESSAGE = "/html/body/div/div/div/div/p[1]/span[37]"
    PRIVACY_POLICY_BACK_BUTTON = "//*[@id='root']/div/button"
    USER_SERVICE_PRIVACY_LINK_XPATH = "//*[@id='first-page']/div[4]/div/div/span[1]"
    USER_SERVICE_PRIVACY_CHECK_MESSAGE = "/html/body/div/div/div/div/p[3]/span[44]"
    USER_SERVICE_BACK_BUTTON = "//*[@id='root']/div/button"
    ERROR_MESSAGE_ON_LOGIN_PAGE_XPATH = "/div/div/div/span[2]"
    GET_VERIFICATION_CODE_BUTTON_XPATH = "//div[@class='code-button']"
    VERIFICATION_CODE_INPUT_XPATH = "//input[@type='text']"
    VERIFICATION_CODE_ERROR_MESSAGE_XPATH = "//div[@class='error-text']"
    TEN_TIMES_ERROR_MESSAGE_XPATH = "//div[@class='lock-container']/div[2]"
    ERROR_MESSAGE_AFTER_INPUT_WRONG_PASSWORD = '//div[@class="error-text global-font-body-small"]'
    WRONG_PASSWORD = "123141231312"
    LOCK_TIP_XPATH = "//div[@class='lock-tip global-font-body-medium']"

    # Home page locators

    # Basic Tools section locators
    EDITION_ON_HOME_BUTTON_XPATH = "(//div[@class='basic-item-box'])[1]"
    BG_REMOVER_ON_HOME_BUTTON_XPATH = "(//div[@class='basic-item-box'])[2]"
    SMART_ERASER_ON_HOME_BUTTON_XPATH = "(//div[@class='basic-item-box'])[3]"
    HD_ENLARGE_ON_HOME_BUTTON_XPATH = "(//div[@class='basic-item-box'])[4]"
    HD_REPAIR_ON_HOME_BUTTON_XPATH = "(//div[@class='basic-item-box'])[5]"

    # sections button locators
    LIFE_BUTTON_ON_HOME_XPATH = "(//div[@role='tab'])[3]"
    WORK_SECTION_BUTTON_XPATH = "(//div[@role='tab'])[4]"
    BUZZ_SECTION_BUTTON_XPATH = "(//div[@role='tab'])[1]"
    ART_SECTION_BUTTON_XPATH = "(//div[@role='tab'])[2]"
    PHOTO_ALBUM_SECTION_BUTTON_XPATH = "(//div[@role='tab'])[3]"

    # buzz section tools locators
    DREAM_HOME_DESIGN_UNDER_BUZZ_SECTION_XPATH = "(//div[@class='cardPercentage'])[3]/div"

    # Portraits section locators
    ID_PHOTO_BUTTON_XPATH = "(//div[@class='cardPercentage'])[6]/div"
    ARABIAN_DREAMS_BUTTON_XPATH = "(//div[@class='cardPercentage'])[8]/div"
    BFF_MOMENT_BUTTON_UNDER_LIFE_BUTTON_XPATH = "(//div[@class='cardPercentage'])[2]/div"
    LOVE_IN_THE_AIR_BUTTON_UNDER_LIFE_BUTTON_XPATH = "(//div[@class='cardPercentage'])[3]/div"
    BRO_SHOW_BUTTON_UNDER_LIFE_BUTTON_XPATH = "(//div[@class='cardPercentage'])[4]/div"
    CHINESE_AESTHETICS_UNDER_LIFE_BUTTON_XPATH = "(//div[@class='cardPercentage'])[7]/div"
    NANYANG_MEMORY_UNDER_LIFE_BUTTON_XPATH = "(//div[@class='cardPercentage'])[9]/div"
    EAST_ASIAN_CULTURE_UNDER_LIFE_BUTTON_XPATH = "(//div[@class='cardPercentage'])[10]/div"
    CYBER_FUTURE_UNDER_LIFE_BUTTON_XPATH = "(//div[@class='cardPercentage'])[11]/div"
    GORGEOUS_ROAD_UNDER_LIFE_BUTTON_XPATH = "(//div[@class='cardPercentage'])[12]/div"
    FANTASY_TALES_UNDER_LIFE_BUTTON_XPATH = "(//div[@class='cardPercentage'])[13]/div"

    # social entertainment tool locators
    CREATE_AS_YOU_LIKE_UNDER_BUZZ_SECTION_XPATH = "(//div[@class='cardPercentage'])[2]/div"
    PERSONAL_AVATAR_BUTTON_UNDER_ART_SECTION_XPATH = "(//div[@class='cardPercentage'])[7]/div"

    # products design locators
    CREATE_CLOTHES_BUTTON_UNDER_WORK_SECTION = "(//div[@class='cardPercentage'])[2]/div"
    CREATE_NAIL_ART_BUTTON_UNDER_WORK_SECTION_XPATH = "(//div[@class='cardPercentage'])[10]/div"
    CREATE_TATTOO_BUTTON_UNDER_WORK_SECTION_XPATH = "(//div[@class='cardPercentage'])[9]/div"
    CREATE_TOY_BUTTON_UNDER_WORK_SECTION_XPATH = "(//div[@class='cardPercentage'])[4]/div"
    ME_TIME_BUTTON_UNDER_WORK_SECTION_XPATH = "(//div[@class='cardPercentage'])[11]/div"

    # business design locators
    CREATE_CHARACTER_BUTTON_UNDER_WORK_SECTION_XPATH = "(//div[@class='cardPercentage'])[5]/div"
    CREATE_LOGO_BUTTON_UNDER_WORK_SECTION_XPATH = "(//div[@class='cardPercentage'])[7]/div"
    STOCK_IMAGE_BUTTON_UNDER_WORK_SECTION_XPATH = "(//div[@class='cardPercentage'])[14]/div"
    CHARACTER_TEXTURE_BUTTON_UNDER_WORK_SECTION_XPATH = "(//div[@class='cardPercentage'])[8]/div"
    CHARACTER_PORTRAIT_STUDIO_BUTTON_UNDER_WORK_SECTION_XPATH = "(//div[@class='cardPercentage'])[13]/div"
    CREATE_PRODUCT_UNDER_WORK_SECTION_XPATH = "(//div[@class='cardPercentage'])[12]/div"
    CREATE_RING_UNDER_WORK_SECTION_XPATH = "(//div[@class='cardPercentage'])[1]/div"

    # art section locators
    TEXTURE_LABEL_BUTTON_UNDER_ART_SECTION_XPATH = "(//div[@class='cardPercentage'])[2]/div"
    STYLE_BUTTON_UNDER_ART_SECTION_XPATH = "(//div[@class='cardPercentage'])[3]/div"
    CREATE_WALLPAPER_BUTTON_UNDER_ART_SECTION_XPATH = "(//div[@class='cardPercentage'])[5]/div"
    TRENDY_ART_BUTTON_UNDER_ART_SECTION_XPATH = "(//div[@class='cardPercentage'])[1]/div"
    PATTERN_BUTTON_UNDER_ART_SECTION_XPATH = "(//div[@class='cardPercentage'])[6]/div"
    CHARACTER_STICKERS_UNDER_ART_BUTTON_XPATH = "(//div[@class='cardPercentage'])[8]/div"
    ANIMAL_AND_ME_UNDER_ART_BUTTON_XPATH = "(//div[@class='cardPercentage'])[4]/div"
    UPLOAD_BUTTON_XPATH="//input[@name='file']"

    # HD enlarge page locators
    TWO_TIMES_ENLARGE_BUTTON_XPATH = "//div[@class='item-box']/div[1]"
    FOUR_TIMES_ENLARGE_BUTTON_XPATH = "//div[@class='item-box']/div[2]"
    ENLARGE_BUTTON_XPATH = "//div[@class='generate-button-container']/div/button"

    # HD repair page locators
    HD_REPAIR_BUTTON_XPATH = "//div[@class='generate-button-container']/div/button"
    INPUT_PROMPT_BOX_XPATH = "//textarea[@name='prompt']"

    # Language switch locators
    LANGUAGE_SELECTION_XPATH = "//div[@class='selector-title']/i"
    SWITCH_TO_ENGLISH_LANGUAGE_XPATH="(//div[@class='group-item'])[1]"
    SWITCH_TO_TRADITIONAL_CHINESE_LANGUAGE_XPATH = "(//div[@class='group-item'])[2]"
    SWITCH_TO_SIMPLIFIED_CHINESE_LANGUAGE_XPATH = "(//div[@class='group-item'])[3]"
    SWITCH_TO_SPANISH_LANGUAGE_XPATH = "(//div[@class='group-item'])[4]"
    SWITCH_TO_FRANCE_LANGUAGE_XPATH = "(//div[@class='group-item'])[5]"
    SWITCH_TO_JAPANESE_LANGUAGE_XPATH = "(//div[@class='group-item'])[6]"
    SWITCH_TO_KOREAN_LANGUAGE_XPATH = "(//div[@class='group-item'])[7]"

    # Billing history page locators
    BUY_HAIBIT_BUTTON_XPATH = "//div[@class='right-vip-head']/div[1]"
    PURCHASE_HAIBIT_ON_BILLING_HISTORY = "//div[@class='orderList-footer']/div[2]"
    HAIBIT_PURCHASE_SELECTION_XPATH = "//div[@class='buyHaibitWrapper-list-item'][1]"
    CONFIRM_PAYMENT_IN_PURCHASE_HAIBIT_XPATH = "//div[@class='buyHaibitWrapper-pay']//button"
    PURCHASE_HAIBIT_INPUT_CARD_NUMBER_XPATH = "//input[@name='number']"
    PURCHASE_HAIBIT_INPUT_CARD_AVAILABLE_XPATH = "//input[@name='expiry']"
    PURCHASE_HAIBIT_INPUT_CARD_SECURE_NUMBER_XPATH = "//input[@name='cvc']"
    PURCHASE_HAIBIT_PAY_NOW_BUTTON_xpath = "//button[@id='submit']"

    # Create As You Like page locators
    REFINE_YOUR_IDEA_BUTTON_XPATH = "//div[@class='container']/div[2]/img"
    SIZE_OF_GENERATION_BUTTON_XPATH = "(//div[@class='shape-item'])[4]"
    NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH = "//div[@class='choose-number-options']/div[1]"
    INTERACTED_IMAGE_1_XPATH = "//div[@class='preview']"
    DOWNLOAD_BUTTON_XPATH = "//span[@class='iconfont ic_download']"
    PUBLISH_BUTTON_XPATH = "//span[@class='iconfont ic_publish']"

    PUBLISH_INTERACTION_ELEMENT_ON_HAIMETA_COMMUNITY = "(//div[@class='dropdown-item'])[1]/.."
    TITLE_INPUT_XPATH = "(//div[@id='input-box'])[1]//textarea"
    DESCRIPTION_INPUT_XPATH = "(//div[@id='input-box'])[2]//textarea"
    CONFIRM_PUBLISH_BUTTON_XPATH = "//div[@class='describe-area-buttons']//button"
    PUBLISH_ON_STYLE_LIBRARY_BUTTON_XPATH = "(//div[@class='dropdown-item'])[2]/.."
    STYLE_NAME_INPUT_XPATH = "(//div[@class='input-box'])[2]//textarea"
    AGREE_TERMS_BUTTON_XPATH = "//input[@type='checkbox']/.."
    PUBLISH_ON_STYLE_LIBRARY_CONFIRM_BUTTON_XPATH = "//div[@class='button']/button"
    REPORT_BUTTON_XPATH = "//span[@class='iconfont ic_report']"
    REPORT_TYPE_BUTTON_XPATH = "//div[@class='type-list']/div[1]"
    REPORT_REASON_INPUT_XPATH = "(//div[@class='input-box' and last()])/textarea"
    CONFIRM_REPORT_BUTTON_XPATH = "//div[@class='button']/button"
    THREE_DOTS_BUTTON_XPATH = "//i[@class='ic_more iconfont']"
    INPUT_SKIN_TEXTURE = "//input[@role='spinbutton']"

    # PHOTO ALBUM page locators
    CREATE_BUTTON_XPATH = "//div[@class='contral-buttons']/button"
    SET_SIZE_BUTTON_XPATH = "(//span[@class='navigation-link-item-title'])[1]"
    SET_LAYOUT_BUTTON_XPATH = "(//span[@class='navigation-link-item-title'])[2]"
    INS_SIZE_BUTTON_XPATH = "//span[contains(text(),'Instagram')]"
    FIVE_INCHES_LAYOUT_BUTTON_XPATH = "(//ul)[2]/div[2]/div/div/span[1]"
    SINGLE_LAYOUT_BUTTON_XPATH = "(//ul)[2]/div[1]/div/div/span[1]"
    CONFIRM_DELETE_BUTTON_XPATH = "//button[@class='confirm-content-buttons--confirm']"
    INTERACTED_ITEM_PREVIEW_ITEM_XPATH = "//div[@class='preview-item']"
    DELETE_BUTTON_XPATH = "(//div[@class='dropdown-item'])[1]/p"
    SECOND_ITEM_SELECTED_XPATH = "(//div[@class='item--background'])[2]"

    # CHINESE AESTHETICS page locators

    # DOUBLE PHOTO ALBUM page locators
    FIRST_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ALBUM = "(//input[@name='file'])[1]"
    SECOND_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ALBUM = "(//input[@name='file'])[3]"

    # Test credentials
    VALID_EMAIL_ACCOUNT = "1974440719@qq.com"
    VALID_PASSWORD = "Tiejiayu666"
    TEST_FEMALE_PHOTO = r'D:\PycharmProjects\PythonProject\UploadMaterial\WomenTest.png'
    TEST_MALE_PHOTO = r'D:\PycharmProjects\PythonProject\UploadMaterial\Mantest.png'
    TEST_IMAGE = r'D:\PycharmProjects\PythonProject\UploadMaterial\TestUpload.png'
    TEST_SKETCH_IMAGE = r'D:\PycharmProjects\PythonProject\UploadMaterial\sketch.png'
    TEST_PRODUCT_IMAGE = r'D:\PycharmProjects\PythonProject\UploadMaterial\Bag_image.png'
    TEST_IP_IMAGE = r'D:\PycharmProjects\PythonProject\UploadMaterial\PandaIPimage.png'
    TEST_HOME_DESIGN_IMAGE = r'D:\PycharmProjects\PythonProject\UploadMaterial\homedesign.jpg'
    # 存储宠物图片数据集的路径
    PET_IMAGE_DATA_SET = [
        r'D:\PycharmProjects\PythonProject\UploadMaterial\cat\image_1.jpg',
        r'D:\PycharmProjects\PythonProject\UploadMaterial\cat\image_2.jpg',
        r'D:\PycharmProjects\PythonProject\UploadMaterial\cat\image_3.jpg',
        r'D:\PycharmProjects\PythonProject\UploadMaterial\cat\image_4.jpg',
        r'D:\PycharmProjects\PythonProject\UploadMaterial\cat\image_5.jpg',
        r'D:\PycharmProjects\PythonProject\UploadMaterial\cat\image_6.jpg',
        r'D:\PycharmProjects\PythonProject\UploadMaterial\cat\image_7.jpg',
        r'D:\PycharmProjects\PythonProject\UploadMaterial\cat\image_8.jpg',

    ]

    # Create clothes page locators
    DOWNLOAD_PATTERN_BUTTON_XPATH = "//div[@class='preview-item']//button"
    ADD_NEW_IMAGE_BUTTON_XPATH = "//i[@class='iconfont ic_add']"

    # Pet page locators
    PET_SECTION_BUTTON_XPATH = "(//div[@role='tab'])[3]"
    STYLE_YOUR_PET_ON_HOME_UNDER_PET_SECTION_XPATH = "(//div[@class='cardPercentage'])[1]/div"
    START_TRAINING_BUTTON_XPATH = "//div[@class='batch-upload-buttons']//button"
    ADD_PET_DATA_SET_BUTTON_XPATH = "//div[@class='upload-item']/i"
    CLOSE_WINDOWS_BUTTON_XPATH = "//i[@class='ic_close iconfont']"


    # T2I page locators
    STYLE_CHOICE_BUTTON_XPATH = "(//div[contains(@class, 'template-list')])[1]/div[1]/div"
    CLOTHING_STYLE_BUTTON_XPATH = "(//div[contains(@class, 'template-list')])[1]/div[2]/div"

    # I2I page locators
    RENDERING_RESULT_XPATH_I2I = "//div[@class='picture-editor-radio-group']/div[1]"

    PICTURE_EDITOR_LOADING_CLASS_NAME = "_pictureEditorLoading_anlig_1"

    SWITCH_TASK_I2I_XPATH="//div[@class='picture-editor-radio-group']/div[2]"
    SWITCH_TASK_T2I_XPATH="//div[@class='picture-editor-radio-group']/div[1]"
    # Configuration
    LOGIN_URL = "https://preview.haimeta.com/login"
    HOME_URL = "https://preview.haimeta.com/"
