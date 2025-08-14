import pytest
from utils.api_client import post
from config.config import VERIFY_LOGIN_ENDPOINT

"""
API 10: POST To Verify Login with invalid details
API URL: https://automationexercise.com/api/verifyLogin
Request Method: POST
Request Parameters: email, password (invalid values)
Response Code: 404
Response Message: User not found!
"""

@pytest.mark.smoke
def test_post_to_verify_login_with_invalid_details():
    payload = {
        "email": "invalid@example.com",
        "password": "wrongpassword"
    }
    response = post(VERIFY_LOGIN_ENDPOINT, json=payload)
    assert response.status_code == 200
