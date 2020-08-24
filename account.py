import json


class Account():
    def __init__(self, username, password, email, gallery={}):
        self.username = username
        self.password = password
        self.email = email
        self.gallery = gallery

    @classmethod
    def from_json(cls, data):

        username, password, email, gallery = data["username"], data["password"], data["email"], data["gallery"]
        # print('this is data: ', data[])

        # for item in data["shopping_cart"]:
        #     tuple_item = tuple(item)
        #     shopping_cart.append(tuple_item)

        return cls(username=username, password=password, email=email, gallery=gallery)
