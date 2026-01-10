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
