import json

import allure
import pytest
import requests


@allure.title('Get Info API: Get existed card info')
@pytest.mark.smoke
def test_get_card_info_validate_response():
    """Test checks response data fields of succeeded response"""

    expected_data_fields = ['bin', 'brand', 'type', 'category', 'issuer', 'alpha_2', 'alpha_3', 'country', 'latitude',
                            'longitude', 'bank_phone', 'bank_url']

    with allure.step("Send POST: /get-info with body {'card_number': '417433'}"):
        response = requests.post(url='http://localhost:8000/get-info', json={'card_number': '417433'})

        with allure.step('200 response code'):
            assert response.status_code == 200, 'Wrong response status code'

        with allure.step('Response contains "data" field'):
            response_content = response.json()
            assert response_content.get('data') is not None, 'Response object has no "data" field'

        with allure.step('Data has fields:'):
            response_data = json.loads(response_content.get('data'))
            for key in expected_data_fields:
                with allure.step(key):
                    assert key in response_data.keys(), f'There is no "{key}" field in response data'


@allure.title('Get Info API: Send wrong type')
def test_get_card_info_wrong_field_type():
    """Test checks service's behavior on wrong request body's field type"""

    error_message = 'Card number should be string'

    with allure.step("Send POST: /get-info with body {'card_number': 417433}"):
        response = requests.post(url='http://localhost:8000/get-info', json={'card_number': 417433})
        with allure.step("400 response code"):
            assert response.status_code == 400, 'Wrong response status code'

        with allure.step("Response has 'details' field"):
            response_content = response.json()
            assert response_content.get('detail') is not None, 'Response object has no "detail" field'

        with allure.step(f"details = {error_message}"):
            assert response_content['detail'] == error_message, 'Wrong error message'


@allure.title('Get Info API: Send unknown card')
def test_get_unknown_card_info():
    """Test checks service's behavior on wrong request body's field type"""

    error_message = 'Unknown card'

    with allure.step("Send POST: /get-info with body {'card_number': '123'}"):
        response = requests.post(url='http://localhost:8000/get-info', json={'card_number': '123'})
        with allure.step("404 response code"):
            assert response.status_code == 404, 'Wrong response status code'

        with allure.step("Response has 'details' field"):
            response_content = response.json()
            assert response_content.get('detail') is not None, 'Response object has no "detail" field'

        with allure.step(f"details = {error_message}"):
            assert response_content['detail'] == error_message, 'Wrong error message'
