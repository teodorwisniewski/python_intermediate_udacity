class Customer:

    def __init__(self,firstname, lastname, tier="free", price=0):
        self.firstname = firstname
        self.lastname = lastname
        self.tier = tier
        self.price = price

    @property
    def name(self):
        return self.firstname + " " + self.lastname

    def can_access(self,info):
        if self.tier == 'premium':
            return True
        return info["tier"] == self.tier

    @classmethod
    def premium(cls,firstname, lastname):
        return cls(firstname,lastname, tier='premium', price=10)

    def bill_for(self,nb_moths):
        return nb_moths*self.price

if __name__ == '__main__':
    # This won't run until you implement the `Customer` class!

    marco = Customer('Marco', 'Polo')  # Defaults to the free tier
    print(marco.name)  # Marco Polo
    print(marco.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(marco.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # False

    victoria = Customer.premium("Alexandrina",
                                "Victoria")  # Build a customer around the ('premium', 10$/mo) streaming plan.
    print(victoria.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(victoria.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # True
    print(victoria.bill_for(5))  # => 50 (5 months at 10$/mo)
    print(victoria.name)  # Alexandrina Victoria