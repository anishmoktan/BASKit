import json

class Account():
    def __init__(self, username, password, email, gallery=[]):
        self.username = username
        self.password = password
        self.email = email
        self.gallery=gallery 
    
    @classmethod
    def from_json(cls, data):
        username, password, email, gallery = data["username"], data["password"], data["email"], data["gallery"]
        return cls(username=username, password=password, email=email, gallery=gallery)
    
    def __str__(self):
        return f"this is username: {self.username}\nthis is password: {self.password}\nthis is email: {self.email}\nthis is gallery: {self.gallery}"
       
    


