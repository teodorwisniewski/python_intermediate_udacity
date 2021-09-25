from abc import abstractmethod, ABC

class Animal(ABC):

    def __init__(self, name:str, age:int):
        """Create a new dog"""
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self):
        pass
    
    
class Cat(Animal):
    isIndoor = True

    def __init__(self, name, age, isIndoor=True):
        """Create a new cat"""
        super().__init__(name, age)
        self.isIndoor = isIndoor

    def speak(self):
        """Make the cat pur"""
        print(f'{self.name} says, "purrrrrr"')
        
        
class Dog(Animal):

    def __init__(self, name:str, age:int, breed:str, weight:int):
        """Create a new dog"""
        super().__init__(name, age)
        self.breed = breed
        self.weight = weight

    def speak(self) -> None:
        """Make the dog bark"""
        print(f'{self.name} says, "woof"')


class Frog(Animal):

    def __init__(self, name, age, color='green'):
        """Create a new cat"""
        super().__init__(name, age)
        self.color = color

    def speak(self):
        """Make the cat pur"""
        print(f'{self.color.title()} frog named {self.name} says, "kumkum"')
        
        
if __name__ == "__main__":
    wiskers = Cat('Wiskers', 3)
    paws = Dog('Mr. Paws', 4, 'dachshund', 18)
    frog = Frog('Mr. Green', 4)
    wiskers.speak()
    paws.speak()
    frog.speak()