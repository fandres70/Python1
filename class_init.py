# Filename: class_init.py
# Simple class showing the use of the __init__ method

class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        'Prints a simple introduction with the parameter as name.'
        print('Hello, my name is', self.name)

Person('Ilir').sayHi()