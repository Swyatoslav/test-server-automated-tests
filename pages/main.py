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
        self.bin_info_title_elm = Element('[id="bin_info_title"]', 'BIN info block title')
        self.bin_number_inp = TextField('[id="bin_number"]', "BIN number")
        self.submit_btn = Button('[name="Submit"]', 'Apply')
        self.info_tbl = Table('table', 'BIN info')

    def open_main_page(self, url: str):
        """Function opens main page by url"""

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
