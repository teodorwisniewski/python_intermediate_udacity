class Cat():
    def __init__(self, name, age, isIndoor=True):
        self.name = name
        self.age = age
        self.isIndoor = isIndoor
        
        if not isinstance(name,str):
            raise Exception(f"name: {name} is not a string")
        
        if age<0:
            raise Exception('Age must be 0 or greater.')

    def speak(self, greeting: str):
        if not isinstance(greeting,str):
            raise Exception("bad greeting")
        print(f'{self.name} says, "{greeting}"')

        
try:
    herbert = Cat("Herber", 2)
    herbert.speak(5)
except Exception as e:
    print(e)
    print('Bad Cat')