import re
from itertools import combinations
from collections import defaultdict

from timing import timing
from read_data import read_data


@timing
def part1(data):
    d = defaultdict(list)
    antinodes = list(map(lambda x: list(map(lambda _: False, x)), data))

    for line, _ in enumerate(data):
        for item, _ in enumerate(data[line]):
            if re.match("[A-Za-z0-9]", data[line][item]):
                d[data[line][item]].append((line, item))

    for _, val in d.items():
        point_comb = list(combinations(val, 2))

        for point1, point2 in point_comb:
            v = (point2[0] - point1[0], point2[1] - point1[1])
            fst_antinode = (point2[0] + v[0], point2[1] + v[1])
            snd_antinode = (point1[0] - v[0], point1[1] - v[1])

            if (
                fst_antinode[0] >= 0
                and fst_antinode[0] < len(data)
                and fst_antinode[1] >= 0
                and fst_antinode[1] < len(data[fst_antinode[0]])
            ):
                antinodes[fst_antinode[0]][fst_antinode[1]] = True

            if (
                snd_antinode[0] >= 0
                and snd_antinode[0] < len(data)
                and snd_antinode[1] >= 0
                and snd_antinode[1] < len(data[snd_antinode[0]])
            ):
                antinodes[snd_antinode[0]][snd_antinode[1]] = True

    res = 0
    for line in antinodes:
        for item in line:
            if item:
                res += 1

    return res


@timing
def part2(data):
    d = defaultdict(list)
    antinodes = list(
        map(
            lambda x: list(
                map(lambda y: True if re.match("[A-Za-z0-9]", y) else False, x)
            ),
            data,
        )
    )
    for line, _ in enumerate(data):
        for item, _ in enumerate(data[line]):
            if data[line][item] != ".":
                d[data[line][item]].append((line, item))

    for _, val in d.items():
        point_comb = list(combinations(val, 2))
        for point1, point2 in point_comb:
            v = (point2[0] - point1[0], point2[1] - point1[1])

            fst_antinode = (point2[0] + v[0], point2[1] + v[1])
            snd_antinode = (point1[0] - v[0], point1[1] - v[1])

            while (
                fst_antinode[0] >= 0
                and fst_antinode[0] < len(data)
                and fst_antinode[1] >= 0
                and fst_antinode[1] < len(data[fst_antinode[0]])
            ):
                antinodes[fst_antinode[0]][fst_antinode[1]] = True
                fst_antinode = (fst_antinode[0] + v[0], fst_antinode[1] + v[1])

            while (
                snd_antinode[0] >= 0
                and snd_antinode[0] < len(data)
                and snd_antinode[1] >= 0
                and snd_antinode[1] < len(data[snd_antinode[0]])
            ):
                antinodes[snd_antinode[0]][snd_antinode[1]] = True
                snd_antinode = (snd_antinode[0] - v[0], snd_antinode[1] - v[1])

    res = 0
    for line in antinodes:
        for item in line:
            if item:
                res += 1

    return res


data = read_data()
print(f"Part 1 result: {part1(data)}")
print(f"Part 2 result: {part2(data)}")
