# Login page locators
from selenium.webdriver.remote.switch_to import SwitchTo


EMAIL_INPUT_XPATH = "/html/body/div/div/div[3]/div/div/div/form/div[1]/div/input"
CONTINUE_BUTTON_XPATH = "/html/body/div/div/div[3]/div/div/div/form/div[2]/button"
PASSWORD_INPUT_XPATH = "/html/body/div/div/div[3]/div/div/div[1]/form/div[1]/div/div/input"
LOGIN_BUTTON_XPATH = "/html/body/div/div/div[3]/div/div/div[1]/form/button"
USER_DISPLAY_ClASS_NAME = "clip-path"

# Third party login locators
THIRD_PARTY_BUTTON_XPATH = "/html/body/div/div/div[3]/div/div/div/form/div[3]/div/div[2]/button"
THIRD_PARTY_NEXT_BUTTON_XPATH = "/html/body/div/div/div[3]/div/div/div/button"

# Privacy policy and USER SERVICE locators
PRIVACY_POLICY_LINK_XPATH = "/html/body/div/div/div[3]/div/div/div/div[4]/div/div/span[2]"
PRIVACY_POLICY_CHECK_MESSAGE = "/html/body/div/div/div/div/p[1]/span[37]"
PRIVACY_POLICY_BACK_BUTTON = "/html/body/div/div/button"
USER_SERVICE_PRIVACY_LINK_XPATH = "/html/body/div/div/div[3]/div/div/div/div[4]/div/div/span[1]"
USER_SERVICE_PRIVACY_CHECK_MESSAGE = "/html/body/div/div/div/div/p[3]/span[44]"
USER_SERVICE_BACK_BUTTON = "/html/body/div/div/button"
ERROR_MESSAGE_ON_LOGIN_PAGE_XPATH = "/div/div/div/span[2]"

# Home page locators
GET_VERIFICATION_CODE_BUTTON_XPATH = "/html/body/div/div/div[3]/div/div/div[1]/div[2]"
EDITION_ON_HOME_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[1]/div/div[1]/span/div[1]"
BG_REMOVER_ON_HOME_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[1]/div/div[2]/span/div[1]"
SMART_ERASER_ON_HOME_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[1]/div/div[3]/span/div[1]"
HD_ENLARGE_ON_HOME_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[1]/div/div[4]/span/div[1]"
HD_REPAIR_ON_HOME_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[1]/div/div[5]/span/div[1]"
LIFE_BUTTON_ON_HOME_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[3]"
WORK_BUTTON_ON_HOME_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[4]"
BUZZ_BUTTON_ON_HOME_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[1]"
ID_PHOTO_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[6]/div/div/div[3]/div[2]/div"
CHINESE_AESTHETICS_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[7]/div/div/div[3]/div[2]/div"
ARABIAN_DREAMS_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[8]/div/div/div[3]/div[2]/div"
NANYANG_MEMORY_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[9]/div/div/div[3]/div[2]"
EAST_ASIAN_CULTURE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[10]/div/div/div[3]/div[2]"
CYBER_FUTURE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[11]/div/div/div[3]/div[2]"
GORGEOUS_ROAD_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[12]/div/div/div[3]/div[2]"
FANTASY_TALES_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[13]/div/div/div[3]/div[2]"

# HAI CREATE LIFE page locators
STYLE_YOUR_PET_ON_HOME_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div[2]"
BFF_MOMENT_BUTTON_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]"
LOVE_IN_THE_AIR_BUTTON_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div/div[3]/div[2]"
BRO_SHOW_BUTTON_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[4]/div/div/div[3]/div[2]"
PET_MASTERPICE_BUTTON_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[5]/div/div/div[3]/div[2]"
ID_PHOTOS_BUTTON_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[6]/div/div/div[3]/div[2]"
CHINESE_AESTHETICS_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[7]/div/div/div[3]/div[2]"
ARBIAN_DREAM_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[8]/div/div/div[3]/div[2]"
NANYANG_MEMORY_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[9]/div/div/div[3]/div[2]"
EAST_ASIAN_CULTURE_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[10]/div/div/div[3]/div[2]"
CYBER_FUTURE_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[11]/div/div/div[3]/div[2]"
GORGEOUS_ROAD_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[12]/div/div/div[3]/div[2]"
FANTASY_TALES_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[13]/div/div/div[3]/div[2]"

#HAI CREATE WORK page locators
CREATE_CLOTHES_UNDER_WORK_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div[2]"
CREATE_NAIL_ART_UNDER_WORK_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]"
CREATE_TOY_UNDER_WORK_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div/div[3]/div[2]"
CREATE_CHARACTER_UNDER_WORK_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[4]/div/div/div[3]/div[2]"
CREATE_LOGO_UNDER_WORK_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[5]/div/div/div[3]/div[2]"
CHARACTER_TEXTURE_UNDER_WORK_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[6]/div/div/div[3]/div[2]"
CREATE_TATTO_UNDER_WORK_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[7]/div/div/div[3]/div[2]"
ME_TIME_UNDER_WORK_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[8]/div/div/div[3]/div[2]"
CREATE_PRODUCT_UNDER_WORK_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[9]/div/div/div[3]/div[2]"
CHARACTER_PORTRAIT_UNDER_WORK_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[10]/div/div/div[3]/div[2]"
STOCK_IMAGE_UNDER_WORK_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[11]/div/div/div[3]/div[2]"

#HAI CREATE BUZZ page locators
CREATE_AS_YOU_LIKE_UNDER_BUZZ_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div[2]"
PET_MASTERPICE_BUTTON_UNDER_BUZZ_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]"
ID_PHOTO_BUTTON_UNDER_BUZZ_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div/div[3]/div[2]"
CHINESE_ASTHETICS_UNDER_BUZZ_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[7]/div/div/div[3]/div[2]"
ARBIAN_DREAM_UNDER_BUZZ_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[8]/div/div/div[3]/div[2]"
NANYANG_MEMORY_UNDER_BUZZ_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[9]/div/div/div[3]/div[2]"
CREATE_LOGO_UNDER_BUZZ_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[10]/div/div/div[3]/div[2]"
CHARACTER_PORTRAIT_UNDER_BUZZ_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[11]/div/div/div[3]/div[2]"


#PE page locators
PICTURE_EDITION_UPLOAD_BUTTON_ClASS_NAME = "ant-upload.ant-upload-btn"
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

#Create boost page locators
INPUT_PROMPT_BOX_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[3]/div/div/div[3]"
INPUT_PROMPT_BOX_CLASS_NAME="ant-input.css-otvc0b.textarea-buttons"
INPUT_PROMPT_BOX_XPATH=""
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
FEEDBACK_XPATH="/html/body/div[10]/div/div/div/span[2]"
IMAGE_1_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div"
DOWNLOAD_BUTTON_XPATH_CAYL_AND_SINGLE_PHOTO_ABLUM="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/span"
PUBLISH_BUTTON_XPATH_CAYL="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/span"
PUBLICK_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_CAYL="/html/body/div[10]/div/ul/li[1]/span"
TITLE_INPUT_XPATH="/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[4]/div[2]/div[1]/div[2]/span/textarea"
DESCRIPTION_INPUT_XPATH="/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[4]/div[2]/div[2]/div[2]/span/textarea"
CONFIRM_PUBLISH_BUTTON_XPATH="/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[4]/div[3]/div/button"
CANCEL_PUBLISH_BUTTON_XPATH_CAYL="/html/body/div[11]/div/ul/li[1]/span"
PUBLICK_ON_STYLE_LIBRARY_BUTTON_XPATH="/html/body/div[11]/div/ul/li[2]/span"
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
PHOTO_ALBUM_SECTION_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[3]/div"
# PHOTO ALBUM page locators
PHOTO_ALBUM_UPLOAD_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/span/div/span/input"
CHOOSE_PHOTO_GENERATION_STYLE_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div[1]/div"
INPUT_SKIN_TEXTURE_ID_PHOTO_XPATH = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[7]/div/div/div/div[2]/div/div/div[2]/div[2]/input"
CREATE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/button"
ITEM_TO_BE_INTERACTED_XPATH_ID="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div"
DELETE_BUTTON_XPATH="/html/body/div[13]/div/ul/li[1]/span/div/p"
CONFRIM_DELETE_BUTTON_XPATH="/html/body/div[1]/div/div[3]/div/div/div/button[2]"
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
PUBLICK_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_ID_PHOTO="/html/body/div[9]/div/ul/li[1]/span/div/p"
CANCEL_PUBLISH_BUTTON_XPATH_ID_PHOTO="/html/body/div[9]/div/ul/li[1]/span/div/p"
THREE_DOTS_BUTTON_XPATH_ID_PHOTO="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div/i"
CONFRIM_DELETE_BUTTON_XPATH="/html/body/div[1]/div/div[3]/div/div/div/button[2]"
EDITED_LAYOUT_PHOTO_LOCATION_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div"
DOWNLOAD_EDITED_LAYOUT_PHOTO_BUTTON_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[9]/div[2]/div/span"
DELETE_BUTTON_XPATH_ID_PHOTO="/html/body/div[11]/div/ul/li[1]/span/div/p"
SECOND_ITEM_SELECTED_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div/div"
NUMBER_OF_IMAGES_TO_GENERATE_BUTTON_XPATH_PHOTO_ALBUM="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[6]/div/div/div/div[1]"
# CHINESE AESTETICS page locators
PUBLICK_ON_HAIMETA_COMMUNITY_BUTTON_XPATH_SINGLE_PHOTO_ALBUM="/html/body/div[9]/div/ul/li[1]/span/div/p"
CANCEL_PUBLISH_BUTTON_XPATH_SINGLE_PHOTO_ALBUM="/html/body/div[10]/div/ul/li[1]/span/div/p"
THREE_DOTS_BUTTON_XPATH_SINGLE_PHOTO_ALBUM="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/i"
REPORT_BUTTON_XPATH_SINGLE_PHOTO_ALBUM="/html/body/div[10]/div/ul/li[2]/span/div/p"
DELETE_BUTTON_XPATH_SINGLE_PHOTO_ALBUM="/html/body/div[10]/div/ul/li[1]/span/div/p"
PUBLISH_BUTTON_XPATH_SINGLE_PHOTO_ALBUM="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/span"

# ARABIAN DREAMS page locators
INPUT_SKIN_TEXTURE_ARABIAN_DREAMS_XPATH="/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[5]/div/div/div/div[2]/div/div/div[2]/div[2]/input"


FIRST_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div/div/span/div/span/input"
SECOND_UPLOAD_BUTTON_XPATH_FOR_DOUBLE_PHOTO_ABLUM = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[3]/div/div/span/div/span/input"

# Test credentials
VALID_EMAIL_ACCOUNT = "1974440719@qq.com"
VALID_PASSWORD = "Tiejiayu666"
TEST_FEMALE_PHOTO=r'D:\PycharmProjects\PythonProject\WomenTest.png'
TEST_MALE_PHOTO=r'D:\PycharmProjects\PythonProject\Mantest.png'


# Configuration
COOKIE_FILE = "../cookies.json"
LOGIN_URL = "https://preview.haimeta.com/login"
HOME_URL = "https://preview.haimeta.com/"
