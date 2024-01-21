from testing_framework.controls.element import Element
from testing_framework.controls.button import Button
from testing_framework.controls.text_field import TextField
from testing_framework.controls.table import Table
from testing_framework.driver import Driver
import allure


class CommonPage:
    def __init__(self):
        self.page_title_elm = Element('[id="page_title"]', "Page title")
        self.input_error_elm = Element('[id="error"]', 'Input error')
        self.card_info_title_elm = Element('[id="card_info_title"]', 'Card info block title')
        self.card_number_inp = TextField('[id="card_number"]', "Card number")
        self.submit_btn = Button('[name="Submit"]', 'Apply')
        self.info_tbl = Table('table', 'Card info')

    def open_main_page(self, url):
        Driver().get_driver().get(url)
        self.page_title_elm.should_be_displayed()

    def check_no_errors(self):
        """Function checks that Erorrs element is hidden"""

        self.input_error_elm.should_be_hidden()
        self.info_tbl.should_not_contains_text('ERROR')

    def check_table_data(self, rows_dict: dict):
        """Function checks table's content"""

        for row_id, row_text in rows_dict.items():
            with allure.step(f'Row "{row_id}" displayed and contains text "{row_text}"'):
                self.info_tbl.row(row_id).should_be_exact_text(row_text)


    #
    # @allure.step("Login and check")
    # def check_successful_ldap_login(self, user_login):
    #     """Login with LDAP and check"""
    #
    #     self.keycloack_page.sign_in_ldap()
    #     self.logout_btn.should_be_displayed()
    #     self.logged_user_elm.should_contains_text(user_login)
    #
    # def switch_to_new_browser_tab(self):
    #     """Switching to new opened browser tab"""
    #
    #     test_case = TestCase()
    #
    #     delay(0.5, "Wait for new browser tab")
    #     last_opened_window = test_case.driver.window_handles[-1]
    #     test_case.driver.switch_to.window(last_opened_window)
    #     delay(0.5, "Wait for new browser tab")
    #     last_opened_window = TestCase().driver.window_handles[-1]
    #     TestCase().driver.switch_to.window(last_opened_window)
