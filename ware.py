from cat import Category


class Warehouse:
    def __init__(self,id,title):
        self.id=id
        self.title=title
        self.categories=list()
        self.balance=None


    def add_cat(self,cats):
        for x in cats:
            if isinstance(x,Category):
                self.categories.append(x)
            else:
                print("Noqonuniy mahsulotni olmayamiz")


    def get_cats(self):
        cats=[c.get_products() for c in self.categories]
        return cats

#
# warehouse=Warehouse(1,"karzinka")
# warehouse.add_cat(cat,cat3,cat2)
# print(warehouse.get_cats())

# Admin
# eng ko'p mahsulot for warehouse cats=[1,2,3,3,4]
# eng kam mahsulot
# eng qimmat mahuslot
# eng arzon mahsulot qaysi
# eng ko'p sotilgan mahsulot
# eng kam sotilgan mahsulot
# barcha categorylarda  cat_name mahsulotlar soni
# jami mahsulotlar soni
# warehousedagi jami total
# tovarga bonus qollash
# katta narxli savdo qilivchi customer sort

# Customer User
# sotib_olganalarim

#
# sonlar=[23,3,4,5,6,67,8]
# print(sorted(sonlar,reverse=True))