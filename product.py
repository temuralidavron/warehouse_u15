class Product:
    def __init__(self,id,title,cat_id,price,quantity,ulchovi):
        self.id=id
        self.title=title
        self.cat_id=cat_id
        self.price=price
        self.quantity=quantity
        self.ulchovi=ulchovi


    def get_info(self):
        return f"""
        ID={self.id} title:{self.title} narxi {self.price} miqdori {self.quantity} {self.ulchovi}

"""
#
# product=Product(1,'olma',1,2,15,'kg')
# product4=Product(4,'nok',1,7,30,'kg')
# product2=Product(2,'kurtka',2,30,8,'dona')
# product3=Product(3,'tv',3,300,15,'dona')
