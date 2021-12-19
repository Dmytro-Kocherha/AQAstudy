from logger.logger import Logger
from core.base_tests import Asserts
from json_data_getter import JsonDataGetter

logger = Logger(logger="BaseTest").getlog()


class DemoQaAsserts(Asserts):

    def assert_current_url(self):
        self.assert_current(JsonDataGetter.url)
