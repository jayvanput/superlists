from pyclbr import Function
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip

import time
import sys


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls) -> None:
        for arg in sys.argv:
            if "liveserver" in arg:
                cls.server_url = "http://" + arg.split("=")[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass

    def setUp(self):
        self.browser = webdriver.Firefox(
            executable_path="C:\Program Files\Mozilla Firefox\geckodriver.exe")
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")

        self.assertIn(row_text, [row.text for row in rows])
