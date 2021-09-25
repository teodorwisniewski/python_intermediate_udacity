from .animal import Animal

class Cat(Animal):
    isIndoor = True

    def __init__(self, name: str, age:int, isIndoor=True):
        """Create a new cat"""
        self.isIndoor = isIndoor
        super().__init__(name, age)

    def speak(self):
        """Make the cat pur"""
        print(f'{self.name} says, "purrrrrr"')