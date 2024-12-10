from timing import timing
from read_data import read_data


def find_trailhead_score(data, i, j, x, reachable):
    if x == "9":
        if reachable is not None:
            reachable[i][j] = True
        return 1

    x = str(int(x) + 1)

    res = 0
    if i > 0 and data[i - 1][j] == x:
        res += find_trailhead_score(data, i - 1, j, x, reachable)
    if j > 0 and data[i][j - 1] == x:
        res += find_trailhead_score(data, i, j - 1, x, reachable)
    if i + 1 < len(data) and data[i + 1][j] == x:
        res += find_trailhead_score(data, i + 1, j, x, reachable)
    if j + 1 < len(data[i]) and data[i][j + 1] == x:
        res += find_trailhead_score(data, i, j + 1, x, reachable)

    return res


@timing
def part1(data):
    res = 0

    for i, _ in enumerate(data):
        for j, _ in enumerate(data):
            if data[i][j] == "0":
                reachable = [[False] * len(data[i]) for i in range(len(data))]
                find_trailhead_score(data, i, j, "0", reachable)
                for line in reachable:
                    for item in line:
                        if item:
                            res += 1

    return res


@timing
def part2(data):
    res = 0

    for i, _ in enumerate(data):
        for j, _ in enumerate(data):
            if data[i][j] == "0":
                res += find_trailhead_score(data, i, j, "0", None)

    return res


data = read_data()
print(f"Part 1 result: {part1(data)}")
print(f"Part 2 result: {part2(data)}")
