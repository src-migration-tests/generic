def calculate_something(*args, **kwargs):
    return len(args) + kwargs['value'] + 12


'''
function(<input>) -> <output>

logger(function) -> function2
function2(<input>)
    1. print(<input>)
    2. function(<input>) -> <output>
    3. print(<output>)
'''


def logger(function):
    def wrapper(*args, **kwargs):
        print(f'Args are {args}, Kwargs are {kwargs}')
        result = function(*args, **kwargs)
        print(f'Result is {result}')
        return result

    return wrapper


calculate_something2 = logger(calculate_something)
calculate_something2(1, 2, 3, value=125, x=2)


def fun1(x, y):
    def fun2(z):
        # z - local
        # x, y - nonlocal
        return x + y + z

    return fun2


f = fun1(1, 2)
print(f(3))