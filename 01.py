def read_data():
    file_in_name = "in.txt"
    with open(file_in_name, "r") as file:
        return file.read().splitlines()


def part1():
    data = read_data()
    a = list(map(lambda x: int(x.split("  ")[0]), data))
    b = list(map(lambda x: int(x.split("  ")[1]), data))
    a.sort()
    b.sort()
    c = list(map(lambda x: abs(x[0] - x[1]), zip(a, b)))
    return sum(c)


def part2():
    data = read_data()
    a = list(map(lambda x: int(x.split("  ")[0]), data))
    b = list(map(lambda x: int(x.split("  ")[1]), data))
    c = list(map(lambda x: x * b.count(x), a))
    return sum(c)


print(f"Part 1 result: {part1()}")
print(f"Part 2 result: {part2()}")
