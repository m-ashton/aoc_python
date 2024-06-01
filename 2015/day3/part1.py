from collections import defaultdict

def build_delivery_grid(grid_string):
    pos = (0, 0)
    grid = defaultdict(lambda: 0)
    grid[pos] = 1

    for c in grid_string:
        match c:
            case '<':
                pos = (pos[0] - 1, pos[1])
                grid[pos] += 1
            case '>':
                pos = (pos[0] + 1, pos[1])
                grid[pos] += 1
            case '^':
                pos = (pos[0], pos[1] + 1)
                grid[pos] += 1
            case 'v':
                pos = (pos[0], pos[1] - 1)
                grid[pos] += 1
    return grid

def main():
    with open("./input.txt", "r") as input_file:
        grid = build_delivery_grid(input_file.read().strip())
        print(len(grid.keys()))

if __name__ == '__main__':
    main()
