class Animal:
    def sound(self):
        pass  # generic (to be defined by subclasses)

class Lion(Animal):
    def sound(self):
        return "Gurr"

class Dog(Animal):
    def sound(self):
        return "Woo Woo"

class Cat(Animal):
    def sound(self):
        return "Meow Meow"

# Demonstrating polymorphism
animals = [Lion(), Dog(), Cat()]

for animal in animals:
    print(animal.sound())
