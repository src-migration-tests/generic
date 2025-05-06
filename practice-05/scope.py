# global scope
x = 1


def do_something(x=2):
    # local scope
    x += 3
    print(x)


do_something(4)
print(x)

# -----------

x = 1


def do_something_else():
    x = 2
    print(x)


do_something_else()
print(x)

'''
При объявлении переменной: по умолчанию ей назначается самый глубокий scope
 * даже если во внешнем scope'е есть переменная с таким же именем
 
При обращении к значению переменной:
 - сначала ищется среди locals
 - если там не найдена, ищется среди nonlocals
 - если и там не найдена, то globals
'''

# -----------

x = 2


def make_global_impact():
    global x
    x = 3
    print(x)


make_global_impact()
print(x)
