# 1 Type hints

def add(x: str, y: str) -> str:
    return x.lower() + y.upper()


# 2 Argument kinds

# 2.1 Positional arguments, key/value arguments

def primitive(x, y):
    return x + y


print(primitive(1, 2))
print(primitive(x=1, y=2))
print(primitive(1, y=2))

primitive(y=1, x=2)


# function(value1, value2, ..., keyx=valuex, keyy=valuey, ...)

# 2.2 Default values

def calculate(x: int, y: int, mode: str = 'int'):
    # Logic
    result = x + y
    # Parametrized logic
    if mode == 'int':
        return result
    elif mode == 'bin':
        return bin(result)[2:]
    elif mode == 'str':
        return str(result)
    else:
        pass


print(calculate(1, 2, 'bin'))
print(calculate(1, 2))


# 2.2.* Collections as default values

def do_something(a: int, b: list = []):
    if a not in b:
        b.append(a)
    return len(b)


print(do_something(1))
print(do_something(2))


def do_something_correct(a: int, b: list | None = None):
    if b is None:
        b = []
    if a not in b:
        b.append(a)
    return len(b)


def do_something_primitive(a: int, b: int = 10):
    b = b + 1
    a += b
    print(a)


do_something_primitive(1)
do_something_primitive(1)

# В чем отличие
'''
b.append(1)
- address(b) -> идет в первую ячейку -> пишет туда 1

b = b + 1
- в локальную переменную b назначается новое значение, равное b + 1
'''

'''
1.  
def do_something(b = [])
Memory
| | | | | | [ | | ] | | | | | | | | | |
 0 1 2 3 4 5 6 7 8 9
 b = <address 6>
 
2.
do_something()
    b.append(1)
# b -> 6 -> по этому адресу пишем 1
Memory
| | | | | | [1| | ] | | | | | | | | | |
 0 1 2 3 4 5 6 7 8 9

3.
do_something()
    b.append(2)
# b -> 6 -> в следующую свободную ячейку за 6 пишем 2
Memory
| | | | | | [1|2| ] | | | | | | | | | |
 0 1 2 3 4 5 6 7 8 9
'''

'''
1.
def do_something_primitive(a: int, b: int = 8):
    b = b + 1
    a += b
    print(a)
Memory
|   |   |   | 8 |   |   |
  0   1   2   3   4   5 
 b = <address 3>

2.
do_something_primitive(1)
    b = b + 1

Memory
|   |   |   | 8 |   |   |
  0   1   2   3   4   5 

 2.1. взять <address 3> -> 8
 2.2. увеличить на 1 -> получили 9
 2.3. положить 9 куда-то в свободное место в памяти
 
Memory
|   |   |   | 8 |   | 9 |
  0   1   2   3   4   5 
 
 2.4. записать в b адрес этого нового значения
 b = <address 5>
'''


# 2.3 Key-only arguments, Positional-only arguments

def calculate2(x: int, y: int, /, *, mode: str = 'int'):
    # Logic
    result = x + y
    # Parametrized logic
    if mode == 'int':
        return result
    elif mode == 'bin':
        return bin(result)[2:]
    elif mode == 'str':
        return str(result)
    else:
        pass


# calculate2(x=1, y=2, mode='x')
# calculate2(1, 2, 'int')
calculate2(1, 2, mode='int')


# 2.4 First-class object


def comparator(x: int) -> int:
    return -x


a = [2, 5, 4, 1, 2, 6, 7, 9, 3]
a.sort(key=comparator)
print(a)

a = ['1', '2', '123']
print(list(map(int, a)))

# map(function, a) = [function(a[0]), function(a[1]), ..., function(a[-1])]

# 2.4.* Lambda functions
# == временная функция без имени

# создать (определить) функцию
# не назначать ей имя
# тут же один раз ее использовать
# и больше никогда о ней не вспоминать

'''
def function(arg1, args2):
    return <expression>

lambda arg1, arg2: <expression>
'''


def function(x: float) -> float:
    return x ** 3 / 10


print(list(map(function, [1, 2, 3, 4])))

print(list(map(
    lambda x: x ** 3 / 10,
    [1, 2, 3, 4]
)))


# 2.5 Variadic arguments

def variadic_function(*args):
    print(type(args), len(args), args)
    print(args[0])


def non_variadic_function(args: tuple):
    print(type(args), len(args), args)
    print(args[0])


variadic_function(1, 2, 3, 4, 5)
non_variadic_function((1, 2, 3, 4, 5))

a = list(map(int, input().split()))
variadic_function(*a)