from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TensorAboutPage(BasePage):

    PAGE_ADRESS = "https://tensor.ru/about"
    WORKING_BLOCK_CSS = ".tensor_ru-Index__block4 a[href*='/about']"

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        super().open(self.PAGE_ADRESS)

    