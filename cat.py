from product import Product


class Category:
    def __init__(self,id,title):
        self.id=id
        self.title=title
        self.products=list()

    def get_info(self):
        return f"cat name {self.title} ----- cat id {self.id}"
    def get_title(self):
        return self.title

    def add_product(self,product):
        if isinstance(product,Product) and product.cat_id==self.id:
            self.products.append(product)
        else:
            print("Xatolik yuz berdi ")

    def get_products(self):
        print(f"------------{self.title.upper()}----------")
        data=[p.title for p in self.products]
        print(data)
        return len(data)

        # print(data)
        # for p in self.products:
        #     print(p.title)

#
# cat=Category(1,'oziq-ovqat')
# cat2=Category(2,'kiyim')
# cat3=Category(3,'texnika')

name='ali'