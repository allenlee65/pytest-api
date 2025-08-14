import pytest
from config.config import PRODUCTS_ENDPOINT
from utils.api_client import post

"""
API 2: POST To All Products List
API URL: https://automationexercise.com/api/productsList
Request Method: POST
Response Code: 405
Response Message: This request method is not supported.
"""

@pytest.mark.smoke
def test_get_products_list_status_code():
    response = post(PRODUCTS_ENDPOINT)
    assert response.status_code == 200