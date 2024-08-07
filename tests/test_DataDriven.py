import pytest
import openpyxl

def read_credentials_from_excel(file_path):
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

@pytest.mark.smoke
def test_create_auth_with_excel():
    file_path = r"C:\Users\ram.dafe\Python312\Selenium_With_Python\Python_Automatio_Framework\.venv\Sample_Excel_File.xlsx"
    credentials = read_credentials_from_excel(file_path = file_path)
    print("Type of credentials:", type(credentials))
    print(credentials)
    
def create_auth_request(username, password):
    payload = {
        "username": username,
        "password": password
    }
    return payload