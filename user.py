class User:
    def __init__(self,id,username,balance):
        self.id=id
        self.username=username
        self.balance=balance


    def get_info(self):
        return f"Kampaniya id:{self.id} Nomi {self.username} balance {self.balance}"

#
# user=User(1,"karzinka",5000)
# print(user.get_info())
