from itertools import pairwise
FORBIDDEN_PAIRS = (('a', 'b'), ('c', 'd'), ('p', 'q'), ('x', 'y'))

def is_nice(word):
    doubled_letter = False
    vowel_count = word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')
    for pair in pairwise(word):
        if pair in FORBIDDEN_PAIRS:
            return False
        if pair[0] == pair[1]:
            doubled_letter = True
    return doubled_letter and vowel_count >= 3

def main():
    with open('input.txt', 'r') as input_file:
        strings = input_file.read().splitlines()
        print(len(list(filter(is_nice, strings))))

if __name__ == '__main__':
    main()

