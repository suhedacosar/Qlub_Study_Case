from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SeleniumHelper:

    def __init__(self, driver):
        self.driver = driver

    def webelement_enter(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
        time.sleep(3)

    def webelement_click(self, locator):
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(locator)).click()
        time.sleep(2)

    def verify_success_url(self, msg):
        time.sleep(2)
        url = self.driver.current_url
        assert msg in url

    def switch_frame(self, iframe):  # switch frame to reach iframe elements
        time.sleep(5)
        self.driver.switch_to.frame(iframe)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")









