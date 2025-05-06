from defintions.consts import POSITIONS


def replace_part(hanger, failure_no):
    row, column, char = POSITIONS[failure_no]
    hanger[row][column] = char


def print_gallows(hanger):
    for line in hanger:
        print(''.join(line))
