from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SabyMainPage(BasePage):

    PAGE_ADRESS = "https://saby.ru"
    header_contacts_CSS = "li.sbisru-Header__menu-item:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)"
    header_contacts_menu_CSS = "div.sbisru-Header-ContactsMenu:nth-child(2)"
    header_contacts_link_CSS2 = "a[href='/contacts']" 
    footer_contacts_link_CSS = "a.sbisru-Footer__link[href='/contacts']"

    def __init__(self, browser):
        super().__init__(browser)

    def find_contacts(self):
        return self.find(By.CSS_SELECTOR, self.header_contacts_CSS)

    def hover_header_contacts(self):  
        contacts_element = self.find_contacts()

        ActionChains(self.driver).move_to_element(contacts_element).perform()
        wait = WebDriverWait(self.driver, 3)
        popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.header_contacts_menu_CSS)))
        return popup

    def get_header_contacts_link(self):
        headerContactsPopup = self.hover_header_contacts()
        link = headerContactsPopup.find_element(By.CSS_SELECTOR, self.header_contacts_link_CSS2)
        return link

    def click_header_contacts_link(self):
        link = self.get_header_contacts_link()
        link.click()

    def get_footer_contacts_link(self):
        link = self.find(By.CSS_SELECTOR, self.footer_contacts_link_CSS)
        return link

    def click_footer_contacts_link(self):
        link = self.get_footer_contacts_link()
        link.click()

    def open(self, url = PAGE_ADRESS):
        super().open(url)

    