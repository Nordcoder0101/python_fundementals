import product


class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product, price, category):
        self.products.append(product.Products(new_product, price, category))
    def sell_product(self, name_of_product_to_sell):
        for i in range(0, len(self.products)):
            if self.products[i].name == name_of_product_to_sell:
                self.products.pop(i)
                break    


gregs = Store('Greg')

gregs.add_product('cellphone', 100, 'electronics')
gregs.add_product('ball', 50, 'electronics')
gregs.add_product('rubber band', .01, 'electronics')
gregs.add_product('bottle', 10, 'electronics')
for i in range(0, len(gregs.products)):
    print(gregs.products[i].name)
gregs.sell_product('ball')

for i in range(0,len(gregs.products)):
    print(gregs.products[i].name)
