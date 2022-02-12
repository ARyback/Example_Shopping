from product import Product

class ShoppingCart:
    def __init__(self):
        self.name_of_product = []
        self.price_total = 0
        self.category = []
    
    def add_product(self, name_of_product, price, category):      
        self.name_of_product.append(name_of_product)
        self.price_total += price
        self.category.append(category)
        pass

    def empty_cart(self):
        self.name_of_product = []
        self.price_total = 0
        self.category = []




    