# # 1.encapsulation
# class Person:
#     def __init__(self, _age):
#         self.age = _age
# 
# 
# 
#     def set_age(self, age: int):
#         if age < 0:
#             return print("Not zero")
#         self._age = age
# 
# 
# 
#     def get_age(self):
#         return f"{self._age}"
# 
# 
# person = Person(21)
# person.set_age(22)
# print(person.get_age())
# person.set_age(-5)
# 
#



# 2.Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return "I'm an animal"
#
#
#
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def speak(self):
#         return "'Woof'"
#
#
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def speak(self):
#         return "'Meow'"
#
# dog = Dog("Buddy")
# cat = Cat("Kitty")
#
# print(dog.name, dog.speak())
# print(cat.name, cat.speak())




# 3.Polymorphism
# class Vehicle:
#     """base class for all Vehicles"""
#     def move(self):
#         return "Vehicle is moving"
#
#
# class Car(Vehicle):
#     def move(self):
#         return "Car is driving"
#
#
# class Bicycle(Vehicle):
#     def move(self):
#         return "Bicycle is pedaling"
#
#
# def move(vehicle):
#     return vehicle.move()
#
# car = Car()
# bike = Bicycle()
#
# print(move(car))
# print(move(bike))



# 4.Abstraction
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())  # Вывод: 50
print(circle.area())  # Вывод: ~153.94