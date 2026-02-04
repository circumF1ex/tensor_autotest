import pytest
from pages.saby_main_page import SabyMainPage
from pages.saby_contacts_page import SabyContactsPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_about_page import TensorAboutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_sabyFooterContactsLink(browser):
    sabyMainPage = SabyMainPage(browser)
    sabyMainPage.open()
    sabyMainPage.click_footer_contacts_link()
    WebDriverWait(browser, 10).until(EC.url_contains("saby.ru/contacts"))
    assert "saby.ru/contacts" in browser.current_url

def test_sabyContactsGetRegionAndPartnersList(browser):
    sabyContactsPage = SabyContactsPage(browser)
    sabyContactsPage.open()
    region_name = sabyContactsPage.get_region_name()
    partners_exist = sabyContactsPage.get_partners()
    assert region_name is not None and partners_exist is True

def test_sabyContactsSetRegionKamchatskyKray(browser):
    sabyContactsPage = SabyContactsPage(browser)
    sabyContactsPage.open()
    sabyContactsPage.click_kamchatsky_kray_link()
    WebDriverWait(browser, 10).until(EC.url_contains("41-kamchatskij-kraj"))
    assert "https://saby.ru/contacts/41-kamchatskij-kraj?tab=clients" in browser.current_url
