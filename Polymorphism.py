#overriding polymorphism
'''class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
class Cat(Animal):
    def sound(self):
        print("Cat Meow")
animals=[Animal(),Dog(),Cat()]
for i in animals:
    i.sound()'''
'''class Food:
    def biryani(self):
        print("Ak biryani is famous in GNT")
class Chicken(Food):
    def biryani(self):
        print("Chicken biryani")
class Mutton(Food):
    def biryani(self):
        print("Mutton biryani")
biryanis=[Chicken(),Mutton()]
for i in biryanis:
    i.biryani()'''

class Coolingmode:
    def biryani(self):
        print("Ak biryani is famous in GNT")
class Chicken(Food):
    def biryani(self):
        print("Chicken biryani")
class Mutton(Food):
    def biryani(self):
        print("Mutton biryani")
biryanis=[Chicken(),Mutton()]
for i in biryanis:
    i.biryani()
