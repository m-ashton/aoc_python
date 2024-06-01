def main():
    with open("input.txt") as input_file:
        instructions = input_file.read()
        floors_up = instructions.count("(")
        floors_down = instructions.count(")")
        print(floors_up - floors_down)

if __name__ == '__main__':
    main()
