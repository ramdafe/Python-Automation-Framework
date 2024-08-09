# GET, POST, PUT, PATCH Requests

import requests
from src.constants.api_constants import APIConstants

class APIRequestWrapper:
    def get_request(self, url, auth):
        booking_id = APIConstants().base_url()
        return requests.get(url + '/' + str(booking_id))
        
    def post_request(self, url, headers, payload):
        # POST Method
        # Positional Arguments are present in the Post method
        response_data_with_post = requests.post(url=url, headers=headers, json=payload)
        return response_data_with_post