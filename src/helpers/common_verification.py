# Common verifications

def verify_http_status_code(response, expected_data):
    print("The expected code:\n", expected_data)
    assert response.status_code == expected_data