class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Creating an instance and calling a method
person = Person("Alice", 30)
person.say_hello()  # Output: "Hello, my name is Alice and I am 30 years old."

person2=Person("munna",40)
person2.say_hello()

