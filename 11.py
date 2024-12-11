from functools import cache

from timing import timing
from read_data import read_data


@timing
def part1(data):
    data = list(map(lambda x: int(x), data[0].split(" ")))
    for _ in range(25):
        zeros = list(map(lambda y: 1, list(filter(lambda x: x == 0, data))))
        evens1 = list(
            map(
                lambda y: int(str(y)[: len(str(y)) // 2]),
                list(filter(lambda x: len(str(x)) % 2 == 0, data)),
            )
        )
        evens2 = list(
            map(
                lambda y: int(str(y)[len(str(y)) // 2 :]),
                list(filter(lambda x: len(str(x)) % 2 == 0, data)),
            )
        )
        not_evens = list(
            map(
                lambda y: y * 2024,
                list(filter(lambda x: len(str(x)) % 2 == 1 and x != 0, data)),
            )
        )
        data = zeros + evens1 + evens2 + not_evens

    return len(data)


@cache
def blink(num, i):
    if i == 75:
        return 1

    if num == 0:
        return blink(1, i + 1)

    if len(str(num)) % 2 == 0:
        return blink(int(str(num)[: len(str(num)) // 2]), i + 1) + blink(
            int(str(num)[len(str(num)) // 2 :]), i + 1
        )

    return blink(num * 2024, i + 1)


@timing
def part2(data):
    data = list(map(lambda x: int(x), data[0].split(" ")))
    res = 0
    for num in data:
        res += blink(num, 0)

    return res


data = read_data()
print(f"Part 1 result: {part1(data)}")
print(f"Part 2 result: {part2(data)}")
