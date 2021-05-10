class Product:
    def __init__(self,name,price,category):
        self.name=name 
        self.price=price
        self.category=category
    def update_price(self,percent_change,is_increased):
        if is_increased:
            self.price += self.price * percent_change/100
        elif not is_increased:
             self.price -= self.price * percent_change/100
    def print_info(self):
        print("Product name:", self.name, "Category:", self.category, "Price:", self.price)
class Store:
    def __init__(self,name,owner,products=[]):
        self.name=name
        self.owner=owner
        self.products=Products
    def add_product(self, new_product):
        self.products.append(new_product)
    def sell_product(self, id):
        self.products.pop(id)
    def inflation(self, percent_increase):
        Product.update_price(percent_change,true)
    def set_clearance(self, category, percent_discount):
        Product.update_price(percent_change,False)
TV = Store.add_product("TV")
TV.print_info()