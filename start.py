from cat import Category
from product import Product
from order import Order
from ware import Warehouse
from user import User

warehouse=Warehouse(1,"teen")
cats=[]
users=[]
def start():
    parol='1234'
    while True:
        print("""
        1 register
        2 admin register
        3 logout
        """)
        register=int(input("tanlang:"))

        if register==3:
            break
        if register==2:
            parol_user=input("parolni yoz")
            if parol==parol_user:
                print("""
                1 add cat
                2 add product
                3 add cats warehouse
                4 exit
                """)
                admin_answer=int(input("tanlang"))
                if admin_answer==1:
                    id = int(input("id yozing"))
                    title = input(f"{id} idili categorya yarating:")
                    cat = Category(id, title)
                    cats.append(cat)
                if admin_answer == 2:
                    for c in cats:
                        print(c.get_info())
                    id = int(input("id yozing"))
                    title = input(f"{id} idili product yozing:")
                    cat_id = int(input(f"{title} ni categoriysini yozing"))
                    price = int(input(f"{title} narxi"))
                    quantity = int(input(f"{title} miqdori:"))
                    ulchovi = input("O'lchovi")
                    product = Product(id, title, cat_id, price, quantity, ulchovi)
                    if product:
                        for c in cats:
                            if c.id == product.cat_id:
                                c.add_product(product)

                    print(product.get_info())
                if admin_answer==3:
                    user=input("qoshilsini ha/no")
                    if user.lower()=='ha':
                        warehouse.add_cat(cats)


        if register==1:
            id=int(input("id yozing"))
            username=input(f"{id} li kompaniya nomini yozing:")
            balance=int(input(f"{username} balanci qancha"))
            user_create=User(id,username,balance)
            users.append(user_create)
            while True:
                print("""
                1 view warehouse
                2 order product
                """)
                choice=int(input("tanlang:"))
                if choice==1:
                    print(warehouse.get_cats())
                elif choice==2:
                    print(warehouse.get_cats())
                    id=int(input("sotuv idsini yozing"))
                    user_id=int(input("oz idsini yozing"))
                    product_id=int(input("product_id idsini yozing"))
                    amount=int(input("qancha kerak yozing:"))
                    buy_user=None
                    for user in users:
                        if user_id==user.id:
                            buy_user=user
                        else:
                            print("Id xato user")
                    for cat in cats:
                        for c in cat:
                            for product in c.products:
                                if product_id==product:
                                    if product.quantity>amount:
                                        product.quantity=product.quantity-amount
                    order=Order(id,user_id,product_id,amount)
                    buy_user.add_order(order)
                    print("Mahsulotni sotib oldingiz")






start()