import pytest
from pages.saby_main_page import SabyMainPage
from pages.saby_contacts_page import SabyContactsPage
from pages.tensor_main_page import TensorMainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_sabyHeaderContactsLink(browser):
    sabyMainPage = SabyMainPage(browser)
    sabyMainPage.open()
    sabyMainPage.click_header_contacts_link()
    assert "saby.ru/contacts" in browser.current_url

def test_sabyContactsBannerClick(browser):

    sabyContactsPage = SabyContactsPage(browser)
    sabyContactsPage.open()
    sabyContactsPage.click_tensor_banner()
    assert "tensor.ru" in browser.current_url

def test_tensorPeopleStrongBlockVisible(browser):

    tensorMainPage = TensorMainPage(browser)
    tensorMainPage.open()
    result = tensorMainPage.people_strong_block_is_visible()
    assert result == True

def test_openTensorPeopleStrongBlockMoreLink(browser):

    tensorMainPage = TensorMainPage(browser)
    tensorMainPage.open()
    tensorMainPage.get_people_strong_block_morelink().click()
    WebDriverWait(browser, 10).until(EC.url_contains("tensor.ru/about"))
    assert "tensor.ru/about" in browser.current_url