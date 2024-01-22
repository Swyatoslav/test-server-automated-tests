import json

import allure
import pytest
import requests


@allure.title('POST /get-info: Get existed BIN info')
@pytest.mark.smoke
def test_get_bin_info_validate_response():
    """Test checks response data fields of succeeded response"""

    expected_data_fields = ['bin', 'brand', 'type', 'category', 'issuer', 'alpha_2', 'alpha_3', 'country', 'latitude',
                            'longitude', 'bank_phone', 'bank_url']

    with allure.step("Send POST: /get-info with body {'bin_number': '417433'}"):
        response = requests.post(url='http://localhost:8000/get-info', json={'bin_number': '417433'})

        with allure.step('200 response code'):
            assert response.status_code == 200, 'Wrong response status code'

        with allure.step('Response contains "data" field'):
            response_content = response.json()
            assert response_content.get('data') is not None, 'Response object has no "data" field'

        with allure.step('Data has fields:'):
            response_data = response_content.get('data')
            for key in expected_data_fields:
                with allure.step(key):
                    assert key in response_data.keys(), f'There is no "{key}" field in response data'


@allure.title('POST /get-info: Send wrong type')
def test_get_bin_info_wrong_field_type():
    """Test checks service's behavior on wrong request body's field type"""

    error_message = 'BIN number should be string'

    with allure.step("Send POST: /get-info with body {'bin_number': 417433}"):
        response = requests.post(url='http://localhost:8000/get-info', json={'bin_number': 417433})
        with allure.step("400 response code"):
            assert response.status_code == 400, 'Wrong response status code'

        with allure.step("Response has 'details' field"):
            response_content = response.json()
            assert response_content.get('detail') is not None, 'Response object has no "detail" field'

        with allure.step(f"details = {error_message}"):
            assert response_content['detail'] == error_message, 'Wrong error message'


@allure.title('POST /get-info: Get unexisted BIN info')
def test_get_unknown_bin_info():
    """Test checks service's behavior on wrong request body's field type"""

    error_message = 'Unknown BIN'

    with allure.step("Send POST: /get-info with body {'bin_number': '123'}"):
        response = requests.post(url='http://localhost:8000/get-info', json={'bin_number': '123456'})
        with allure.step("404 response code"):
            assert response.status_code == 404, 'Wrong response status code'

        with allure.step("Response has 'details' field"):
            response_content = response.json()
            assert response_content.get('detail') is not None, 'Response object has no "detail" field'

        with allure.step(f"details = {error_message}"):
            assert response_content['detail'] == error_message, 'Wrong error message'
