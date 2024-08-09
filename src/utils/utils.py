import openpyxl
import requests
from src.constants.api_constants import APIConstants

class Utils:
    def get_headers(self):
        headers = {
            "Content-Type" : "application/json"
            }
        return headers
    
    def create_auth_request(self, username, password):
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
    
    def read_credentials_from_excel(self, file_path):
        credentials = []
        workbook = openpyxl.load_workbook(filename = file_path)
        sheet = workbook.active
        
        for rows in sheet.iter_rows(min_row=2, values_only=True):
            username,password = rows
            credentials.append(
                {
                    "username" : username,
                    "password" : password
                } 
            )
        return credentials