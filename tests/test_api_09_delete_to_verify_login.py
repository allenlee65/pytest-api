import pytest
from utils.api_client import delete
from config.config import VERIFY_LOGIN_ENDPOINT

"""
API 9: DELETE To Verify Login
API URL: https://automationexercise.com/api/verifyLogin
Request Method: DELETE
Response Code: 405
Response Message: This request method is not supported.
"""

@pytest.mark.smoke
def test_delete_to_verify_login():
    response = delete(VERIFY_LOGIN_ENDPOINT)
    assert response.status_code == 200
