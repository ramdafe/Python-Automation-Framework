class PayloadManager:
    def get_payload(self):
        payload = {
            "firstname" : "Brianna",
            "lastname" : "Washington",
            "totalprice" : 111,
            "depositpaid" : True,
            "bookingdates" : {
                "checkin" : "2018-01-01",
                "checkout" : "2019-01-01"
            },
            "additionalneeds" : "Breakfast"
        }   
        return payload
    
    def get_token_payload(self):
        json_paylod = {
            "username" : "admin",
            "password" : "password123"
        }
        return json_paylod