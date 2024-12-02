import re

from timing import timing
from read_data import read_data
from itertools import combinations


def diff_max_three(nums):
    for curr, next in zip(nums, nums[1:]):
        if abs(curr - next) > 3:
            return False

    return True


def increasing_or_decreasing(nums):
    return len(nums) == len(set(nums)) and (
        nums == sorted(nums) or nums == sorted(nums, reverse=True)
    )


@timing
def part1(data):
    data = list(map(lambda x: list(map(lambda y: int(y), re.findall("\\d+", x))), data))
    safe_data = list(
        filter(lambda x: increasing_or_decreasing(x) and diff_max_three(x), data)
    )

    return len(safe_data)


@timing
def part2(data):
    data = list(map(lambda x: list(map(lambda y: int(y), re.findall("\\d+", x))), data))
    safe_data = list(
        filter(lambda x: increasing_or_decreasing(x) and diff_max_three(x), data)
    )

    non_safe_data = list(
        filter(lambda x: not increasing_or_decreasing(x) or not diff_max_three(x), data)
    )
    data = list(
        map(
            lambda x: list(map(lambda y: list(y), combinations(x, len(x) - 1))),
            non_safe_data,
        )
    )

    new_save_data = list(
        filter(
            lambda x: len(
                list(
                    filter(
                        lambda y: increasing_or_decreasing(y) and diff_max_three(y), x
                    )
                )
            )
            > 0,
            data,
        )
    )

    return len(safe_data) + len(new_save_data)


data = read_data()
print(f"Part 1 result: {part1(data)}")
print(f"Part 2 result: {part2(data)}")
