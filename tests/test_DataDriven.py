import pytest
import requests
import openpyxl
from src.constants.api_constants import APIConstants
from src.utils.utils import Utils

#-------Without using pytest.mark.parameterize()----------
# @pytest.mark.smoke
# def test_create_auth_with_excel():
#     file_path = APIConstants().file_path
#     credentials = Utils().read_credentials_from_excel(file_path = file_path)
    
    # for user_cred in credentials:
    #     username = user_cred["username"]
    #     password = user_cred["password"]
    #     response = create_auth_request(username=username, password=password)
    #     print(response.text, response.status_code, sep="\n")
    #     assert response.status_code == 200
    
# Test Method with an example of parameterize()
@pytest.mark.parametrize(
    "user_cred", 
    Utils().read_credentials_from_excel(
        file_path = APIConstants().file_path
        )
    )
def test_create_auth_with_excel_2(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    response = Utils().create_auth_request(username=username, password=password)
    print("Response:", response.json())
    assert response.status_code == 200