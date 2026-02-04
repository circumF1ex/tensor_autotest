from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SabyContactsPage(BasePage):

    PAGE_ADRESS = "https://saby.ru/contacts"

    TENSOR_BANNER_CSS = ".sbisru-Contacts__border-left--border-xm > a:nth-child(1)"
    REGION_CSS = ".sbis_ru-Region-Chooser.ml-16.ml-xm-0"
    PARTNERS_LIST_CSS = '#contacts_list'
    REGION_PANEL_CSS = '.sbis_ru-Region-Panel.sbis_ru-Region-Panel-l'
    KAMCHATSKY_KRAY_CSS = "li.sbis_ru-Region-Panel__item:nth-child(43) > span:nth-child(1) > span:nth-child(1)"

    def __init__(self, browser):
        super().__init__(browser)

    def find_tensor_banner(self):
        return self.find(By.CSS_SELECTOR, self.TENSOR_BANNER_CSS)

    def get_tensor_banner_link(self):
        return self.find_tensor_banner().get_attribute("href")

    def get_region_element(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.REGION_CSS)))
        return self.find(By.CSS_SELECTOR, self.REGION_CSS)

    def get_region_name(self):
        region = self.get_region_element()
        return region.text

    def click_region_element(self):
        self.get_region_element().click()

    def get_kamchatsky_kray_link(self):
        pass
    
    def click_kamchatsky_kray_link(self):
        self.click_region_element()
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.REGION_PANEL_CSS)))
        
        region_panel = self.find(By.CSS_SELECTOR, self.REGION_PANEL_CSS)
        kamchatsky_kray_link = region_panel.find_element(
            By.CSS_SELECTOR, self.KAMCHATSKY_KRAY_CSS)
        
        self.driver.execute_script("arguments[0].scrollIntoView(true);", kamchatsky_kray_link)
        self.driver.execute_script("arguments[0].click();", kamchatsky_kray_link)
        
    def get_partners(self):
        partners = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.PARTNERS_LIST_CSS))
        )

        return len(partners) > 0

    def click_tensor_banner(self):
        link = self.get_tensor_banner_link()
        super().open(link)

    def open(self, url = PAGE_ADRESS):
        super().open(url)