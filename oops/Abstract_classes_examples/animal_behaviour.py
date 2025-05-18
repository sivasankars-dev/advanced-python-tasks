# Scenario:
# Create a base structure for different animals. Each animal can speak, but how it speaks depends on the animal type.
# Requirements:
# Create an abstract class Animal with an abstract method speak().
# Implement subclasses:
# Dog → prints "Woof!"
# Cat → prints "Meow!"
# Snake → prints "Hiss!"
# Write a function make_it_speak(animal: Animal) that accepts any Animal subclass and calls speak().

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")
    
class Snake(Animal):
    def speak(self):
        print("Hiss!")

def make_it_speak(animal: Animal):
    animal.speak()

make_it_speak(Dog())
make_it_speak(Cat())
make_it_speak(Snake())