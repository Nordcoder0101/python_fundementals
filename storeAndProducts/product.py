class Products:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += (self.price * percent_change)
        else:
            self.price -= (self.price * percent_change)
    def print_info(self):
        print(f"Product is {self.name}, and the price is {self.price}")


# phone = Products('cellphone', 100, 'electronics')
# phone.print_info()