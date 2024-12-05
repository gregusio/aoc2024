from collections import defaultdict 
from functools import cmp_to_key 
from timing import timing
from read_data import read_data


def get_sorted_and_not(data):
    rules = data[: data.index('')]
    in_lines = data[data.index('') + 1 :]
    d = defaultdict(list)
    for rule in rules:
        a, b = int(rule.split('|')[0]), int(rule.split('|')[1])
        d[a].append((b, 'after'))
        d[b].append((a, 'before'))

    sorted_nums = []
    not_sorted_nums = []
    for line in in_lines:
        is_sorted = True
        nums = list(map(lambda x: int(x), line.split(',')))
        for i, num in enumerate(nums):
            if is_sorted == False:
                break

            for j in range(i):
                if (num, 'before') in d.get(nums[j]):
                    is_sorted = False

            for j in range(1, len(nums) - i):
                if (num, 'after') in d.get(nums[i + j]):
                    is_sorted = False

        if is_sorted:
            sorted_nums.append(nums)
        else:
            not_sorted_nums.append(nums)

    return sorted_nums, not_sorted_nums, d


@timing
def part1(data):
    sorted_nums, _, _ = get_sorted_and_not(data)

    return sum(list(map(lambda x: x[len(x) // 2], sorted_nums)))


@timing
def part2(data):
    _, not_sorted_nums, d = get_sorted_and_not(data)
    
    for nums in not_sorted_nums:
        nums.sort(key=cmp_to_key(lambda x, y: -1 if (x, 'before') in d[y] else 1))

    return sum(list(map(lambda x: x[len(x) // 2], not_sorted_nums)))


data = read_data()
print(f"Part 1 result: {part1(data)}")
print(f"Part 2 result: {part2(data)}")
