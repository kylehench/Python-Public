class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)
    def sell_product(self, id):
        print(f"{self.products[id]} was sold. These products remain: ")
        sold = self.products.pop(id)
        print(self.products)
    def inflation(self, percent_increase):
        for item in self.products:
            item.update_price(percent_increase, is_increased=True)
    def set_clearance(self, category, percent_discount):
        for item in self.products:
            if item.category==category:
                item.update_price(percent_discount, is_increased=False)

class Products:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def __repr__(self):
        return f"Name: {self.name}"
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            prevPrice = self.price
            self.price += self.price*percent_change/100
            print(f"The previous price is ${prevPrice}. The new price is ${self.price}.")
        else:
            prevPrice = self.price
            self.price -= self.price*percent_change/100
            print(f"The previous price is ${prevPrice}. The new price is ${self.price}.")
    def print_info(self):
        print(f"Name of product: {self.name}\nCategory: {self.category}\nPrice: {self.price}")

store = Store('Ralphs')
new_products = [Products('milk', 5, 'dairy'), Products('eggs', 3, 'dairy'), Products('cage free eggs', 12, 'dairy'), Products('bacon', 7, 'meat')] 
for product in new_products:
    store.add_product(product)
store.products[0].update_price(5,is_increased=True)
store.sell_product(1)
store.inflation(50)
store.set_clearance('dairy',15)