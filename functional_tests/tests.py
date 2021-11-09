from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


class NewVisitorTest(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox(
            executable_path="C:\Program Files\Mozilla Firefox\geckodriver.exe")
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")

        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Alice has heard of a new app and goes to check it out.
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter a to-do item"
        )

        # She enters "Write user story" into a text box (she is a web developer)
        inputbox.send_keys("Write user story")

        # When she hits enter, the page updates and now lists "1: Build website"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table("1: Write user story")

        # A text box is still on the screen so she can enter another item. She enters "Launch website"
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Launch website")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again and now shows both of the items.
        self.check_for_row_in_list_table("1: Write user story")
        self.check_for_row_in_list_table("2: Launch website")

        # She wonders if the website will save the list and notices a unique URL for her.
        self.fail("Finish the test!")
        # She visits the URL and her to-do list is still there.

        # She closes out the site.
