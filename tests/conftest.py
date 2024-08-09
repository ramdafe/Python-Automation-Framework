import pytest
import requests
import openpyxl
from src.constants.api_constants import APIConstants
from src.utils.utils import Utils

@pytest.fixture(scope="session")
def create_token(username, password):
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(
        url=APIConstants().url_create_token(), 
        headers=Utils().get_headers(), 
        json=payload,
        auth=None
    )
    return response