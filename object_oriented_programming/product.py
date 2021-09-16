

class Product:
    products = []

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        self.reviews = []
        Product.products.append(self)

    @property
    def available(self):
        return self in Product.products
