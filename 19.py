from frozendict import frozendict
from frozenlist import FrozenList
from collections import defaultdict
from functools import cache

from timing import timing
from read_data import read_data


@cache
def can_be_made(d, towel):
    if towel == "":
        return True

    for item in d[towel[0]]:
        if towel.startswith(item):
            if can_be_made(d, towel[len(item) :]):
                return True

    return False


@cache
def made_ways(d, towel):
    if towel == "":
        return 1

    x = 0
    for item in d[towel[0]]:
        if towel.startswith(item):
            x += made_ways(d, towel[len(item) :])

    return x


@timing
def part1(data):
    tower_patterns = data[0]
    tower_patterns = tower_patterns.split(", ")
    d = defaultdict(list)

    for pattern in tower_patterns:
        d[pattern[0]].append(pattern)

    for key in d.keys():
        d[key] = FrozenList(d[key])
        d[key].freeze()

    d = frozendict(d)
    potential_towels = data[2:]

    res = 0
    for towel in potential_towels:
        if can_be_made(d, towel):
            res += 1

    return res


@timing
def part2(data):
    tower_patterns = data[0]
    tower_patterns = tower_patterns.split(", ")
    d = defaultdict(list)

    for pattern in tower_patterns:
        d[pattern[0]].append(pattern)

    for key in d.keys():
        d[key] = FrozenList(d[key])
        d[key].freeze()

    d = frozendict(d)
    potential_towels = data[2:]

    res = 0
    for towel in potential_towels:
        res += made_ways(d, towel)

    return res


data = read_data()
print(f"Part 1 result: {part1(data)}")
print(f"Part 2 result: {part2(data)}")
