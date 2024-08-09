import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import APIRequestWrapper
from src.helpers.payload_manager import PayloadManager
from src.helpers.common_verification import verify_http_status_code
from src.utils.utils import Utils

@allure.title("Test POST request for create a new booking")
@pytest.mark.positive 
def test_create_booking_positive():
    url_for_booking = APIConstants().create_booking_base_url()
    headers = Utils().get_headers()
    payload = PayloadManager().get_payload()
    
    response = APIRequestWrapper().post_request(url=url_for_booking, headers=headers, payload=payload)
    
    verify_http_status_code(response=response,expected_data=200)