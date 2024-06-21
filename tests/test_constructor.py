from locators import Locators
from data.urls import Urls
from conftest import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructor:
    def test_go_to_sauce(self, driver):
        driver.get(Urls.URL)
        driver.find_element(*Locators.SPAN_SAUCES).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.TITLE_SAUCE))
        assert "current" in driver.find_element(*Locators.SPAN_SAUCES).get_attribute("class")

    def test_go_to_filling(self, driver):
        driver.get(Urls.URL)
        driver.find_element(*Locators.SPAN_FILLING).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.TITLE_FILLING))
        assert "current" in driver.find_element(*Locators.SPAN_FILLING).get_attribute("class")

    def test_go_to_bun(self, driver):
        driver.get(Urls.URL)
        driver.find_element(*Locators.SPAN_FILLING).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.TITLE_FILLING))
        driver.find_element(*Locators.SPAN_BUNS).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.TITLE_BUNS))
        assert "current" in driver.find_element(*Locators.SPAN_BUNS).get_attribute("class")