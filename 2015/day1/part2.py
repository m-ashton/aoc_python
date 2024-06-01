def main():
    with open("input.txt") as input_file:
        instructions = input_file.read()
        floor = 0
        for idx, c in enumerate(instructions):
            if c == '(':
                floor += 1
            elif c == ')':
                floor -= 1
            if floor == -1:
                print(idx + 1)
                return
        print("never entered basement")

if __name__ == '__main__':
    main()
