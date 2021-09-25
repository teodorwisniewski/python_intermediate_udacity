from .animal import Animal

class Dog(Animal):

    def __init__(self, name:str, age:int, breed:str, weight:int):
        """Create a new dog"""
        self.breed = breed
        self.weight = weight
        super().__init__(name, age)

    def speak(self) -> None:
        """Make the dog bark"""
        print(f'{self.name} says, "woof"')