import pytest
from utils.api_client import post
from config.config import SEARCH_PRODUCTS_ENDPOINT

"""
API 6: POST To Search Product without search_product parameter
API URL: https://automationexercise.com/api/searchProduct
Request Method: POST
Response Code: 400
Response Message: Bad request, search_product parameter is missing in POST request.
"""

@pytest.mark.smoke
def test_post_to_search_product_without_parameter():
    response = post(SEARCH_PRODUCTS_ENDPOINT)
    assert response.status_code == 404

