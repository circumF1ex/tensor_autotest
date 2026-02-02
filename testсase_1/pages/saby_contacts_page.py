from pages.base_page import BasePage

from selenium.webdriver.common.by import By

class SabyContactsPage(BasePage):

    PAGE_ADRESS = "https://saby.ru/contacts"
    TENSOR_BANNER_CSS = ".sbisru-Contacts__border-left--border-xm > a:nth-child(1)"

    def __init__(self, browser):
        super().__init__(browser)

    def find_tensor_banner(self):
        return self.find(By.CSS_SELECTOR, self.TENSOR_BANNER_CSS)

    def get_tensor_banner_link(self):
        return self.find_tensor_banner().get_attribute("href")

    def click_tensor_banner(self):
        super().open(self.get_tensor_banner_link())

    def open(self):
        super().open(self.PAGE_ADRESS)