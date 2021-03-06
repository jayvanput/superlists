from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
import time


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Alice goes to the home page.
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered.
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertAlmostEqual(
            inputbox.location["x"] + inputbox.size["width"] / 2, 512,
            delta=10)

        # She starts a new list and sees the input is nicely centered there too.
        inputbox.send_keys("testing")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertAlmostEqual(
            inputbox.location["x"] + inputbox.size["width"] / 2, 512,
            delta=10)
