import pytest
from utils.api_client import delete
from config.config import DELETE_ACCOUNT_ENDPOINT


"""
API 12: DELETE METHOD To Delete User Account
API URL: https://automationexercise.com/api/deleteAccount
Request Method: DELETE
Request Parameters: email, password
Response Code: 200
Response Message: Account deleted!
"""

@pytest.mark.smoke
def test_delete_account():
    payload = {
        "email": "john.doe@example.com",
        "password": "SecurePassword123"
    }

    response = delete(DELETE_ACCOUNT_ENDPOINT, json=payload)
    assert response.status_code == 200

