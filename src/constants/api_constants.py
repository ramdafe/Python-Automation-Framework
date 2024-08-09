# APIConstants - Contains all the constants, endpoint urls

class APIConstants:
    file_path = ""
    def __init__(self):
        self.file_path = r"C:\Users\ram.dafe\Python312\Selenium_With_Python\Python_Automation_Framework\Sample_Excel_File.xlsx"

    def create_booking_base_url(self):
        url = 'https://restful-booker.herokuapp.com/booking'
        print("The URL in constants file:", url)
        return url
    
    def url_create_token(self):
        url = 'https://restful-booker.herokuapp.com/auth'
        return url