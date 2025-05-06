from copy import deepcopy

from defintions.consts import GALLOWS, ALPHABET, POSITIONS
from logic.gallows import print_gallows, replace_part


def run_game(word):
    failures = 0
    guessed_chars = ['_' for _ in range(len(word))]
    guessed_count = 0

    gallows = deepcopy(GALLOWS)
    guesses = set()

    def check_finished():
        if failures == len(POSITIONS):
            print(f'Поражение! Это было слово \'{word}\'')
            return True
        if guessed_count == len(word):
            print('Победа!')
            return True
        return False

    while True:
        print_gallows(gallows)
        print(' '.join(guessed_chars))

        if check_finished():
            return

        s = input('Выберите букву: ')
        if s not in ALPHABET:
            print('Нет такой буквы')
            continue
        if s in guesses:
            print('Вы уже называли эту букву')
            continue

        guesses.add(s)
        char_found = False
        for i, c in enumerate(word):
            if c != s:
                continue
            guessed_chars[i] = c
            guessed_count += 1
            char_found = True

        if not char_found:
            replace_part(gallows, failures)
            failures += 1
