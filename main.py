# def func():
#     pass
#
# class Test:
#     pass
#
# print(type(5))
# print(type('a'))
# print(type(5.5))
# print(type(True))
# print(type([1, 2]))
# print(type((5, 4)))
# print(type({1, 2}))
# print(type({'a': 2}))
# print(type(Test))
# print(type(func))

# class Person:
#     name = "Лёша"
#     age = 42
#
#     def say(self):
#         print("hello")
#
# Alexey = Person()
# print(Alexey.name)
# print(Alexey.age)
# Alexey.say()
#
# Alexey2 = Person()
# Alexey2.name = "Не Лёша"
# print(Alexey2.name)
#
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# person1 = person('Иван', 15)
# person2 = person('Пётр', 14)
#
# print(person1.name)
# print(person1.age)
# print(person2.name)
# print(person2.age)
#
# class person:
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
#
#     def __str__(self):
#         return f'Меня зовут {self.name} {self.lastname}'
#
# person1 = person('Иван', 'Иванов')
# print(person1)

class person:
    def __init__(self, firstname, lastname, status, numder):
        self.firstname = firstname
        self.lastname = lastname
        self.status = status
        self.numder = numder

    def __str__(self):
        return f'Меня зовут {self.firstname} {self.lastname}, я учусь на {self.status} и я нахожусь на {self.numder} месте в списке'

person1 = person("Иван", "Иванов", "5", "23")
person2 = person("Алексей", "Рыбаков", "4", "25")
person3 = person("Пётр", "Соколов", "3", "21")
person4 = person("Мария", "Воровна", "5", "30")

print(person1)
print(person2)
print(person3)
print(person4)
