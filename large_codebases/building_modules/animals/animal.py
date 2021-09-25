from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self):
        pass
