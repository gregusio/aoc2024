import re

from timing import timing
from read_data import read_data


def check_mult_add(nums, index, curr, res):
    if index >= len(nums) and curr == res:
        return True

    if curr > res or index >= len(nums):
        return False

    num = nums[index]
    for operation in ["mult", "add"]:
        tmp = curr
        if operation == "mult":
            tmp *= num
        elif operation == "add":
            tmp += num

        if check_mult_add(nums, index + 1, tmp, res):
            return True


def check_conc_mult_add(nums, index, curr, res):
    if index >= len(nums) and curr == res:
        return True

    if curr > res or index >= len(nums):
        return False

    num = nums[index]
    for operation in ["conc", "mult", "add"]:
        tmp = curr
        if operation == "conc":
            tmp *= 10 ** len(str(num))
            tmp += num
        elif operation == "mult":
            tmp *= num
        elif operation == "add":
            tmp += num

        if check_conc_mult_add(nums, index + 1, tmp, res):
            return True


@timing
def part1(data):
    res = 0
    for line in data:
        nums = list(map(lambda x: int(x), re.findall("\\d+", line)))
        expected_res = nums[0]
        first = nums[1]
        if check_mult_add(tuple(nums[2:]), 0, first, expected_res):
            res += expected_res

    return res


@timing
def part2(data):
    res = 0
    for line in data:
        nums = list(map(lambda x: int(x), re.findall("\\d+", line)))
        expected_res = nums[0]
        first = nums[1]
        if check_conc_mult_add(tuple(nums[2:]), 0, first, expected_res):
            res += expected_res

    return res


data = read_data()
print(f"Part 1 result: {part1(data)}")
print(f"Part 2 result: {part2(data)}")
