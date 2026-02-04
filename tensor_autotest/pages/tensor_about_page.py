from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TensorAboutPage(BasePage):

    PAGE_ADRESS = "https://tensor.ru/about"
    WORKING_BLOCK_CSS = "div.tensor_ru-container:nth-child(4)"

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        super().open(self.PAGE_ADRESS)

    def get_working_block(self):
        return self.find(By.CSS_SELECTOR, self.WORKING_BLOCK_CSS)

    def get_images_from_working_block(self):
        return self.get_working_block().find_elements(By.TAG_NAME, "IMG")
    