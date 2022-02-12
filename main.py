from customer import Customer
from product import Product
from shoppingcart import ShoppingCart

newer_customer = Customer('Adam')
print(newer_customer.name)
newer_customer.add_product_to_cust_cart("LOTR Book", 12, "Books")
newer_customer.add_product_to_cust_cart("Monopoly", 15, "Games")
newer_customer.add_product_to_cust_cart("Cuzco", 130, "LLamas")

newer_customer.view_product()
total_price = newer_customer.view_price_total()
print(total_price)
newer_customer.new_shopping_cart.empty_cart()
newer_customer.view_product()

