from product import Product
from review import Review
# A User will have an id and a name, and be able to sell_product, buy_product, and write_review

class User:

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.reviews = []

    def __str__(self):
        return f"User({self.user_id}, {self.name}, {self.reviews})"

    def sell_product(self, name, description, price):
        p = Product(name, description, price)
        return p

    def buy_product(self, prod):
        if prod in Product.products:
            Product.products.remove(prod)

    def write_review(self, desciption, product):
        rev = Review(desciption)
        self.reviews.append(rev)
        product.reviews.append(rev)
        return rev


if __name__ == "__main__":
    brianna = User(1, 'Brianna')
    mary = User(2, 'Mary')

    keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
    print(keyboard.available)  # => True
    print(keyboard)
    mary.buy_product(keyboard)
    print(keyboard.available)  # => False
    review = mary.write_review('This is the best keyboard ever!', keyboard)
    print(keyboard)
    print(review in mary.reviews)  # => True
    print(review in keyboard.reviews)  # => True