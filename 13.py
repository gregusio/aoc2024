import re
from sympy import Eq, solve, symbols

from timing import timing
from read_data import read_data


def solve_eq(a_nums, b_nums, to_win):
    a, b = symbols("a b")
    eq1 = Eq(a * a_nums[0] + b * b_nums[0], to_win[0])
    eq2 = Eq(a * a_nums[1] + b * b_nums[1], to_win[1])

    sol = solve((eq1, eq2), (a, b))

    return sol[a], sol[b]


@timing
def part1(data):
    res = 0
    for s in zip(data[0::4], data[1::4], data[2::4]):
        a_nums = list(map(lambda x: int(x), re.findall("\\d+", s[0])))
        b_nums = list(map(lambda x: int(x), re.findall("\\d+", s[1])))
        to_win = list(map(lambda x: int(x), re.findall("\\d+", s[2])))

        a, b = solve_eq(a_nums, b_nums, to_win)

        if (
            a.is_real
            and b.is_real
            and a.is_integer
            and b.is_integer
            and a <= 100
            and b <= 100
        ):
            res += a * 3 + b

    return res


@timing
def part2(data):
    res = 0
    for a_data, b_data, win_data in zip(data[0::4], data[1::4], data[2::4]):
        a_nums = list(map(lambda x: int(x), re.findall("\\d+", a_data)))
        b_nums = list(map(lambda x: int(x), re.findall("\\d+", b_data)))
        to_win = list(
            map(lambda x: int(x) + 10000000000000, re.findall("\\d+", win_data))
        )

        a, b = solve_eq(a_nums, b_nums, to_win)

        if a.is_real and b.is_real and a.is_integer and b.is_integer:
            res += a * 3 + b

    return res


data = read_data()
print(f"Part 1 result: {part1(data)}")
print(f"Part 2 result: {part2(data)}")
