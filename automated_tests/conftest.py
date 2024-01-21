import allure
import pytest

from pages.main import CommonPage
from testing_framework.driver import Driver


@pytest.fixture
def common_page():
    with allure.step("Open main page"):
        Driver().get_driver().get('http://localhost:8000/')
        page = CommonPage()
        page.page_title_elm.should_be_displayed()

    return page
