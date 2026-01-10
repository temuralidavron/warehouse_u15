# #
# # category title,id (oziq-ovqat,kiyim kechak)
# # product id,title,cat_id,price,quantity,ulchovi
# # warehouse title,id,cat_id
# # user username,id,balance
# # order id,user_id,product_id,amount
#
#
# class Category:
#     def __init__(self,id,title):
#         self.id=id
#         self.title=title
#         self.products=list()
#
#     def get_info(self):
#         return f"cat name {self.title} ----- cat id {self.id}"
#     def get_title(self):
#         return self.title
#
#     def add_product(self,product):
#         if isinstance(product,Product) and product.cat_id==self.id:
#             self.products.append(product)
#         else:
#             print("Xatolik yuz berdi ")
#
#     def get_products(self):
#         print(f"------------{self.title.upper()}----------")
#         data=[p.title for p in self.products]
#         print(data)
#         return len(data)
#
#         # print(data)
#         # for p in self.products:
#         #     print(p.title)
#
#
# cat=Category(1,'oziq-ovqat')
# cat2=Category(2,'kiyim')
# cat3=Category(3,'texnika')
# class Product:
#     def __init__(self,id,title,cat_id,price,quantity,ulchovi):
#         self.id=id
#         self.title=title
#         self.cat_id=cat_id
#         self.price=price
#         self.quantity=quantity
#         self.ulchovi=ulchovi
#
#
#     def get_info(self):
#         return f"""
#         ID={self.id} title:{self.title} narxi {self.price} miqdori {self.quantity} {self.ulchovi}
#
# """
#
# product=Product(1,'olma',1,2,15,'kg')
# product4=Product(4,'nok',1,7,30,'kg')
# product2=Product(2,'kurtka',2,30,8,'dona')
# product3=Product(3,'tv',3,300,15,'dona')
#
# cat.add_product(product)
# cat.add_product(product4)
# # print(cat.get_products())
# cat2.add_product(product2)
# # print(cat2.get_products())
#
#
# class Warehouse:
#     def __init__(self,id,title):
#         self.id=id
#         self.title=title
#         self.categories=list()
#         self.balance=None
#
#
#     def add_cat(self,cats):
#         for x in cats:
#             if isinstance(x,Category):
#                 self.categories.append(x)
#             else:
#                 print("Noqonuniy mahsulotni olmayamiz")
#
#
#     def get_cats(self):
#         cats=[c.get_products() for c in self.categories]
#         return cats
#
# #
# warehouse=Warehouse(1,"karzinka")
# # warehouse.add_cat(cat,cat3,cat2)
# # print(warehouse.get_cats())
#
# class User:
#     def __init__(self,id,username,balance):
#         self.id=id
#         self.username=username
#         self.balance=balance
#
#
#     def get_info(self):
#         return f"Kampaniya id:{self.id} Nomi {self.username} balance {self.balance}"
#
# #
# # user=User(1,"karzinka",5000)
# # print(user.get_info())
#
# class Order:
#     def __init__(self,id,user_id,product_id,amount):
#         self.id=id
#         self.user_id=user_id
#         self.product_id=product_id
#         self.amount=amount
#
#
#     def get_buy(self):
#         return f"""
#         User:{self.user_id}
#         Product:{self.product_id}
#         Miqdor:{self.amount}
# """
#
#     # def order_product(self):
#
# # sotuv=Order(1,1,1,5)
# # print(sotuv.get_buy())
#
# cats=[]
# users=[]
# def start():
#     parol='1234'
#     while True:
#         print("""
#         1 register
#         2 admin register
#         3 logout
#         """)
#         register=int(input("tanlang:"))
#
#         if register==3:
#             break
#         if register==2:
#             parol_user=input("parolni yoz")
#             if parol==parol_user:
#                 print("""
#                 1 add cat
#                 2 add product
#                 3 add cats warehouse
#                 4 exit
#                 """)
#                 admin_answer=int(input("tanlang"))
#                 if admin_answer==1:
#                     id = int(input("id yozing"))
#                     title = input(f"{id} idili categorya yarating:")
#                     cat = Category(id, title)
#                     cats.append(cat)
#                 if admin_answer == 2:
#                     for c in cats:
#                         print(c.get_info())
#                     id = int(input("id yozing"))
#                     title = input(f"{id} idili product yozing:")
#                     cat_id = int(input(f"{title} ni categoriysini yozing"))
#                     price = int(input(f"{title} narxi"))
#                     quantity = int(input(f"{title} miqdori:"))
#                     ulchovi = input("O'lchovi")
#                     product = Product(id, title, cat_id, price, quantity, ulchovi)
#                     if product:
#                         for c in cats:
#                             if c.id == product.cat_id:
#                                 c.add_product(product)
#
#                     print(product.get_info())
#                 if admin_answer==3:
#                     user=input("qoshilsini ha/no")
#                     if user.lower()=='ha':
#                         warehouse.add_cat(cats)
#
#
#         if register==1:
#             id=int(input("id yozing"))
#             username=input(f"{id} li kompaniya nomini yozing:")
#             balance=int(input(f"{username} balanci qancha"))
#             user_create=User(id,username,balance)
#             users.append(user_create)
#             while True:
#                 print("""
#                 1 view warehouse
#                 2 order product
#                 """)
#                 choice=int(input("tanlang:"))
#                 if choice==1:
#                     print(warehouse.get_cats())
#
#
# start()