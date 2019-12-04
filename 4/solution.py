from itertools import groupby

"""
It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
"""
def validate_number(n):
    str_n = str(n)
    lengths = [len(group) for group in [list(group) for char, group in groupby(str_n)]]
    has_adjacent_chars = False
    try:
        lengths.index(2)
        has_adjacent_chars = True
    except ValueError:
        return False

    is_increasing = all(int(i) <= int(j) for i, j in zip(str_n, str_n[1:]))
    return is_increasing and has_adjacent_chars


if __name__== "__main__":
    min = 307237
    max = 769058
    valid_count = 0
    for n in range(min, max + 1):
        if validate_number(n):
            valid_count += 1

    print('valid_count: {}'.format(valid_count))
