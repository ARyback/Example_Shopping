from distutils.dep_util import newer
from product import Product
from shoppingcart import ShoppingCart

class Customer:
    def __init__(self, name):
        self.name = name
        self.new_shopping_cart = ShoppingCart()
        pass

    def add_product_to_cust_cart(self, name, price, category):
        self.new_shopping_cart.add_product(name, price, category)
        return self.new_shopping_cart.name_of_product
    
    def view_product(self):
        print(self.new_shopping_cart.name_of_product)

    def view_price_total(self):
        return self.new_shopping_cart.price_total





