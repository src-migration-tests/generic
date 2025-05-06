import random

from defintions.consts import WORDS
from logic.game import run_game

random.seed()
word = random.choice(WORDS)
run_game(word)
