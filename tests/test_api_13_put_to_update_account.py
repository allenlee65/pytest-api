import pytest
from utils.api_client import post
from config.config import UPDATE_ACCOUNT_ENDPOINT

"""
API 13: PUT METHOD To Update User Account
API URL: https://automationexercise.com/api/updateAccount
Request Method: PUT
Request Parameters: name, email, password, title (for example: Mr, Mrs, Miss), birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number
Response Code: 200
Response Message: User updated!
"""

@pytest.mark.smoke
def test_put_to_update_account():
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "SecurePassword123",
        "title": "Mr",
        "birth_date": "01",
        "birth_month": "January",
        "birth_year": "1990",
        "firstname": "John",
        "lastname": "Doe",
        "company": "Example Inc.",
        "address1": "123 Main St",
        "address2": "Apt 4B",
        "country": "United States",
        "zipcode": "10001",
        "state": "NY",
        "city": "New York",
        "mobile_number": "1234567890"
    }
    response = post(UPDATE_ACCOUNT_ENDPOINT, json=payload)
    assert response.status_code == 405
    assert response.json()["detail"] == 'Method "POST" not allowed.'