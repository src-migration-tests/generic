# Минимальная единица измерения - байт (8 бит)
# 00000000_2, 11111111_2

print(int('00000000', 2), int('11111111', 2))

# Байт принимает значения от 0 до 255 = всего 256 значений

print(ord('a'), chr(97))

# AB_d = A * d + B
# 123_10 = 1 * 10^2 + 2 * 10 + 3
# 472_8 = 4 * 8^2 + 7 * 8 + 2
# 0 1 2 3 4 5 6 7 8 9 a b c d e f

s = '65 48 6c 6c 20 6f 6f 77 6c 72 21 64'
s = list(map(lambda x: int(x, 16), s.split()))

s[::2], s[1::2] = s[1::2], s[::2]
print(s)

for c in s:
    print(chr(c), end = ', ')
    
for c in range(256):
    print(c, chr(c))
    
# Encoding / кодировка

def to_bytes(s, enc='utf-8'):    
    b = s.encode(enc)
    b = list(map(int, b))
    print(b)

# Кодировка - это набор правил преобразования последовательности байт в последовательность символов
# ASCII - "каждый байт - отдельный символ"
# UTF-8:
# - определенный интервал байт - читаем как есть (с 33 по 126, возможно больше)
# - если видим байт не из этого интервала, воспринимаем его и 1-2 следующих как один символ

rs = 'Русские буквы'
to_bytes(rs)
rs2 = '™ ≈ ≠ µ'
to_bytes(rs2)

# Работаем с файлами

fd = open('example.txt')
print(fd.readline().rstrip('\n'))
print(fd.readline().rstrip('\n'))
fd.close()

# 1. Закрывайте файл сразу
#   1.1. файлы надо закрывать, чтобы не увеличивать нагрузку на операционную систему
#   1.2. если вы писали что-то новое в файл, и не закрыли его, не факт, что оно запишется

try:
    fd = open('example.txt')
    a = int(fd.readline().rstrip())
    b = int(fd.readline().rstrip())
    c = int(fd.readline().rstrip())
    d = a / c
    fd.close()
except:
    print(fd.closed)

#   1.3. Resource management

'''
with <RESOURCE_INIT> as <NAME>:
    do_something()
'''

try:
    with open('example.txt') as fd:
        a = int(fd.readline().rstrip())
        b = int(fd.readline().rstrip())
        c = int(fd.readline().rstrip())
        print(a / c)
except:
    print(fd.closed)
    
# 2. Режимы работы с файлом

MODES = [
    'r',  # чтение (read)
    'a',  # дозапись в конец (append)
    'w',  # запись (write)
    'br',  # байтовое чтение (bytes)
    'ba', # bytes append
    'bw', # bytes write
    'r+', # чтение + запись
]

additional_data = 'X\n0023687\na+b+c+d!'
with open('example.txt', 'a') as fd:
    # +: print печатает что угодно, автоматически преобразуя в строку
    # -: лишний перевод строки в конце
    # -: не работает с байтовым режимом
    # print(additional_data, file=fd, end='')
    
    # +: почти все ок
    # -: принимает только строку (или байты в байтовом режиме)
    fd.write(additional_data)
    
with open('example.txt', encoding='utf-8') as fd:
    print(fd.read())
    
# Почитайте про чтение и запись файлов
# Почитайте про -"-, но в байтовом режимe

a = [10, 122, 47368768, 243897, 43987687, 22222]
with open('code', 'wb') as fd:
    for item in a:
        fd.write(item.to_bytes(4))
    
b = []
with open('code', 'br') as fd:
    while True:
        data = fd.read(4)
        if len(data) == 0:
            break
        b.append(int.from_bytes(data))
print(b)
        
# ~10^9 = 
#  - 9-10 цифр, то есть 9 или 10 байт в текстовом режиме
#  - ~2^30 < 2^32 = 4 байта