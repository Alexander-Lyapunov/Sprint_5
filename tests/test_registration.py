from data.urls import Urls
from locators import Locators
from conftest import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
import helpers


class TestRegistration:
    def test_registration_successful(self, driver):
        driver.get(Urls.URL_REGISTER)
        driver.find_element(*Locators.INPUT_USER_NAME).send_keys(helpers.random_user_name())
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(helpers.random_email())
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(helpers.random_password())
        driver.find_element(*Locators.BUTTON_REG).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_LOGIN))
        assert driver.current_url == Urls.URL_LOGIN

    @pytest.mark.parametrize('password', ['A', 'Alexa'])
    def test_registration_negative_password_error(self, driver, password):
        driver.get(Urls.URL_REGISTER)
        driver.find_element(*Locators.INPUT_USER_NAME).send_keys(helpers.random_user_name())
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(helpers.random_email())
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON_REG).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.TEXT_PASSWORD_WRONG))
        assert driver.find_element(*Locators.TEXT_PASSWORD_WRONG).text == 'Некорректный пароль'

