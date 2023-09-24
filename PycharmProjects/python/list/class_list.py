class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Alice", 25)
print(person1)
person2 = Person("Bob", 30)
print(person2)
people = [person1, person2]
print(people)
