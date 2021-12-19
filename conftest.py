import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from json_data_getter import JsonDataGetter


@pytest.fixture(scope='session')
def browser():
    driver: WebDriver = get_web_driver()
    driver.get(JsonDataGetter.url)
    yield driver
    driver.quit()


def get_web_driver():
    if JsonDataGetter.browser_name == 'firefox':
        s = Service(executable_path=GeckoDriverManager().install())
        return webdriver.Firefox(service=s)
    elif JsonDataGetter.browser_name == 'chrome':
        s = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=s)

    raise Exception("No such " + JsonDataGetter.browser_name + " browser exists")
