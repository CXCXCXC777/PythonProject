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
EDITION_ON_HOME_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[1]"
BG_REMOVER_ON_HOME_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]"
SMART_ERASER_ON_HOME_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[1]/div/div[3]"
HD_ENLARGE_ON_HOME_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[1]/div/div[4]"
HD_REPAIR_ON_HOME_BUTTON_XPATH = "/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[1]/div/div[5]"
CREATE_AS_YOU_LIKE_ON_HOME_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div[2]"
STYLE_YOUR_PET_ON_HOME_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]"
LIFE_BUTTON_ON_HOME_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[3]"
WORK_BUTTON_ON_HOME_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[4]"
BUZZ_BUTTON_ON_HOME_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[1]"
LOVE_IN_THE_AIR_BUTTON_UNDER_LIFE_BUTTON_XPATH="/html/body/div[1]/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div/div[3]/div[2]"



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

# Billing history page locators
BUY_HAIBIT_BUTTON_ON_PE_XPATH = "/html/body/div[1]/div/div[1]/div[1]/div/div[3]/div[4]/div[1]"
PURCHASE_HAIBIT_ON_BILLING_HISTORY = "/html/body/div[1]/div/div[5]/div[2]/div[1]/div[4]/div[2]"
HAIBIT_PURCHASE_SELECTION_XPATH = "/html/body/div[1]/div/div[5]/div[2]/div[1]/div[2]/div[1]/div[2]"
COMFIRM_PAYMENT_IN_PURCHASE_HAIBIT_XPATH = "/html/body/div[1]/div/div[5]/div[2]/div[1]/div[2]/div[2]/div[2]/button"
PURCHASE_HAIBIT_INPUT_CARD_NUMBER_XPATH = "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/form/div/div[2]/div[1]/div/div[1]/div/div[1]/input"
PURCHASE_HAIBIT_INPUT_CARD_AVAILABLE_XPATH = "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/form/div/div[2]/div[2]/div/div[1]/div/div/input"
PURCHASE_HAIBIT_INPUT_CARD_SECURE_NUMBER_XPATH = "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/form/div/div[2]/div[3]/div/div[1]/div/div[1]/input"
PURCHASE_HAIBIT_PAY_NOW_BUTTON_id = "button-text"

# Test credentials
VALID_EMAIL_ACCOUNT = "1974440719@qq.com"
VALID_PASSWORD = "Tiejiayu666"

# Configuration
COOKIE_FILE = "cookies.json"
LOGIN_URL = "https://preview.haimeta.com/login"
HOME_URL = "https://preview.haimeta.com/"