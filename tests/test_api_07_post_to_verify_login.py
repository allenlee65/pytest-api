import pytest
from utils.api_client import post
from config.config import VERIFY_LOGIN_ENDPOINT

"""
API 7: POST To Verify Login with valid details
API URL: https://automationexercise.com/api/verifyLogin
Request Method: POST
Request Parameters: email, password
Response Code: 200
"""

@pytest.mark.smoke
def test_post_to_verify_login():
    payload = {
        "email": "allenlee@punkproof.com",
        "password": "SKDeIutmdZqgNxJ"
    }
    response = post(VERIFY_LOGIN_ENDPOINT, json=payload)
    assert response.status_code == 200
    
