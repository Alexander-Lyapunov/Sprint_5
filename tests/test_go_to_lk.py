from data.data import Data
from data.urls import Urls
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLK:
    def test_go_to_account_from_main(self, driver):
        driver.get(Urls.URL)
        driver.find_element(*Locators.BUTTON_LK).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGO))
        driver.find_element(*Locators.BUTTON_LK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_LINK))
        assert driver.find_element(*Locators.PROFILE_LINK)