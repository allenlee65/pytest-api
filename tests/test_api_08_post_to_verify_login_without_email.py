import pytest
from config.config import VERIFY_LOGIN_ENDPOINT
from utils.api_client import post

"""
API 8: POST To Verify Login without email parameter
API URL: https://automationexercise.com/api/verifyLogin
Request Method: POST
Request Parameter: password
Response Code: 400
"""

@pytest.mark.smoke
def test_post_to_verify_login_without_email():
    payload = {
        "password": "SKDeIutmdZqgNxJ"
    }
    response = post(VERIFY_LOGIN_ENDPOINT, json=payload)
    assert response.status_code == 200