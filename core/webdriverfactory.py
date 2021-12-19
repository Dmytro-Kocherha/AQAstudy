from selenium import webdriver
from json_data_getter import JsonDataGetter


class WebDriverFactory:

    def __init__(self, browser):
        self.browser = JsonDataGetter.browser_name

    def get_web_driver_instance(self):
        base_url = JsonDataGetter.url
        if self.browser == "chrome":
            driver = webdriver.Chrome("chromedriver.exe")
        elif self.browser == "firefox":
            driver = webdriver.Firefox()

        else:
            driver = webdriver.Chrome("chromedriver.exe")
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(base_url)
        return driver
