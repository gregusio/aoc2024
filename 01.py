from timing import timing
from read_data import read_data


@timing
def part1(data):
    a = list(map(lambda x: int(x.split("  ")[0]), data))
    b = list(map(lambda x: int(x.split("  ")[1]), data))
    a.sort()
    b.sort()
    c = list(map(lambda x: abs(x[0] - x[1]), zip(a, b)))
    return sum(c)


@timing
def part2(data):
    a = list(map(lambda x: int(x.split("  ")[0]), data))
    b = list(map(lambda x: int(x.split("  ")[1]), data))
    c = list(map(lambda x: x * b.count(x), a))
    return sum(c)


data = read_data()
print(f"Part 1 result: {part1(data)}")
print(f"Part 2 result: {part2(data)}")
