import pytest
from conftest import *
from pages.CheckoutPage import CheckoutPage


@pytest.mark.usefixtures("browser_setup")
class TestCheckout:

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.checkout_page = CheckoutPage(self.driver)

    # Amount,Tip,Card Info can be changed from "conftest.py"
    def test_valid_split_checkout_tip_included(self):
        self.checkout_page.click_pay_now_home()
        self.checkout_page.click_split_the_bill()
        self.checkout_page.configure_custom_amount(Amount)
        self.checkout_page.click_tip_option(Tip)
        self.checkout_page.enter_card_information(CardNumber, CardExpiredDate, CardCvv)
        self.checkout_page.click_pay_now(Password)
        self.checkout_page.payment_success_verification(msg)

    def teardown_class(self):
        self.driver.quit()
