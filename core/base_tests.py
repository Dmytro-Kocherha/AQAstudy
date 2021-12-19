from core.base_elements import BaseElement
from logger.logger import Logger


logger = Logger(logger="BaseTest").getlog()


class Asserts(BaseElement):

    def assert_current(self, link):
        assert link in self.current_url(), 'Incorrect url was opened.'
        logger.info("Right url opened test successfully complete.")
