print(
    type('aiufhhun'),
    type(2346567),
    type(4354.4354),
)

# Object
# Class - категория объектов / тип

# Класс "строка" - это категория всех строковых объектов
'''
1. 'ahdiuhiu'/"dahishdi"
2. свои методы (split, strip, join, ...)
'''


def attend_lecture(person, course):
    ...


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def rest(self):
        print(f'Person {self.name} has rested')
    
    def attend_lecture(self, course):
        print(f'Person {self.name} attended course {course}')
        

john = Person('John', 18)
david = Person('David', 32)

john.attend_lecture('Programming')


class Teacher(Person):
    def attend_lecture(self, course):
        return f'Teacher {self.name} read a lecture on {course} to some students'


daniel1 = Person('Daniel', 25)
daniel2 = Teacher('Daniel', 25)

persons = [daniel1, daniel2, john, david]
for p in persons:
    p.rest()
    
    
class NPC:
    def attack(self, player):
        pass

class Bear(NPC):
    def attack(self, player):
        pass
    
class Wolf(NPC):
    def attack(self, player):
        pass

class Thug(NPC):
    def attack(self, player):
        pass


npcs = [Bear(...), Wolf(...), Wolf(...), Thug(...)]
i = 0
player = ...
while True:
    npcs[i].attack(player)
    i = (i + 1) % len(npcs)
    break
    


from dataclasses import dataclass

@dataclass
class Experiment:
    name: str
    data: list[int]
    result: float
    err: float
    
    def print_result(self):
        print(f'{experiment.result} +- {experiment.err}')
        
    def __matmul__(self, other):
        return 'anything'

experiment = Experiment('test exp', [1, 2, 3, 4, 5], 3.0, 0.001)
experiment.print_result()

print(experiment @ 'bv')