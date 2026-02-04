import pytest
from pages.saby_main_page import SabyMainPage
from pages.saby_contacts_page import SabyContactsPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_about_page import TensorAboutPage
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

def test_tensorOpenPeopleStrongBlockMoreLink(browser):

    tensorMainPage = TensorMainPage(browser)
    tensorMainPage.open()
    tensorMainPage.get_people_strong_block_morelink().click()
    WebDriverWait(browser, 10).until(EC.url_contains("tensor.ru/about"))
    assert "tensor.ru/about" in browser.current_url

def test_tensorGetWorkingBlock(browser):
    tensorAboutPage = TensorAboutPage(browser)
    tensorAboutPage.open()
    assert tensorAboutPage.get_working_block() != None

def test_tensorImageSizesInWorkingBlock(browser):

    tensorAboutPage = TensorAboutPage(browser)
    tensorAboutPage.open()
    images = tensorAboutPage.get_images_from_working_block()

    img0 = [images[0].size['height'], images[0].size['width']]
    result = True

    for i in images:
        if i.size['height'] != img0[0] or i.size['width'] != img0[1]:
            result = False

    assert result == True

