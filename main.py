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

# class person:
#     def __init__(self, firstname, lastname, status, numder):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.status = status
#         self.numder = numder
#
#     def __str__(self):
#         return f'Меня зовут {self.firstname} {self.lastname}, я учусь на {self.status} и я нахожусь на {self.numder} месте в списке'
#
# person1 = person("Иван", "Иванов", "5", "23")
# person2 = person("Алексей", "Рыбаков", "4", "25")
# person3 = person("Пётр", "Соколов", "3", "21")
# person4 = person("Мария", "Воровна", "5", "30")
#
# print(person1)
# print(person2)
# print(person3)
# print(person4)

# class transport:
#     def __init__(self, speed, color):
#         self.speed = speed
#         self.color = color
#
#     def beep(self):
#         print('beep')
#
# class car(transport):
#     def __init__(self, speed, color, owner):
#         super().__init__(speed, color)
#         self.owner = owner
#
#     def say_owner(self):
#         print(f'Владелец {self.owner}')
#
# class sportcar(car, transport):
#     pass
#
# car11 = sportcar(150, 'white', "Алексей")
# print(car11.speed)
# car11.say_owner()

# class bus(transport):
#     def __init__(self, speed, color, seeds):
#         super().__init__(speed, color)
#         self.seeds = seeds
#
#     def say_seeds(self):
#         print(f'Кол-во мест {self.seeds}')


# car1 = car(100, 'yellow', 'Василий')
# bus1 = bus(60, 'red', 42)
# print(car1.color)
# print(car1.speed)
# print(car1.owner)
#
# car1.beep()
# car1.say_owner()
#
#
# print(bus1.color)
# print(bus1.speed)
# print(bus1.seeds)
# bus1.say_seeds()


class roditel:
    def __init__(self, eyes, hair, growth):
        self.eyes = eyes
        self.hair = hair
        self.growth = growth

    def say_name(self):
        print("Я твой папа")

class soon(roditel):
    def __init__(self, eyes, hair, growth, ears):
        super().__init__(eyes, hair, growth)
        self.ears = ears

    def say_name1(self):
        print('Я сын')

parents1 = roditel("зелёные", "каштановые", 175)
soon1 = soon("голубые","светлые",160, 'длинные')
print(parents1.eyes, parents1.hair, parents1.growth)
print(soon1.eyes, soon1.hair, soon1.growth, soon1.ears)
parents1.say_name()
soon1.say_name1()
