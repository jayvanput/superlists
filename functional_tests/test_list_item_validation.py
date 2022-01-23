from .base import FunctionalTest
from unittest import skip

import time
import sys


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Alice goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box.

        # The home page refreshses, and there is an erro rmessage saying
        # that the list items cannot be blank.

        # She tries again with some test for the item, which now works.

        # She now decides to submit a second blank list item.

        # She receives a similar warning on the list page.

        # And she can correct it by filling some text in.
        self.fail("Finish the test!")
