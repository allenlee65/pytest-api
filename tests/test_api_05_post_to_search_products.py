import pytest
from utils.api_client import post
from config.config import SEARCH_PRODUCTS_ENDPOINT


"""
API 5: POST To Search Product
API URL: https://automationexercise.com/api/searchProduct
Request Method: POST
Request Parameter: search_product (For example: top, tshirt, jean)
Response Code: 200
"""

@pytest.mark.smoke
def test_post_to_search_product():
    payload = {"search_product": "Blue Top"}
    response = post(SEARCH_PRODUCTS_ENDPOINT, json=payload)
    assert response.status_code == 404
