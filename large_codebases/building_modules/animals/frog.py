from .animal import Animal

class Frog(Animal):

    def __init__(self, name: str, age:int, color='Green'):
        self.color = color
        super().__init__(name, age)

    def speak(self):
        """Make the cat pur"""
        print(f'{self.name} says, "ribbit"')