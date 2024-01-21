import logging

from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains

from testing_framework.controls.element import Element


class TextField(Element):
    def __str__(self):
        return f'"{self.eng_name}" text field'

    def input_text(self, text, is_clear=True):
        """Entering text into text field
        :param text: text to enter
        :param is_clear: clear field before entering text
        """

        logging.info(f'Input text "{text}" into "{self.eng_name}"')

        self.should_be_displayed()

        if is_clear:
            self.webelement.clear()

        ActionChains(self.driver).send_keys_to_element(self.webelement, text).perform()

    def enter_click(self):
        """Perform ENTER click behavior"""

        self.webelement.click()
        ActionChains(self.driver).send_keys_to_element(self.webelement, Keys.ENTER).perform()
