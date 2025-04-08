
from selenium.webdriver.remote.switch_to import SwitchTo

# Login page locators
EMAIL_INPUT_XPATH = "//input[@id='first-email']"
CONTINUE_BUTTON_XPATH = "//div[@id='first-page']/form/div[2]/button"
PASSWORD_INPUT_XPATH = "//input[@id='login-password']"
LOGIN_BUTTON_XPATH = "//form[@class='login-form']/button"
USER_DISPLAY_ClASS_NAME = "clip-path"

# Third party login locators
THIRD_PARTY_BUTTON_XPATH = "//*[@id='first-page']/button"
THIRD_PARTY_NEXT_BUTTON_XPATH = "/html/body/div/div/div[3]/div/div/div/button"

# Privacy policy and USER SERVICE locators
PRIVACY_POLICY_LINK_XPATH = "//*[@id='first-page']/div[4]/div/div/span[2]"
PRIVACY_POLICY_CHECK_MESSAGE = "/html/body/div/div/div/div/p[1]/span[37]"
PRIVACY_POLICY_BACK_BUTTON = "//*[@id='root']/div/button"
USER_SERVICE_PRIVACY_LINK_XPATH = "//*[@id='first-page']/div[4]/div/div/span[1]"
USER_SERVICE_PRIVACY_CHECK_MESSAGE = "/html/body/div/div/div/div/p[3]/span[44]"
USER_SERVICE_BACK_BUTTON = "//*[@id='root']/div/button"
ERROR_MESSAGE_ON_LOGIN_PAGE_XPATH = "/div/div/div/span[2]"
GET_VERIFICATION_CODE_BUTTON_XPATH = "/html/body/div/div/div[3]/div/div/div[1]/div[2]"

# Home page locators

# Basic Tools section locators
EDITION_ON_HOME_BUTTON_XPATH = "//*[@id='scrollContainer']/div/div/div[1]/div[1]/div[2]/div[1]/span/div[1]"
BG_REMOVER_ON_HOME_BUTTON_XPATH = "//*[@id='scrollContainer']/div/div/div[1]/div[1]/div[2]/div[2]/span/div[1]"
SMART_ERASER_ON_HOME_BUTTON_XPATH = "//*[@id='scrollContainer']/div/div/div[1]/div[1]/div[2]/div[3]/span/div[1]"
HD_ENLARGE_ON_HOME_BUTTON_XPATH = "//*[@id='scrollContainer']/div/div/div[1]/div[1]/div[2]/div[4]/span/div[1]"
HD_REPAIR_ON_HOME_BUTTON_XPATH = "//*[@id='scrollContainer']/div/div/div[1]/div[1]/div[2]/div[5]/span/div[1]"

# sections button locators
LIFE_BUTTON_ON_HOME_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[3]"
WORK_SECTION_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[4]/div"
BUZZ_SECTION_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[1]"
ART_SECTION_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[2]/div"
PHOTO_ALBUM_SECTION_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[3]/div"


# buzz section tools locators
DREAM_HOME_DESIGN_UNDER_BUZZ_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/img"


# Portraits section locators
ID_PHOTO_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[6]/div/div/div[3]/div[2]/div"
ARABIAN_DREAMS_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[8]/div/div/div[3]/div[2]/div"
BFF_MOMENT_BUTTON_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]"
LOVE_IN_THE_AIR_BUTTON_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div/div[3]/div[2]"
BRO_SHOW_BUTTON_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[4]/div/div/div[3]/div[2]"
CHINESE_AESTHETICS_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[7]/div/div/div[3]/div[2]"
NANYANG_MEMORY_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[9]/div/div/div[3]/div[2]"
EAST_ASIAN_CULTURE_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[10]/div/div/div[3]/div[2]"
CYBER_FUTURE_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[11]/div/div/div[3]/div[2]"
GORGEOUS_ROAD_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[12]/div/div/div[3]/div[2]"
FANTASY_TALES_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[13]/div/div/div[3]/div[2]"

# social entertainment tool locators
CREATE_AS_YOU_LIKE_UNDER_BUZZ_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div[2]"
PERSONAL_AVATAR_BUTTON_UNDER_ART_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[6]/div/div/div[3]/div[2]/div"


# products design locators
CREATE_CLOTHES_BUTTON_UNDER_WORK_SECTION="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div"
CREATE_NAIL_ART_BUTTON_UNDER_WORK_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div"
CREATE_TATTOO_BUTTON_UNDER_WORK_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[7]/div/div/div[3]/div[2]/div"
CREATE_TOY_BUTTON_UNDER_WORK_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div/div[3]/div[2]/div"
ME_TIME_BUTTON_UNDER_WORK_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[8]/div/div/div[3]/div[2]/div"

# business design locators
CREATE_CHARACTER_BUTTON_UNDER_WORK_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[4]/div/div/div[3]/div[2]/div"
CREATE_LOGO_BUTTON_UNDER_WORK_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[5]/div/div/div[3]/div[2]/div"
STOCK_IMAGE_BUTTON_UNDER_WORK_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[11]/div/div/div[3]/div[2]/div"
CHARACTER_TEXTURE_BUTTON_UNDER_WORK_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[8]/div/div/div[3]/div[2]/div"
CHARACTER_PORTRAIT_STUDIO_BUTTON_UNDER_WORK_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[12]/div/div/div[3]/div[2]/div"
CREATE_PRODUCT_UNDER_WORK_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[11]/div/div/div[3]/div[2]/div"


# art section locators
TEXTURE_LABEL_BUTTON_UNDER_ART_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div"
STYLE_BUTTON_UNDER_ART_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div/div[3]/div[2]/div"
CREATE_WALLPAPER_BUTTON_UNDER_ART_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[4]/div/div/div[3]/div[2]/div"
TRENDY_ART_BUTTON_UNDER_ART_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div"
PATTERN_BUTTON_UNDER_ART_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[5]/div/div/div[3]/div[2]/div"
CHARACTER_STICKERS_UNDER_ART_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[7]/div/div/div[3]/div[2]/div/img"


#PE page locators
PICTURE_EDITION_UPLOAD_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/span/div/span/input"

#BG page locators
BG_REMOVER_UPLOAD_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/span/div/span/input"

#SE page locators
SMART_ERASER_UPLOAD_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/div[2]/div[1]/div/span/div/span/input"

#HD enlarge page locators
HD_ENLARGE_UPLOAD_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div[2]/div[1]/div/span/div/span/input"
TWO_TIMES_ENLARGE_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div[1]"
FOUR_TIMES_ENLARGE_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]"
ENLARGE_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div"


#HD repair page locators
HD_REPAIR_UPLOAD_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div[2]/div[1]/div/span/div/span/input"
HD_REPAIR_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/button"

INPUT_PROMPT_BOX_CLASS_NAME="ant-input.css-otvc0b.textarea-buttons"

GENERATE_BUTTON_CLASS_NAME="contral-buttons-generate"

# Language switch locators
LANGUAGE_SELECTION_CLASS_NAME = "_main_y4u1i_1"
SWITCH_TO_CHINESE_LANGUAGE_PE_HOME_XPATH = "/html/body/div[6]/div/div/div/div/div/div[2]/div/div[1]"
SWITCH_TO_ENGLISH_LANGUAGE_PE_HOME_XPATH = "/html/body/div[6]/div/div/div/div/div/div[1]/div/div[1]"
SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_PE = "/html/body/div[7]/div/div/div/div/div/div[1]/div/div[1]"
SWITCH_TO_CHINESE_LANGUAGE_XPATH_UNDER_PE = "/html/body/div[7]/div/div/div/div/div/div[2]/div/div[1]"
SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_AI_CUT = "/html/body/div[7]/div/div/div/div/div/div[1]/div/div[1]"
SWITCH_TO_CHINESE_LANGUAGE_XPATH_UNDER_AI_CUT = "/html/body/div[7]/div/div/div/div/div/div[2]/div/div[1]"
SWITCH_TO_CHINESE_LANGUAGE_XPATH_ON_AI_CUT_HOME = "/html/body/div[6]/div/div/div/div/div/div[2]/div/div[1]"
SWITCH_TO_ENGLISH_LANGUAGE_XPATH_ON_AI_CUT_HOME = "/html/body/div[7]/div/div/div/div/div/div[1]/div/div[1]"
SWITCH_TO_ENGLISH_LANGUAGE_CSS_SELECTOR = "#haimeta > div:nth-child(8) > div > div > div > div > div > div:nth-child(1) "
SWITCH_TO_CHINESE_LANGUAGE_CSS_SELECTOR = "#haimeta > div:nth-child(8) > div > div > div > div > div > div:nth-child(2)  "
SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_SE="/html/body/div[7]/div/div/div/div/div/div[1]/div/div[1]"
SWITCH_TO_CHINESE_LANGUAGE_XPATH_UNDER_SE="/html/body/div[7]/div/div/div/div/div/div[2]/div/div[1]"
SWITCH_TO_ENGLISH_LANGUAGE_XPATH_ON_SE_HOME = "/html/body/div[6]/div/div/div/div/div/div[1]/div/div[1]"
SWITCH_TO_CHINESE_LANGUAGE_XPATH_ON_SE_HOME = "/html/body/div[7]/div/div/div/div/div/div[2]/div/div[1]"
SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_HDE="/html/body/div[7]/div/div/div/div/div/div[1]/div/div[1]"
SWITCH_TO_CHINESE_LANGUAGE_XPATH_UNDER_HDE="/html/body/div[7]/div/div/div/div/div/div[2]/div/div[1]"
SWITCH_TO_ENGLISH_LANGUAGE_XPATH_ON_HDE_HOME = "/html/body/div[6]/div/div/div/div/div/div[1]/div/div[1]"
SWITCH_T0_CHINESE_LANGUAGE_XPATH_ON_HDE_HOME = "/html/body/div[6]/div/div/div/div/div/div[2]/div/div[1]"
SWITCH_TO_ENGLISH_LANGUAGE_XPATH_UNDER_CREATE_AS_U_LIKE="/html/body/div[11]/div/div/div/div/div/div[1]/div/div/span"
SWITCH_TO_CHINESE_LANGUAGE_XPATH_UNDER_CREATE_AS_U_LIKE="/html/body/div[9]/div/div/div/div/div/div[2]/div/div[1]/span"

# Billing history page locators
BUY_HAIBIT_BUTTON_ON_PE_XPATH = "/html/body/div[1]/div/div[1]/div[1]/div/div[3]/div[4]/div[1]"
PURCHASE_HAIBIT_ON_BILLING_HISTORY = "/html/body/div[1]/div/div[5]/div[2]/div[1]/div[4]/div[2]"
HAIBIT_PURCHASE_SELECTION_XPATH = "/html/body/div[1]/div/div[5]/div[2]/div[1]/div[2]/div[1]/div[2]"
COMFIRM_PAYMENT_IN_PURCHASE_HAIBIT_XPATH = "/html/body/div[1]/div/div[5]/div[2]/div[1]/div[2]/div[2]/div[2]/button"
PURCHASE_HAIBIT_INPUT_CARD_NUMBER_XPATH = "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/form/div/div[2]/div[1]/div/div[1]/div/div[1]/input"
PURCHASE_HAIBIT_INPUT_CARD_AVAILABLE_XPATH = "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/form/div/div[2]/div[2]/div/div[1]/div/div/input"
PURCHASE_HAIBIT_INPUT_CARD_SECURE_NUMBER_XPATH = "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/form/div/div[2]/div[3]/div/div[1]/div/div[1]/input"
PURCHASE_HAIBIT_PAY_NOW_BUTTON_id = "button-text"

# Create As You Like page locators
REFINE_YOUR_IDEA_BUTTON_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[3]/div/div/div[4]/div/div[2]/img"
SIZE_OF_GENERATION_BUTTON_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[7]/div/div[2]/div/div[4]"
NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[8]/div/div/div/div[1]"
INTERACTED_IMAGE_1_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div"
DOWNLOAD_BUTTON_XPATH_CAYL_AND_SINGLE_PHOTO_ABLUM="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/span"
PUBLISH_BUTTON_XPATH_CAYL="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/span"
PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_CAYL= "/html/body/div[10]/div/ul/li[1]/span"
TITLE_INPUT_XPATH="/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[4]/div[2]/div[1]/div[2]/span/textarea"
DESCRIPTION_INPUT_XPATH="/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[4]/div[2]/div[2]/div[2]/span/textarea"
CONFIRM_PUBLISH_BUTTON_XPATH="/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[4]/div[3]/div/button"
CANCEL_PUBLISH_BUTTON_XPATH_CAYL="/html/body/div[11]/div/ul/li[1]/span"
PUBLISH_ON_STYLE_LIBRARY_BUTTON_XPATH= "/html/body/div[11]/div/ul/li[2]/span"
STYLE_NAME_INPUT_XPATH="/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/div[2]/div/textarea"
AGREE_TERMS_BUTTON_XPATH="/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[1]/div[2]/div[7]/label/span"
PUBLISH_ON_STYLE_LIBRARY_CONFIRM_BUTTON_XPATH="/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[1]/div[2]/div[5]/button"
REPORT_BUTTON_XPATH_CAYL="/html/body/div[9]/div/ul/li[2]/span"
REPORT_BUTTON_AFTER_PUBLISH_ON_STYLE_LIBRARY_XPATH="/html/body/div[11]/div/ul/li/span/div/p"
REPORT_TYPE_BUTTON_XPATH="/html/body/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div"
REPORT_REASON_INPUT_XPATH="/html/body/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/textarea"
CONFIRM_REPORT_BUTTON_XPATH="/html/body/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/button"
THREE_DOTS_BUTTON_XPATH_CAYL="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div"
INPUT_SKIN_TEXTURE_SINGLE_PHOTO_ALBUM="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[5]/div/div/div/div[2]/div/div/div[2]/div[2]/input"


# PHOTO ALBUM page locators
PHOTO_ALBUM_UPLOAD_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/span/div/span/input"
CHOOSE_PHOTO_GENERATION_STYLE_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div[1]/div"
INPUT_SKIN_TEXTURE_ID_PHOTO_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[7]/div/div/div/div[2]/div/div/div[2]/div[2]/input"
CREATE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/button"
ITEM_TO_BE_INTERACTED_XPATH_ID="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div"
DELETE_BUTTON_XPATH="/html/body/div[13]/div/ul/li[1]/span/div/p"
CONFIRM_DELETE_BUTTON_XPATH= "/html/body/div[1]/div/div[3]/div/div/div/button[2]"
SET_SIZE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/i"
INS_SIZE_BUTTON_XPATH="/html/body/div[9]/div/div/div/div/div/div/div/div/ul/div[4]/div/div/span[1]"
SET_LAYOUT_BUTTON_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/i"
FIVE_INCHES_LAYOUT_BUTTON_XPATH="/html/body/div[10]/div/div/div/div/div/div/div/div/ul/div[2]/div/div/span[1]"
SINGLE_LAYOUT_BUTTON_XPATH="/html/body/div[10]/div/div/div/div/div/div/div/div/ul/div[1]/div/div/span[1]"
AFTER_LAYOUT_EDIT_PHOTO_LOCATION_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div"
AFTER_LAYOUT_EDIT_PHOTO_DOWNLOAD_BUTTON_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[9]/div[2]/div/span"
ID_PHOTO_IFRAME_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/iframe"
DOWNLOAD_BUTTON_XPATH_ID_PHOTO="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/span"
PUBLISH_BUTTON_XPATH_ID_PHOTO="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div[3]/div/span"
REPORT_BUTTON_XPATH_ID_PHOTO_SINGLE_PHOTO_ALBUM="/html/body/div[9]/div/ul/li[2]/span/div/p"
PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_ID_PHOTO= "/html/body/div[9]/div/ul/li[1]/span/div/p"
CANCEL_PUBLISH_BUTTON_XPATH_ID_PHOTO="/html/body/div[9]/div/ul/li[1]/span/div/p"
THREE_DOTS_BUTTON_XPATH_ID_PHOTO="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div/i"
CONFIRM_DELETE_BUTTON_XPATH= "/html/body/div[1]/div/div[3]/div/div/div/button[2]"
EDITED_LAYOUT_PHOTO_LOCATION_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div"
DOWNLOAD_EDITED_LAYOUT_PHOTO_BUTTON_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[9]/div[2]/div/span"
DELETE_BUTTON_XPATH_ID_PHOTO="/html/body/div[11]/div/ul/li[1]/span/div/p"
SECOND_ITEM_SELECTED_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div/div"
NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_PHOTO_ALBUM="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[6]/div/div/div/div[1]"

# CHINESE AESTETICS page locators
PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_SINGLE_PHOTO_ALBUM= "/html/body/div[9]/div/ul/li[1]/span/div/p"
CANCEL_PUBLISH_BUTTON_XPATH_SINGLE_PHOTO_ALBUM="/html/body/div[10]/div/ul/li[1]/span/div/p"
THREE_DOTS_BUTTON_XPATH_SINGLE_PHOTO_ALBUM="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/i"
REPORT_BUTTON_XPATH_SINGLE_PHOTO_ALBUM="/html/body/div[10]/div/ul/li[2]/span/div/p"
DELETE_BUTTON_XPATH_SINGLE_PHOTO_ALBUM="/html/body/div[10]/div/ul/li[1]/span/div/p"
PUBLISH_BUTTON_XPATH_SINGLE_PHOTO_ALBUM="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/span"

# DOUBLE PHOTO ALBUM page locators
INPUT_SKIN_TEXTURE_ARABIAN_DREAMS_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[5]/div/div/div/div[2]/div/div/div[2]/div[2]/input"
FIRST_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div/div/span/div/span/input"
SECOND_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[3]/div/div/span/div/span/input"

# Test credentials
VALID_EMAIL_ACCOUNT = "1974440719@qq.com"
VALID_PASSWORD = "Tiejiayu666"
TEST_FEMALE_PHOTO=r'D:\PycharmProjects\PythonProject\UploadMaterial\WomenTest.png'
TEST_MALE_PHOTO=r'D:\PycharmProjects\PythonProject\UploadMaterial\Mantest.png'
TEST_IMAGE=r'D:\PycharmProjects\PythonProject\UploadMaterial\TestUpload.png'
TEST_SKETCH_IMAGE=r'D:\PycharmProjects\PythonProject\UploadMaterial\sketch.png'
TEST_PRODUCT_IMAGE=r'D:\PycharmProjects\PythonProject\UploadMaterial\Bag_image.png'
TEST_IP_IMAGE=r'D:\PycharmProjects\PythonProject\UploadMaterial\PandaIPimage.png'
TEST_HOME_DESIGN_IMAGE=r'D:\PycharmProjects\PythonProject\UploadMaterial\homedesign.jpg'
# 存储宠物图片数据集的路径
PET_IMAGE_DATA_SET = [
    r'D:\PycharmProjects\PythonProject\UploadMaterial\cat\image_1.png',
    r'D:\PycharmProjects\PythonProject\UploadMaterial\cat\image_2.png', 
    r'D:\PycharmProjects\PythonProject\UploadMaterial\cat\image_3.png',
    r'D:\PycharmProjects\PythonProject\UploadMaterial\cat\image_4.png',
    r'D:\PycharmProjects\PythonProject\UploadMaterial\cat\image_5.png',
    r'D:\PycharmProjects\PythonProject\UploadMaterial\cat\image_6.png'
]


# Create clothes page locators
DOWNLOAD_PATTERN_BUTTON_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/button"
ADD_NEW_IMAGE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div[1]/i"
INTERACTED_IMAGE_2_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[1]"
UPLOAD_IMAGE_CREATE_CLOTHES_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[5]/div/div[1]/div/span/div/span/input"
REPORT_BUTTON_CREATE_CLOTHES_XPATH="/html/body/div[10]/div/ul/li[2]/span/div/p"

# Pet page locators
PET_SECTION_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[3]/div"
STYLE_YOUR_PET_ON_HOME_UNDER_PET_SECTION_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div"
START_TRAINING_BUTTON_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[3]/div/div[1]/div/div/div[3]/span/div/span/div/div/div[2]/span[2]/button"
CREATE_BUTTON_XPATH_STYLE_YOUR_PET="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/button/div/span"
UPLOAD_IMAGE_STYLE_YOUR_PET_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[3]/div/div[1]/div/div/div[3]/span/div/span/input"
ADD_PET_DATA_SET_BUTTON_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div/div[1]/i"


# T2I page locators
STYLE_CHOICE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div"
STYLE_CHOICE_BUTTON_XPATH_T2I_WITHE_REFINING="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[6]/div/div/div[2]/div/div/div[1]"
SIZE_OF_GENERATION_BUTTON_XPATH_T2I="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/img"
NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_T2I="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[4]/div/div/div/div[1]"
CREATE_BUTTON_XPATH_T2I="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/button/div/span"
CANCEL_PUBLISH_BUTTON_XPATH_T2I="/html/body/div[10]/div/ul/li[1]/span/div/p"
REPORT_BUTTON_XPATH_T2I="/html/body/div[10]/div/ul/li[2]/span/div/p"
THREE_DOTS_BUTTON_XPATH_T2I="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/i"
DELETE_BUTTON_XPATH_T2I="/html/body/div[10]/div/ul/li[1]/span/div/p"
SIZE_OF_GENERATION_BUTTON_XPATH_T2I_WITHE_REFINING="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[7]/div/div[2]/div/div[4]/div/div"
NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_T2I_WITHE_REFINING="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[8]/div/div/div/div[1]"
PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_T2I_WITHE_REFINING= "/html/body/div[10]/div/ul/li[1]/span/div/p"
CANCEL_PUBLISH_BUTTON_XPATH_T2I_WITHE_REFINING="/html/body/div[11]/div/ul/li[1]/span/div/p"
PUBLISH_BUTTON_XPATH_T2I_WITHE_REFINING="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/span"
CREATE_BUTTON_XPATH_I2I="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/button"

# I2I page locators
UPLOAD_IMAGE_BUTTON_XPATH_I2I="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/span/div/span/input"
STYLE_CHOICE_BUTTON_XPATH_I2I="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div[1]/div"
SIZE_OF_GENERATION_BUTTON_XPATH_I2I="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[4]/div/div[2]/div/div[4]/div/div"
NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_I2I="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[5]/div/div/div/div[1]"
DOWNLOAD_BUTTON_XPATH_I2I="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/span"
PUBLISH_BUTTON_XPATH_I2I="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/span"
PUBLISH_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_I2I="/html/body/div[9]/div/ul/li[1]/span/div/p"
CANCEL_PUBLISH_BUTTON_XPATH_I2I="/html/body/div[9]/div/ul/li[1]/span/div/p"
THREE_DOTS_BUTTON_XPATH_I2I="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/i"
REPORT_BUTTON_XPATH_I2I="/html/body/div[9]/div/ul/li[2]/span/div/p"
DELETE_BUTTON_XPATH_I2I="/html/body/div[9]/div/ul/li[1]/span/div/p"
RENDERING_RESULT_XPATH_I2I="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[4]/div/div/div/div[1]"
STYLE_CHOICE_BUTTON_XPATH_I2I_TEXTURE_TRANSFER="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[3]/div/div/div[2]/div/div/div[1]"
NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_I2I_PERSONAL_AVATAR="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[4]/div/div/div/div[1]"
STYLE_CHOICE_BUTTON_XPATH_I2I_HOME_DESIGN="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[3]/div/div/div[2]/div/div/div[1]"
NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_I2I_HOME_DESIGN="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[4]/div/div/div/div[1]"


# Configuration
COOKIE_FILE = "../cookies.json"
LOGIN_URL = "https://preview.haimeta.com/login"
HOME_URL = "https://preview.haimeta.com/"
