from itertools import pairwise

def has_repeated_letter_separated_by_one(word):
    for idx, c in enumerate(word):
        if idx > len(word) - 3:
            return False
        if c == word[idx + 2]:
            return True

def has_non_overlapping_repeated_pair(word):
    pairs = list(pairwise(word))
    for idx, pair in enumerate(pairs):
        count = pairs.count(pair)
        if count > 2:
            return True
        if count == 2:
            try:
                second_idx = pairs.index(pair, idx + 1)
                if second_idx - idx > 1:
                    return True
            except ValueError:
                pass # this happens if we're checking the second pair
    return False


def is_nice(word):
    return has_repeated_letter_separated_by_one(word) and has_non_overlapping_repeated_pair(word)

def main():
    with open('input.txt', 'r') as input_file:
        strings = input_file.read().splitlines()
        print(len(list(filter(is_nice, strings))))

if __name__ == '__main__':
    main()
