# 🔹 Task 3: Online Shopping Cart (Composition + Abstraction)
# Requirements:
# Classes: Product, Cart, User, Order
# Cart should:
# Add/remove products
# Calculate total
# Apply discounts
# Stretch Goal: Introduce DiscountStrategy as an abstract class and create different discount policies (strategy pattern).

class Product:
    def __init__(self, product_id, product_name, product_price, available=0):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.available = available

    def add(self, added_count):
        if self.available > 0:
            res = added_count*self.product_price
            self.available -= int(self.available)
            return res
        else:
            return f'{self.product_name.lower()} is not available'


    # def __str__(self):
    #     return f"Product: {self.product_name}, Price: {self.product_price}"
    
class User:
    def __init__(self, username):
        self.username = username

    def add_product(self, item, cnt=0):
        tot_amt = item.add(cnt)
        return f'{item.product_name} : {cnt}*{item.product_price} = {tot_amt}'
        # return f"{self.username} want to add {item.product_name.lower()}."

milk = Product('SGS1', 'Milk', 25, 10)
curd = Product('SGS2', 'Curd', 29)

siva = User('Siva')
kowsi = User('Kowsi')

print(siva.add_product(milk, 2))
print(kowsi.add_product(curd, 1))

