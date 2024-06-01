from collections import defaultdict

def build_delivery_grid(grid_string):
    santa_pos = (0, 0)
    robo_santa_pos = (0, 0)
    grid = defaultdict(lambda: 0)
    grid[(0,0)] = 2

    for idx, c in enumerate(grid_string):
        match c:
            case '<':
                move = (-1, 0)
            case '>':
                move = (1, 0)
            case '^':
                move = (0, 1)
            case 'v':
                move = (0, -1)
        if idx % 2 == 0:
            santa_pos = (santa_pos[0] + move[0], santa_pos[1] + move[1])
            grid[santa_pos] += 1
        else:
            robo_santa_pos = (robo_santa_pos[0] + move[0], robo_santa_pos[1] + move[1])
            grid[robo_santa_pos] += 1

    return grid

def main():
    with open("./input.txt", "r") as input_file:
        grid = build_delivery_grid(input_file.read().strip())
        print(len(grid.keys()))

if __name__ == '__main__':
    main()
