from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TensorMainPage(BasePage):

    PAGE_ADRESS = "https://tensor.ru/"
    PEOPLE_STRONG_BLOCK_CSS = ".tensor_ru-Index__block4"
    PEOPLE_STRONG_BLOCK_MORELINK_CSS = "a[href*='/about']"

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        super().open(self.PAGE_ADRESS)

    def people_strong_block_is_visible(self, timeout = 10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, self.PEOPLE_STRONG_BLOCK_CSS)))
            return True
        except:
            return False

    def get_people_strong_block_morelink(self):
       link = self.find(By.CSS_SELECTOR, self.PEOPLE_STRONG_BLOCK_MORELINK_CSS)
       return link

    