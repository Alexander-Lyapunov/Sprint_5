from data.data import Data
from data.urls import Urls
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver

class TestGoToConstructorFromLK:
    def test_go_to_constructor_from_lk_constructor_button(self, driver):
        driver.get(Urls.URL_LOGIN)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGO))
        driver.find_element(*Locators.BUTTON_LK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_LINK))
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGO))
        assert driver.current_url == Urls.URL

    def test_go_to_constructor_from_lk_logo(self, driver):
        driver.get(Urls.URL_LOGIN)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGO))
        driver.find_element(*Locators.BUTTON_LK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_LINK))
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGO))
        assert driver.current_url == Urls.URL
