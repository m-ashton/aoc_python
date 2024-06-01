def main():
    with open("input.txt", "r") as input_file:
        total_area = 0
        package_dimensions = input_file.read().strip().split("\n")
        for dim in package_dimensions:
            l, w, h = map(int, dim.split("x"))
            side_areas = [l*w, w*h, l*h]
            total_area += sum([2 * x for x in side_areas]) + min(side_areas)
        print(total_area)


if __name__ == "__main__":
    main()
