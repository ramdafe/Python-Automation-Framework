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