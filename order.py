class Order:
    def __init__(self,id,user_id,product_id,amount):
        self.id=id
        self.user_id=user_id
        self.product_id=product_id
        self.amount=amount


    def get_buy(self):
        return f"""
        User:{self.user_id}
        Product:{self.product_id}
        Miqdor:{self.amount}
"""

