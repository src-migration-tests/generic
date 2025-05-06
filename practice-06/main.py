# Primitives

a = 1
a = 'str'
a = True
a = 1.4

print(a)
print(f'{a:.5f}')

# Collections

a = [1, 2, 3] # list
b = {1, 2, 3} # set
c = {'1': 1, '2': 2, '3': 3} # dict

a[1], c['1']

# Conditions and if / Loops

if len(a) == 2:
    print('two')
elif len(a) == 3:
    print('three')
else:
    print('something else')
    
# Loop

while len(a) > 0:
    print(a[-1])
    a.pop()
    
for kv in c.items():
    print(kv)
    
# Functions

def function_name(a: int, b: int, c: str):
    print(a, b, c)
    return a + b * len(c)

print(function_name(1, 2, '5'))
print(function_name(1, 3, 'abcaba'))

# Collection comprehension

a = [
    x ** 3
    for x in range(20)
    if x % 2 == 1
]
print(a)

c = {
    x: x ** 3
    for x in range(20)
    if x % 2 == 1
}
print(c)