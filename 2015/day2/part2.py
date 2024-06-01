def main():
    with open("input.txt", "r") as input_file:
        ribbon_length = 0
        package_dimensions = input_file.read().strip().split("\n")
        for dim in package_dimensions:
            l, w, h = map(int, dim.split("x"))
            side_perimeters = [2*l + 2*w, 2*w + 2*h, 2*l + 2*h]
            ribbon_length += min(side_perimeters) + l * w * h
        print(ribbon_length)


if __name__ == "__main__":
    main()
