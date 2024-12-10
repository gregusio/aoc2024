from timing import timing
from read_data import read_data


def turn_right(d, x, y):
    if d == "U":
        return "R", x + 1, y
    if d == "R":
        return "D", x, y - 1
    if d == "D":
        return "L", x - 1, y
    if d == "L":
        return "U", x, y + 1


def go(dir, x, y):
    if dir == "U":
        x -= 1
    elif dir == "R":
        y += 1
    elif dir == "D":
        x += 1
    elif dir == "L":
        y -= 1

    return x, y


def find_visited(data, curr_x, curr_y):
    visited = list(map(lambda x: list(map(lambda _: False, x)), data))
    dir = "U"
    while True:
        if (
            curr_x < 0
            or curr_y < 0
            or curr_x >= len(data)
            or curr_y >= len(data[curr_x])
        ):
            break

        if data[curr_x][curr_y] == "#":
            dir, curr_x, curr_y = turn_right(dir, curr_x, curr_y)
            continue

        visited[curr_x][curr_y] = True
        curr_x, curr_y = go(dir, curr_x, curr_y)

    return visited


@timing
def part1(data):
    curr_x = 0
    curr_y = 0

    for i, _ in enumerate(data):
        for j, _ in enumerate(data[i]):
            if data[i][j] == "^":
                curr_x = i
                curr_y = j

    visited = find_visited(data, curr_x, curr_y)
    res = 0
    for line in visited:
        for item in line:
            if item:
                res += 1

    return res


@timing
def part2(data):
    curr_x = 0
    curr_y = 0
    for i, _ in enumerate(data):
        for j, _ in enumerate(data[i]):
            if data[i][j] == "^":
                curr_x = i
                curr_y = j

    points_to_block = []
    visited = find_visited(data, curr_x, curr_y)
    for i, line in enumerate(visited):
        for j, item in enumerate(line):
            if item:
                points_to_block.append((i, j))

    start_x = curr_x
    start_y = curr_y
    res = 0
    count = 0
    data = list(map(lambda x: list(x), data))

    for i, j in points_to_block:
        data[i][j] = "#"
        curr_x = start_x
        curr_y = start_y
        visited = [[[] for _ in range(len(data[x]))] for x in range(len(data))]
        count = 0

        dir = "U"
        while True:
            if (
                curr_x < 0
                or curr_y < 0
                or curr_x >= len(data)
                or curr_y >= len(data[curr_x])
            ):
                break

            if data[curr_x][curr_y] == "#":
                dir, curr_x, curr_y = turn_right(dir, curr_x, curr_y)
                continue

            count += 1
            if [True, dir] in visited[curr_x][curr_y]:
                res += 1
                break

            visited[curr_x][curr_y].append([True, dir])
            curr_x, curr_y = go(dir, curr_x, curr_y)

        data[i][j] = "."

    return res


data = read_data()
print(f"Part 1 result: {part1(data)}")
print(f"Part 2 result: {part2(data)}")
