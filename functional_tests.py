from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox(
            executable_path="C:\Program Files\Mozilla Firefox\geckodriver.exe")
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Alice has heard of a new app and goes to check it out.
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

        # She is invited to enter a to-do item

        # She enters "Write user story" into a text box (she is a web developer)

        # When she hits enter, the page updates and now lists "1: Build website"

        # A text box is still on the screen so she can enter another item. She enters "Launch website"

        # The page updates again and now shows both of the items.

        # She wonders if the website will save the list and notices a unique URL for her.

        # She visits the URL and her to-do list is still there.

        # She closes out the site.


if __name__ == "__main__":
    unittest.main(warnings="ignore")
