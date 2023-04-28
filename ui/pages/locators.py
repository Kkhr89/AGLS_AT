"""LOCATORS FOR PAGES"""

from selenium.webdriver.common.by import By


class LoginPageLocators:
    BTN_FEEDBACK_SURVEY = (By.CSS_SELECTOR, 'button.uui-button-box')
    BTN_EPAM_LOGIN = (By.CSS_SELECTOR, 'button.Button__button.Button__blue.SsoAuthLinks__epamSsoButton')
    BTN_GITHUB_LOGIN = (By.CSS_SELECTOR, 'button.Button__button.Button__darkGray')
    BTN_SIGN_IN = (By.CSS_SELECTOR, 'button[type="submit"]')
    BTN_QUICK_ACCESS = (By.CSS_SELECTOR, 'button.Button__button.Button__blueTransparent')
    INPUT_EMAIL = (By.CSS_SELECTOR, 'input[placeholder="Enter Your Email"]')
    INPUT_PASSWORD = (By.CSS_SELECTOR, 'input[placeholder="Enter Your Password"]')
    LINK_HEADER_LOGO = (By.CSS_SELECTOR, 'a[href="/poker"]')
    LINK_RECOVER_MY_PASSWORD = (By.CSS_SELECTOR, 'a.SignInForm__recoverLink')
    LINK_SIGN_UP = (By.CSS_SELECTOR, 'a.TextLink__link')
    TEXT_MAIN_TITLE = (By.CSS_SELECTOR, 'h2.WelcomeTitle__title')
    TEXT_SIGN_IN = (By.CSS_SELECTOR, 'h4.Subtitle__secondaryTitle')
    TEXT_DONT_HAVE_ACCOUNT = (By.CSS_SELECTOR, 'div.TextLink__container > span')
    PIC_EPAM_LOGO = (By.CSS_SELECTOR, 'img[alt="epam-logo"]')
    MODAL_WHATS_NEW = (By.CSS_SELECTOR, 'div.ant-modal-content')
    ERR_MESSAGE_EMAIL = (By.CSS_SELECTOR, 'div[data-testid="text-field-error"]')
    ERR_POP_UP = (By.CSS_SELECTOR, 'div.uui-snackbar-item-self')


class QuickAccessPageLocators:
    BTN_QA_CANCEL = (By.CSS_SELECTOR, 'button.Button__button.Button__blueTransparent')
    BTN_QA_ENTER = (By.CSS_SELECTOR, 'button.Button__button.Button__blue.styles__actionButton')
    INPUT_QA_NAME = (By.CSS_SELECTOR, 'input[placeholder="Enter Your Name"]')
    TEXT_QA_QUICK_ACCESS = (By.CSS_SELECTOR, 'h4.Subtitle__secondaryTitle')
    TEXT_QA_NOTICE = (By.CSS_SELECTOR, 'p.QuickAccessForm__noticeMessage')


class FeedbackModalPageLocators:
    BTN_FB_CLOSE_CROSS = (By.CSS_SELECTOR, 'svg[data-icon="close"]')
    BTN_SCALE_DICT = dict()
    for i in range(1, 11):
        BTN_SCALE_DICT[f"BTN_FB_RADIO_SCALE_{i}"] = (By.CSS_SELECTOR, f'label[for="point{i}"]>div')
    BTN_FB_NOT_NOW = (By.CSS_SELECTOR, 'button.Button__button.Button__gray')
    BTN_FB_SEND = (By.CSS_SELECTOR, 'button.Button__button.Button__limeGreen')
    TEXT_FB_TITLE = (By.CSS_SELECTOR, 'div.ant-modal-title')
    TEXT_FB_SCALE = (By.CSS_SELECTOR, 'div[data-testid="feedback-rating-scale-title"]')
    TEXT_FB_FEEDBACK = (By.CSS_SELECTOR, 'div[data-testid="feedback-comment-title"]')
    INPUT_FB_FEEDBACK = (By.CSS_SELECTOR, 'textarea[data-testid="feedback-comment-field"]')
    WDW_MODAL = (By.CSS_SELECTOR, 'div.ant-modal-content')


class SignUpPageLocators:
    BTN_SU_SIGN_UP = (By.CSS_SELECTOR, 'button[type="submit"]')
    INPUT_SU_FIRST_NAME = (By.CSS_SELECTOR, 'input[placeholder="Enter First Name"]')
    INPUT_SU_LAST_NAME = (By.CSS_SELECTOR, 'input[placeholder="Enter Last Name (Optional)"]')
    INPUT_SU_EMAIL = (By.CSS_SELECTOR, 'input[placeholder="Enter Your Email"]')
    INPUT_SU_PASSWORD = (By.CSS_SELECTOR, 'input[placeholder="Enter Your Password"]')
    INPUT_SU_CONFIRM_PASSWORD = (By.CSS_SELECTOR, 'input[placeholder="Confirm Password"]')
    TEXT_SU_SIGN_UP = (By.CSS_SELECTOR, 'h4.Subtitle__secondaryTitle')
    TEXT_HAVE_ACCOUNT = (By.CSS_SELECTOR, 'div.TextLink__container > span')
    LINK_SU_SIGN_IN = (By.CSS_SELECTOR, 'a.TextLink__link')
    MESSAGE_CONFIRMATION_LINK = (By.CSS_SELECTOR, 'div.uui-snackbar-item-wrapper-right-self>div>div>div>div>div')
    MESSAGE_MAILHOG_MAIL = (By.CSS_SELECTOR, 'div.msglist-message')
    LINK_MAILHOG_CONFIRMATION = (By.CSS_SELECTOR, '#preview-plain > a')

class WhatsNewModalPageLocators:
    MODAL_WHATS_NEW = (By.CSS_SELECTOR, 'div[style="width: 820px;"]')
    TITLE_WHATS_NEW = (By.CSS_SELECTOR, 'div#rcDialogTitle2')
    TITLE_LATEST_RELEASE = (By.CSS_SELECTOR, 'div[data-testid="whats-new-title-wrapper"]>:nth-child(1)')
    TITLE_NEW_FEATURES = (By.CSS_SELECTOR, 'div[data-testid="whats-new-features-block"]>div')
    TITLE_BUGS = (By.CSS_SELECTOR, 'div[data-testid="whats-new-fixed-bugs-title"]')
    TEXT_RELEASE_DATE = (By.CSS_SELECTOR, 'div[data-testid="whats-new-title-wrapper"]>:nth-child(2)')
    LIST_NEW_FEATURES = (By.CSS_SELECTOR, 'div[data-testid="whats-new-features-block"]>ul')
    LIST_BUGS = (By.CSS_SELECTOR, 'ul[data-testid="whats-new-fixed-bugs-list"]')
    BTN_WHATS_NEW_CLOSE_CROSS = (By.CSS_SELECTOR,
                                 'div:nth-child(4)>div>.ant-modal-wrap>div>.ant-modal-content>button')
    BTN_GOT_IT = (By.CSS_SELECTOR,
                  'div:nth-child(6)>div>div.ant-modal-wrap>div>div.ant-modal-content>div.ant-modal-footer>button')
