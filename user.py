from order import Order


class User:
    def __init__(self,id,username,balance):
        self.id=id
        self.username=username
        self.balance=balance
        self.orders=list()


    def get_info(self):
        return f"Kampaniya id:{self.id} Nomi {self.username} balance {self.balance}"

    def add_order(self,order):
        if isinstance(order,Order):
            self.orders.append(order)


    def get_order(self):
        orders=[o.get_buy() for o in self.orders]
        return orders


# user=User(1,"karzinka",5000)
# print(user.get_info())
