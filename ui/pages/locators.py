'''LOCATORS FOR PAGES'''

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
