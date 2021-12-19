from selenium.webdriver.common.by import By
from core.base_elements import BaseElement
from selenium.common.exceptions import TimeoutException


class HomePageLocators:
    HOME_BANNER_LOGO = (By.XPATH, '//div[contains(@class, "home-banner")]//img[contains(@class, "banner-image")]')
    ALERTS_FRAME_BUTTON = (By.XPATH, '//div[contains(@class, "home-body")]//*[contains(text(), "Alert")]')


class HomePage(BaseElement):

    def click_alerts_frames_windows(self):
        self.move_to_element(HomePageLocators.ALERTS_FRAME_BUTTON)
        self.click(HomePageLocators.ALERTS_FRAME_BUTTON)


class AlertsFrameWindowsLocators:
    ALERTS_FRAMES_WINDOWS_BANNER = (By.XPATH, '//div[contains(@class, "playgound-header")]/div[contains(text(), '
                                              '"Alerts")]')
    ALERTS_FRAMES_WINDOWS_BUTTON = None
    ALERTS_BUTTON = None
    SEE_ALERT_BUTTON = None

class AlertsFrameWindowsPage:

    def see_alert_button(self):
        pass

    def accept_alert(self):
        pass
