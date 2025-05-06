ALPHABET = {chr(code) for code in range(ord('a'), ord('z'))}

WORDS = [
    'apple',
    'orange',
    'battle',
    'factory',
    'pycharm',
    'python',
    'code',
    'kotlin'
]

_GALLOWS = r'''
 ___
 |  \
    |
    |
    |
___/_\
'''
GALLOWS = list(map(list, _GALLOWS.split('\n')))

_GALLOWS_FULL = r'''
 ___
 |  \
 o  |
/|\ |
/ \ |
___/_\
'''
GALLOWS_FULL = list(map(list, _GALLOWS_FULL.split('\n')))

POSITIONS = []
for row, line, full_line in zip(range(len(GALLOWS)), GALLOWS, GALLOWS_FULL):
    for column in range(0, len(line)):
        if line[column] != full_line[column]:
            POSITIONS.append((row, column, full_line[column]))

print(POSITIONS)


def _priority(position):
    char_priority = 0 if position[2] == '|' else 1
    return position[0], char_priority


POSITIONS.sort(key=_priority)
