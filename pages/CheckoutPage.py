from selenium.webdriver.common.by import By
from helper.SeleniumHelper import SeleniumHelper
import time


class CheckoutPage(SeleniumHelper):
    HOME_PAY_NOW_BUTTON = (By.XPATH, "//button[contains(@class, 'MuiButton-containedPrimary')]")
    SPLIT_THE_BILL_BUTTON = (By.XPATH, "//button[contains(@class, 'MuiButton-containedLightPrimary')]")
    SELECT_CUSTOM_AMOUNT = (By.XPATH, "// button[ @id = 'select-custom']")
    SEND_CUSTOM_AMOUNT = (By.XPATH, "//*[@name='amount']")
    CONFIRM_CUSTOM_AMOUNT = (By.XPATH, "//*[@id='split-bill']")
    TIP_5 = (By.XPATH, "//*[@id='tip_5']")
    TIP_10 = (By.XPATH, "//*[@id='tip_10']")
    TIP_15 = (By.XPATH, "//*[@id='tip_15']")
    CARD_NUMBER = (By.XPATH, "//*[@id='cardNumber']")
    CARD_EXPIRED_DATE = (By.XPATH, "//*[@id='expiryDate']")
    CARD_CVV = (By.XPATH, "//*[@id='cvv']")
    PAY_NOW_BUTTON = (By.XPATH, "//*[@id='checkout-action-btn']")
    PAYMENT_PASSWORD = (By.XPATH, "//input[@id='password']")
    CONTINUE_BUTTON = (By.XPATH, "//*[@id='txtButton']")
    IFRAME = 'cko-3ds2-iframe'

    def __init__(self, driver):
        super().__init__(driver)

    def click_pay_now_home(self):
        self.webelement_click(self.HOME_PAY_NOW_BUTTON)

    def click_split_the_bill(self):
        self.webelement_click(self.SPLIT_THE_BILL_BUTTON)

    def configure_custom_amount(self, amount):
        self.webelement_click(self.SELECT_CUSTOM_AMOUNT)
        self.webelement_enter(self.SEND_CUSTOM_AMOUNT, amount)
        self.webelement_click(self.CONFIRM_CUSTOM_AMOUNT)

    def click_tip_option(self, tip):
        if tip == 5:
            self.webelement_click(self.TIP_5)
        elif tip == 10:
            self.webelement_click(self.TIP_10)
        elif tip == 15:
            self.webelement_click(self.TIP_15)
        else:
            self.webelement_click(self.TIP_5)

    def enter_card_information(self, card_number, card_expired_date, card_cvv):
        self.scroll_to_bottom()
        self.webelement_enter(self.CARD_NUMBER, card_number)
        self.webelement_click(self.CARD_EXPIRED_DATE)
        self.webelement_enter(self.CARD_EXPIRED_DATE, card_expired_date)
        self.webelement_enter(self.CARD_CVV, card_cvv)

    def click_pay_now(self, password):
        self.webelement_click(self.PAY_NOW_BUTTON)
        time.sleep(2)
        self.switch_frame(self.IFRAME)
        self.webelement_click(self.PAYMENT_PASSWORD)
        self.webelement_enter(self.PAYMENT_PASSWORD, password)
        self.webelement_click(self.CONTINUE_BUTTON)

    def payment_success_verification(self, msg):
        self.verify_success_url(msg)
