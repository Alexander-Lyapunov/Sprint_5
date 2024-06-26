import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from data.urls import Urls


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get(Urls.URL)
    yield driver
    driver.quit()
