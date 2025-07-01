from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.CSS_SELECTOR, "[data-test='lp-resultsCount']")
    SELECT_PRODUCT = (By.CSS_SELECTOR, "[alt*='Tazo Organic']")
    AD_BANNER = (By.CSS_SELECTOR, ".heroImg")

    def verify_search_results(self):
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TXT).text
        assert 'tea' in actual_text, f"Error, expected 'tea' not in {actual_text}"

    def select_product(self):
        self.wait_for_element_disappear(*self.AD_BANNER)
        self.click(*self.SELECT_PRODUCT)