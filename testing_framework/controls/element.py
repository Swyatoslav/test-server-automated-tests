import logging
from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from testing_framework.driver import Driver


class Element:
    """Common class of web elements"""

    _parent_web_elm = None

    def __str__(self):
        return f'"{self.eng_name}" element'

    def __init__(self, locator, eng_name):
        self.driver = Driver().get_driver()
        self.locator = locator
        self.how = By.XPATH if "/" in self.locator[:2] else By.CSS_SELECTOR
        self.eng_name = eng_name
        self.wait_time = 5
        self.wait = WebDriverWait(self.driver, self.wait_time)

    @property
    def webelement(self) -> WebElement:
        """Method return webelement"""
        if self.parent_web_elm:
            return self.wait.until(lambda x: self.parent_web_elm().find_element(self.how, self.locator))
        else:
            error_msg = f"There is no webelement {self.eng_name} on this page"
            try:
                return self.wait.until(ec.visibility_of_element_located(locator=(self.how, self.locator)))
            except TimeoutException as error:
                raise AssertionError(error_msg) from error

    @property
    def parent_web_elm(self):
        return self._parent_web_elm

    @parent_web_elm.setter
    def parent_web_elm(self, value: WebElement) -> None:
        self._parent_web_elm = value

    def should_be_displayed(self, msg=""):
        """Method to checking visibility
        :param msg: error message
        """

        error_msg = f"{str(self)} is not displayed" if not msg else msg

        try:
            self.wait.until(ec.visibility_of(self.webelement))
        except TimeoutException as error:
            logging.error(f"{str(self)} is still not displayed after {self.wait_time} sec")
            raise AssertionError(error_msg) from error
        logging.info(f"{str(self)} is displayed")

        return self

    def should_be_hidden(self, msg=""):
        """Check that element is not displayed"""

        error_msg = f"{str(self)} is displayed on page" if not msg else msg
        try:
            self.wait.until(ec.invisibility_of_element_located(locator=(self.how, self.locator)))
        except TimeoutException as error:
            logging.error(f"{str(self)} is still displayed after {self.wait_time} sec")
            raise AssertionError(error_msg) from error
        logging.info(f"{str(self)} is not displayed on page")

        return self

    def should_be_exact_text(self, text):
        """Method to checking text in element
        :param text: text to check
        """

        self.should_be_displayed()

        for _ in range(self.wait_time):
            if text != self.webelement.text:
                sleep(1)
            else:
                logging.info(f'{str(self)} has exact text "{text}"')
                return self
        raise AssertionError(
            f"{str(self)} has not exact text {text}"
            f"\n\nCurrent text: {self.webelement.text}\n\nExpected text: {text}"
        )

    def should_be_exact_value(self, value):
        """Method to checking attribute 'value' in element"""

        for _ in range(self.wait_time):
            if value != self.webelement.get_attribute("value"):
                sleep(1)
            else:
                logging.info(f'{str(self)} has exact value "{value}"')
                return self
        raise AssertionError(
            f"{str(self)} has not exact value {value}"
            f"\n\nCurrent value: {self.webelement.get_attribute('value')}"
            f"\n\nExpected value: {value}"
        )

    def subelement(self, locator: str, eng_name: str) -> "Element":
        """Searching child element in parent
        :param locator: locator of element
        :param eng_name: english name
        """
        child = Element(locator, eng_name)
        child.parent_web_elm = lambda: self.webelement
        return child

    def should_not_contains_text(self, text):
        """Method to checking text in element"""

        for _ in range(self.wait_time):
            if text in self.webelement.text:
                sleep(1)
            else:
                logging.info(f'{str(self)} does not contain text "{text}"')
                return self

        raise AssertionError(f'{str(self)} contains text "{text}"')
