from timing import timing
from read_data import read_data


@timing
def part1(data):
    res = 0
    for i, x in enumerate(data):
        for j, y in enumerate(x):
            if y == "X":
                if (
                    j + 3 < len(x)
                    and x[j + 1] == "M"
                    and x[j + 2] == "A"
                    and x[j + 3] == "S"
                ):
                    res += 1
                if (
                    j - 3 >= 0
                    and x[j - 1] == "M"
                    and x[j - 2] == "A"
                    and x[j - 3] == "S"
                ):
                    res += 1
                if (
                    i + 3 < len(data)
                    and data[i + 1][j] == "M"
                    and data[i + 2][j] == "A"
                    and data[i + 3][j] == "S"
                ):
                    res += 1
                if (
                    i - 3 >= 0
                    and data[i - 1][j] == "M"
                    and data[i - 2][j] == "A"
                    and data[i - 3][j] == "S"
                ):
                    res += 1
                if (
                    i + 3 < len(data)
                    and j + 3 < len(x)
                    and data[i + 1][j + 1] == "M"
                    and data[i + 2][j + 2] == "A"
                    and data[i + 3][j + 3] == "S"
                ):
                    res += 1
                if (
                    i + 3 < len(data)
                    and j - 3 >= 0
                    and data[i + 1][j - 1] == "M"
                    and data[i + 2][j - 2] == "A"
                    and data[i + 3][j - 3] == "S"
                ):
                    res += 1
                if (
                    i - 3 >= 0
                    and j - 3 >= 0
                    and data[i - 1][j - 1] == "M"
                    and data[i - 2][j - 2] == "A"
                    and data[i - 3][j - 3] == "S"
                ):
                    res += 1
                if (
                    i - 3 >= 0
                    and j + 3 < len(x)
                    and data[i - 1][j + 1] == "M"
                    and data[i - 2][j + 2] == "A"
                    and data[i - 3][j + 3] == "S"
                ):
                    res += 1

    return res


@timing
def part2(data):
    res = 0
    for i, x in enumerate(data):
        for j, y in enumerate(x):
            if y == "A":
                if i + 1 < len(data) and j + 1 < len(x) and i - 1 >= 0 and j - 1 >= 0:
                    if (
                        data[i - 1][j - 1] == "M"
                        and data[i - 1][j + 1] == "M"
                        and data[i + 1][j - 1] == "S"
                        and data[i + 1][j + 1] == "S"
                    ):
                        res += 1
                    if (
                        data[i - 1][j - 1] == "S"
                        and data[i - 1][j + 1] == "M"
                        and data[i + 1][j - 1] == "S"
                        and data[i + 1][j + 1] == "M"
                    ):
                        res += 1
                    if (
                        data[i - 1][j - 1] == "S"
                        and data[i - 1][j + 1] == "S"
                        and data[i + 1][j - 1] == "M"
                        and data[i + 1][j + 1] == "M"
                    ):
                        res += 1
                    if (
                        data[i - 1][j - 1] == "M"
                        and data[i - 1][j + 1] == "S"
                        and data[i + 1][j - 1] == "M"
                        and data[i + 1][j + 1] == "S"
                    ):
                        res += 1

    return res


data = read_data()
print(f"Part 1 result: {part1(data)}")
print(f"Part 2 result: {part2(data)}")
