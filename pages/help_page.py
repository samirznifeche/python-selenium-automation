from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pages.base_page import Page


class HelpPage(Page):
    HEADER = (By.XPATH, "//h1[text()=' {SUBSTR}']")
    SELECT_DD = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    def _get_header_locator(self, expected_text):
        return [self.HEADER[0], self.HEADER[1].replace('{SUBSTR}', expected_text)]

    def open_help_returns_page(self):
        self.driver.get("https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges")

    def select_help_circle_topic(self, value):
        dd = self.find_element(*self.SELECT_DD)
        select = Select(dd)
        select.select_by_value(value)

    def verify_help_topic_page_opened(self, expected_text):
        locator = self._get_header_locator(expected_text)
        self.wait_for_element(*locator)