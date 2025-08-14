import pytest
from utils.api_client import put
from config.config import BRANDS_ENDPOINT

"""
API 4: PUT To All Brands List
API URL: https://automationexercise.com/api/brandsList
Request Method: PUT
Response Code: 405
Response Message: This request method is not supported.
"""

@pytest.mark.smoke
def test_put_to_all_brands_list_status_code():
    response = put(BRANDS_ENDPOINT)
    assert response.status_code == 200