from testing_framework.controls.element import Element
import logging

class Button(Element):
    """
    Button web element
    """

    def __str__(self):
        return f'"{self.eng_name}" button'

    def click(self):
        """Action - click on web element"""

        self.should_be_displayed()
        self.webelement.click()
        logging.info(f"{str(self)} is clicked")