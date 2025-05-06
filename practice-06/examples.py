# Simple task

'''
Напишите функцию, которая принимает строку s и число x и возвращает
множество символов, которые входят в строку не меньше x раз

- определить функцию
- для всех возможных символов найти их число вхождений в строку
    > for по всем символам
    > внутри цикла - считаем количество вхождений
- оставить только часто входящие
- сделать множество
- вернуть
'''

def count_frequent(s: str, x: int) -> set[str]:
    result = set()
    for ch in range(ord('a'), ord('z') + 1):
        c = chr(ch)
        if s.count(c) >= x:
            result.add(c)
    return result

''' 
26 * |s| iterations
'''

def count_frequent(s: str, x: int) -> set[str]:
    count = {
        chr(c): 0 
        for c in range(ord('a'), ord('z') + 1)
    }
    for c in s:
        count[c] += 1
    
    result = set()
    for ch in range(ord('a'), ord('z') + 1):
        if count[chr(ch)] >= x:
            result.add(chr(ch))
    return result


'''
result = set()
for ch in <...>:
    if <condition(ch)>:
        result.add(ch)
        
result = {
    ch
    for ch in <...>
    if <condition(ch)>
}
'''

def count_frequent(s: str, x: int) -> set[str]:
    count = {
        chr(c): 0 
        for c in range(ord('a'), ord('z') + 1)
    }
    for c in s:
        count[c] += 1
    
    # result = set()
    # for ch in range(ord('a'), ord('z') + 1):
    #     if count[chr(ch)] >= x:
    #         result.add(chr(ch))
    # return result
    
    return {chr(ch) for ch in range(ord('a'), ord('z') + 1) if count[chr(ch)] >= x}

'''
list вместо set
'''

def count_frequent(s: str, x: int) -> set[str]:
    result = []
    for ch in range(ord('a'), ord('z') + 1):
        c = chr(ch)
        if s.count(c) >= x:
            result.append(c)
    return result


# Another easy example

'''
Напишите функцию, которая принимает три целых числа a, b, c и 
возвращает 'EVEN', если между a и b есть четное количество чисел, делящихся на c,
и 'ODD' иначе

- ? кол-во чисел, делящихся на c, между a и b
    > числа между a и b - range(a, b+1)
    > делящихся на c - x mod c == 0
'''

def count_divisible(a: int, b: int, c: int):
    count = 0
    for x in range(a, b):
        if x % c == 0:
            count += 1
    if count % 2 == 0:
        return 'EVEN'
    else:
        return 'ODD'
    
# Recursion

'''
Дана функция f(x) = [
    f(x // 2) + f(x + 1), если x четно
    2 * f(x - 2), если x нечетно
]
f(0) = 1
'''

import sys

sys.setrecursionlimit(200000)

MEMORY = {}

def f(x: int) -> int:
    if x == 0:
        return 1
    if x in MEMORY:
        return MEMORY[x]
    
    if x % 2 == 0:
        value = f(x // 2) + 2 * f(x - 1)
    else:
        value = 2 * f(x - 2)
    MEMORY[x] = value
    return value


from functools import lru_cache

# Decorator
@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# fib = lru_cache(maxsize=None)(fib)


def cache(fn):
    MEMORY = {}
    
    def wrapper(*args):
        if args in MEMORY:
            return MEMORY[args]
        value = fn(*args)
        MEMORY[args] = value
        return value

    return wrapper

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# fib = cache(fib)

'''
Вывести все объекты какого-то вида
- вывести все перестановки массива
- вывести все сочетания из n по k

- Ханойские башни
- коды Грея
'''

def all_permutations(n: int, permutation_prefix: list[int]):
    print(f'{"\t" * len(permutation_prefix)} > called all_permutations({n=}, {permutation_prefix=})')
    
    if len(permutation_prefix) == n:
        print(permutation_prefix)
    
    for i in range(1, n + 1):
        if i not in permutation_prefix:
            all_permutations(n, permutation_prefix + [i])

'''
                         |-|
                        |---|
                       |-----|
                      |-------| 
'''

'''
n = 1

n > 1

   |-|                      
  |---|                     
 |-----|                     
|-------|            
             
> 4 диска c 3 на 1
  1. 3 диска с 3 на 2
  2. оставшийся диск с 3 на 1
  3. 3 диска со 2 на 1
'''

def hanoi(n, d_from, d_to, discs: list[list[int]]):
    def move(x, y):
        discs[y - 1].append(discs[x - 1][-1])
        discs[x - 1].pop()
        print(discs)
        
    if n == 1:
        move(d_from, d_to)
        return
    
    d_extra = 6 - d_from - d_to
    hanoi(n - 1, d_from, d_extra, discs)
    move(d_from, d_to)
    hanoi(n - 1, d_extra, d_to, discs)
    

'''
Коды Грея
000
001
011
010
110
111
101
100

0000
0001
0011
0010
0110
0111
0101
0100
1100
1101
1111
1110
1010
1011
1001
1000
'''

def grey_code(n: int):
    if n == 1:
        return ["0", "1"]
    prev = grey_code(n - 1)
    return ["0" + code for code in prev] + ["1" + code for code in reversed(prev)]


for code in grey_code(5):
    print(code)