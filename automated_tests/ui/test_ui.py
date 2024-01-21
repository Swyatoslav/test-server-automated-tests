import allure
import pytest


@pytest.mark.smoke
@allure.title('Common Page: Check main elements')
def test_check_main_elements(common_page):
    """Test checks visibility of main elements"""

    table_rows_dict = {'row_bin': 'BIN', 'row_brand': 'Brand', 'row_type': 'Type', 'row_category': 'Category',
                       'row_issuer': 'Issuer', 'row_alpha_2': 'Alpha 2', 'row_alpha_3': 'Alpha 3',
                       'row_country': 'Country', 'row_latitude': 'Latitude', 'row_longitude': 'Longitude',
                       'row_bank_phone': 'Bank phone', 'row_bank_url': 'Bank URL'}

    with allure.step("Check main page elements"):
        common_page.card_number_inp.should_be_displayed()
        common_page.submit_btn.should_be_displayed()
        common_page.info_tbl.should_be_displayed()
        common_page.check_no_errors()

    with allure.step("Check rows of Card Info table"):
        common_page.check_table_data(table_rows_dict)


@allure.title("Common Page: Search by existed card number: Full card info (Apply button)")
@pytest.mark.parametrize('card_number', ['417433', ' 417433', '417433 ', ' 417433 '],
                         ids=['No whitespaces', 'First whitespace', 'Last whitespace', 'Both whitesapces'])
def test_search_by_existed_card_number_full_info_using_apply_button(common_page, card_number):
    """Test checking search by existed card number (All card info fields are filled) using Apply button"""

    table_rows_dict = {'row_bin': 'BIN 417433', 'row_brand': 'Brand VISA', 'row_type': 'Type DEBIT',
                       'row_category': 'Category PREMIER', 'row_issuer': 'Issuer ASIACREDIT BANK JSC',
                       'row_alpha_2': 'Alpha 2 KZ', 'row_alpha_3': 'Alpha 3 KAZ', 'row_country': 'Country Kazakhstan',
                       'row_latitude': 'Latitude 48.0196', 'row_longitude': 'Longitude 66.9237',
                       'row_bank_phone': 'Bank phone 8 (727) 330-88-18', 'row_bank_url': 'Bank URL asiacreditbank.kz/'}

    with allure.step(f"Enter '{card_number}' card number and click 'Apply button'"):
        common_page.card_number_inp.input_text(card_number)
        common_page.submit_btn.click()
        common_page.info_tbl.should_not_contains_text('WAIT FOR RESPONSE')
        common_page.check_no_errors()

    with allure.step("Table contains correct data"):
        common_page.check_table_data(table_rows_dict)


@allure.title("Common Page: Search by existed card number: Partial card info (ENTER button)")
def test_search_by_existed_card_number_partial_info_using_enter_button(common_page):
    """Test checking search by existed card number (Card info fields are partially filled) using ENTER button"""

    card_number = '417130'
    table_rows_dict = {'row_bin': 'BIN 417130', 'row_brand': 'Brand VISA', 'row_type': 'Type NOT FOUND',
                       'row_category': 'Category NOT FOUND', 'row_issuer': 'Issuer NOT FOUND',
                       'row_alpha_2': 'Alpha 2 US', 'row_alpha_3': 'Alpha 3 USA',
                       'row_country': 'Country United States',
                       'row_latitude': 'Latitude 37.0902', 'row_longitude': 'Longitude -95.7129',
                       'row_bank_phone': 'Bank phone NOT FOUND', 'row_bank_url': 'Bank URL NOT FOUND'}

    with allure.step(f"Enter '{card_number}' card number and click 'ENTER' keyboard button"):
        common_page.card_number_inp.input_text(card_number)
        common_page.card_number_inp.enter_click()
        common_page.info_tbl.should_not_contains_text('WAIT FOR RESPONSE')
        common_page.check_no_errors()

    with allure.step("Table contains correct data"):
        common_page.check_table_data(table_rows_dict)


@allure.title("Common Page: Multi-search")
def test_search_two_different_existed_cards(common_page):
    """Test checking multi search and check data changing"""

    card_number1 = '417433'
    table_rows_dict1 = {'row_bin': 'BIN 417433', 'row_brand': 'Brand VISA', 'row_type': 'Type DEBIT',
                       'row_category': 'Category PREMIER', 'row_issuer': 'Issuer ASIACREDIT BANK JSC',
                       'row_alpha_2': 'Alpha 2 KZ', 'row_alpha_3': 'Alpha 3 KAZ', 'row_country': 'Country Kazakhstan',
                       'row_latitude': 'Latitude 48.0196', 'row_longitude': 'Longitude 66.9237',
                       'row_bank_phone': 'Bank phone 8 (727) 330-88-18', 'row_bank_url': 'Bank URL asiacreditbank.kz/'}

    card_number2 = '417130'
    table_rows_dict2 = {'row_bin': 'BIN 417130', 'row_brand': 'Brand VISA', 'row_type': 'Type NOT FOUND',
                       'row_category': 'Category NOT FOUND', 'row_issuer': 'Issuer NOT FOUND',
                       'row_alpha_2': 'Alpha 2 US', 'row_alpha_3': 'Alpha 3 USA',
                       'row_country': 'Country United States',
                       'row_latitude': 'Latitude 37.0902', 'row_longitude': 'Longitude -95.7129',
                       'row_bank_phone': 'Bank phone NOT FOUND', 'row_bank_url': 'Bank URL NOT FOUND'}

    with allure.step(f"Enter '{card_number1}' card number and click 'Apply button'"):
        common_page.card_number_inp.input_text(card_number1)
        common_page.submit_btn.click()
        common_page.info_tbl.should_not_contains_text('WAIT FOR RESPONSE')
        common_page.check_no_errors()

    with allure.step("Table contains correct data"):
        common_page.check_table_data(table_rows_dict1)

    with allure.step(f"Enter '{card_number2}' card number and click 'Apply button'"):
        common_page.card_number_inp.input_text(card_number2)
        common_page.submit_btn.click()
        common_page.info_tbl.should_not_contains_text('WAIT FOR RESPONSE')
        common_page.check_no_errors()

    with allure.step("Table contains correct data"):
        common_page.check_table_data(table_rows_dict2)


@allure.title("Common Page: Search by unexisted card number")
def test_search_by_unexisted_card_number(common_page):
    """Test checking search by unexisted card number"""

    card_number = '00000000'
    table_rows_dict = {'row_bin': 'BIN ERROR', 'row_brand': 'Brand ERROR', 'row_type': 'Type ERROR',
                       'row_category': 'Category ERROR', 'row_issuer': 'Issuer ERROR',
                       'row_alpha_2': 'Alpha 2 ERROR', 'row_alpha_3': 'Alpha 3 ERROR', 'row_country': 'Country ERROR',
                       'row_latitude': 'Latitude ERROR', 'row_longitude': 'Longitude ERROR',
                       'row_bank_phone': 'Bank phone ERROR', 'row_bank_url': 'Bank URL ERROR'}

    with allure.step(f"Enter '{card_number}' card number and click 'ENTER' keyboard button"):
        common_page.card_number_inp.input_text(card_number)
        common_page.card_number_inp.enter_click()
        common_page.info_tbl.should_not_contains_text('WAIT FOR RESPONSE')

    with allure.step("Table contains errors"):
        common_page.check_table_data(table_rows_dict)

    with allure.step("Displayed validation error"):
        common_page.input_error_elm.should_be_displayed()
        common_page.input_error_elm.should_be_exact_text('Unknown card')


@pytest.mark.parametrize('card_number, error_text',
                         [
                             ('qwerty123', 'Card number should contain only digits'),
                             (' ', 'Card number should contain only digits'),
                             ('', 'Card number can\'t be empty')
                         ],
                         ids=['Contains letters', 'Only whitespace', 'Empty text'])
@allure.title("Common Page: Search by invalid card number")
def test_search_by_invalid_card_number(common_page, card_number, error_text):
    """Test checking search by invalid card number"""

    table_rows_dict = {'row_bin': 'BIN ERROR', 'row_brand': 'Brand ERROR', 'row_type': 'Type ERROR',
                       'row_category': 'Category ERROR', 'row_issuer': 'Issuer ERROR',
                       'row_alpha_2': 'Alpha 2 ERROR', 'row_alpha_3': 'Alpha 3 ERROR', 'row_country': 'Country ERROR',
                       'row_latitude': 'Latitude ERROR', 'row_longitude': 'Longitude ERROR',
                       'row_bank_phone': 'Bank phone ERROR', 'row_bank_url': 'Bank URL ERROR'}

    with allure.step(f"Enter '{card_number}' card number and click 'ENTER' keyboard button"):
        common_page.card_number_inp.input_text(card_number)
        common_page.card_number_inp.enter_click()
        common_page.info_tbl.should_not_contains_text('WAIT FOR RESPONSE')

    with allure.step("Table contains errors"):
        common_page.check_table_data(table_rows_dict)

    with allure.step(f"Displayed validation error: {error_text}"):
        common_page.input_error_elm.should_be_displayed()
        common_page.input_error_elm.should_be_exact_text(error_text)


@allure.title("Common Page: Check max search length field")
def test_check_max_search_length(common_page):
    """Test checking search by unexisted card number"""

    card_number_full = '123456789123456789'
    card_number_expected = '1234567891234567'


    with allure.step(f"Enter '{card_number_full}' card number"):
        common_page.card_number_inp.input_text(card_number_full)

        with allure.step(f"Displayed '{card_number_expected}' number in text field"):
            common_page.card_number_inp.should_be_exact_value(card_number_expected)