import pytest
from utils.api_client import get
from utils.schema_validator import validate_schema
from config.config import PRODUCTS_ENDPOINT

PRODUCT_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "responseCode": {"type": "integer"},
        "products": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "price": {"type": "string"},
                    "brand": {"type": "string"},
                    "category": {
                        "type": "object",
                        "properties": {
                            "usertype": {
                                "type": "object",
                                "properties": {
                                    "usertype": {"type": "string"}
                                },
                                "required": ["usertype"]
                            },
                            "category": {"type": "string"}
                        },
                        "required": ["usertype", "category"]
                    }
                },
                "required": ["id", "name", "price", "brand", "category"]
            }
        }
    },
    "required": ["responseCode", "products"]
}

@pytest.mark.smoke
def test_get_products_list_status_code():
    response = get(PRODUCTS_ENDPOINT)
    assert response.status_code == 200

@pytest.mark.smoke
def test_get_products_list_schema():
    response = get(PRODUCTS_ENDPOINT)
    json_data = response.json()
    validate_schema(json_data, PRODUCT_LIST_SCHEMA)

@pytest.mark.regression
def test_response_code_in_body():
    response = get(PRODUCTS_ENDPOINT)
    json_data = response.json()
    assert json_data["responseCode"] == 200

@pytest.mark.regression
def test_products_not_empty():
    response = get(PRODUCTS_ENDPOINT)
    json_data = response.json()
    assert len(json_data["products"]) > 0

@pytest.mark.regression
def test_all_products_have_required_fields():
    response = get(PRODUCTS_ENDPOINT)
    products = response.json()["products"]
    for product in products:
        assert product["id"] > 0
        assert product["name"].strip() != ""
        assert "Rs." in product["price"]
        assert product["brand"].strip() != ""
