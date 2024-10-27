from product import Product

class Store:
    def __init__(self, name, money):
        self.__name = name
        self.__money = money
        self.__products = []

    def order_product(self, product, quantity):
        if isinstance(product, Product) and product not in self.__products:
            product.increase_quantity(quantity)
            self.__products.append(product)
        else:
            print("Not a valid product")

    def find(self, product_id):
        for __product in self.__products:
            if __product.get_id() == product_id:
                return __product

    def sell_product(self, product_id, quantity):
        product = self.find(product_id)
        if isinstance(product, Product):
            if quantity <= product.get_quantity():
                self.__money += (product.get_price() * quantity)
                product.decrease_quantity(quantity)
            elif product.get_quantity() == 0:
                print(f"The item: {product.get_name()} is sold out.\n")
            elif quantity > product.get_quantity():
                if product.get_quantity() == 1:
                    print(f"This quantity ({quantity}) cannot be sold as there are only ({product.get_quantity()}) {product.get_name()} remaining in stock.")
                else:
                    print(f"This quantity ({quantity}) cannot be sold as there are only ({product.get_quantity()}) {product.get_name()}(s) remaining in stock.")

    def markup_prices(self, up_price):
        for product in self.__products:
            price = round(product.get_price() * up_price, 2)
            product.set_price(price)

    def __str__(self):
        if len(self.__products) == 0:
            return f"{self.__name.upper()}\nCurrent Holdings: ${self.__money}\nThis store is out of stock... of everything. *shrug*\n"
        else:
            products = ""
            for product in self.__products:
                p1 = f"===========\n{product}===========\n"
                products += p1

            return f"{self.__name.upper()}\nCurrent Holdings: ${self.__money}\nCurrent Stock:\n{products}"


store = Store("Sleep Token", 1000.0)
pillow = Product(1, "Pillow Set", "Set of two bamboo material pillows.", 45.99)
candle = Product(2, "Scented Candle", "Sandalwood, dual-wick candle.", 39.99)
print(store)

store.order_product(pillow, 2)
store.order_product(candle, 4)

store.sell_product(1, 3)
store.sell_product(1, 2)
store.sell_product(1, 2)
print(store)

store.markup_prices(1.5)
store.sell_product(2, 2)
print(store)