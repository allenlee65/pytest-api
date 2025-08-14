import pytest
from utils.api_client import get
from config.config import BRANDS_ENDPOINT

"""
API 3: Get All Brands List
API URL: https://automationexercise.com/api/brandsList
Request Method: GET
Response Code: 200
Response JSON: All brands list
"""

@pytest.mark.smoke
def test_get_all_brands_list_status_code():
    response = get(BRANDS_ENDPOINT)
    assert response.status_code == 200, "Expected status code 200 for GET request to brands list"
    assert "brands" in response.json(), "Expected 'brands' key in response JSON"
    assert isinstance(response.json()["brands"], list), "Expected 'brands' key to be a list"

def test_get_all_brands_list_schema():
    response = get(BRANDS_ENDPOINT)
    schema = {
        "type": "object",
        "properties": {
            "brands": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"}
                    },
                    "required": ["id", "name"]
                }
            }
        },
        "required": ["brands"]
    }

