from data.data import Data
from data.urls import Urls
from locators import Locators
from conftest import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.get(Urls.URL)
        driver.find_element(*Locators.BUTTON_ENTER_LK).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER))
        assert driver.current_url == Urls.URL

    def test_login_from_profile_page(self, driver):
        driver.get(Urls.URL)
        driver.find_element(*Locators.BUTTON_LK).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER))
        assert driver.current_url == Urls.URL

    def test_login_registration_form_sign_in_button(self, driver):
        driver.get(Urls.URL_REGISTER)
        driver.find_element(*Locators.LINK_LOGIN_PASS_RECOVERY).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_LOGIN))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER))
        assert driver.current_url == Urls.URL

    def test_login_from_recovery_pass_page(self, driver):
        driver.get(Urls.URL_LOGIN)
        driver.find_element(*Locators.LINK_PASS_RECOVERY).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_PASS_RECOVERY))
        driver.find_element(*Locators.LINK_LOGIN_PASS_RECOVERY).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_LOGIN))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER))
        assert driver.current_url == Urls.URL
