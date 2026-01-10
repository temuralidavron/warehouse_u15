# Omborxona
# category title
# product cats,title,price,quantity
#auth username,parol
#order product,amount,,total_price
# warehouse products \
class Product:
    def __init__(self,id,title,price,quantity,parametr,cat_id):
        self.id=id
        self.title=title
        self.price=price
        self.quantity=quantity
        self.parametr=parametr
        self.cat_id=cat_id


product=Product(1,'olma',20000,4,'kg',1)
# product2=Product(2,'oliviye',2)
# product32=Product(3,'safia shakalali tort',4)
# product3=Product(3,'cola',3)
# product4=Product(3,'fanta',3)
class Category:
    def __init__(self,id,title):
        self.id=id
        self.title=title
        self.products=list()

    def add_product(self,product):
        if isinstance(product,Product):
            if product.cat_id==self.id:
                self.products.append(product)
            else:
                print(f"{self.title} categoryiasiga taluqli emas")
        else:
            print("Faqat mahsulotlarni omborga joylash mumkin")

    def get_info(self):
        print(f"-------  {self.title.upper()} -----")
        # data=[p.title for p in self.products]
        # print(data)
        for m in self.products:
            print(f"{m.title}")

    def get_title(self):
        return self.title

cat=Category(1,'mevalar')
cat2=Category(2,'salatlar')
cat3=Category(3,'ichimliklar')
cat4=Category(4,'shirinliklar')
cat3.add_product(product3)
cat3.add_product(product2)
cat3.add_product(product4)
print(cat3.get_info())

