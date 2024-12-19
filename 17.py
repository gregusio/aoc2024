import re
import sys
from collections import defaultdict

from timing import timing
from read_data import read_data


def combo(operand, a, b, c):
    if operand >= 0 and operand <= 3:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c


@timing
def part1(data):
    a = int(re.findall("\\d+", data[0])[0])
    b = int(re.findall("\\d+", data[1])[0])
    c = int(re.findall("\\d+", data[2])[0])

    nums = list(map(lambda x: int(x), re.findall("\\d+", data[4])))
    res = []
    ins = 0

    while ins < len(nums):
        opcode = nums[ins]
        operand = nums[ins + 1]

        if opcode == 0:
            a //= 2 ** combo(operand, a, b, c)
            ins += 2
        elif opcode == 1:
            b ^= operand
            ins += 2
        elif opcode == 2:
            b = combo(operand, a, b, c) % 8
            ins += 2
        elif opcode == 3:
            if a != 0:
                ins = operand
            else:
                ins += 2
        elif opcode == 4:
            b ^= c
            ins += 2
        elif opcode == 5:
            res.append(combo(operand, a, b, c) % 8)
            ins += 2
        elif opcode == 6:
            b = a // 2 ** combo(operand, a, b, c)
            ins += 2
        elif opcode == 7:
            c = a // 2 ** combo(operand, a, b, c)
            ins += 2

    return ",".join(map(str, res))


@timing
def part2(data):
    nums = list(map(lambda x: int(x), re.findall("\\d+", data[4])))
    i = len(nums) - 1
    x = 0
    v = defaultdict(bool)
    d = defaultdict(list)
    check = True
    lowest = sys.maxsize
    while check:
        if i == -1:
            i += 1
            if x != -1:
                d[i] = []
                if x < lowest:
                    lowest = x

            while not d[i] and i < len(nums):
                i += 1

            continue

        if d[i]:
            x = d[i].pop(0)
            i -= 1
        elif not d[i] and x != -1:
            s = nums[i]
            for a in range(8 * x, 8 * (x + 1)):

                try:
                    if ((((a % 8) ^ 5) ^ 6) ^ (a // (2 ** ((a % 8) ^ 5)))) % 8 == s:
                        d[i].append(a)

                except:
                    # print('X')
                    pass
            if d[i]:
                x = d[i].pop()
                i -= 1
            else:
                x = -1
        elif x == -1:
            i += 1

        if len(d) < len(nums):
            continue
        check = any(list(map(lambda x: True if d[x] else False, d.keys())))

    return lowest


data = read_data()
print(f"Part 1 result: {part1(data)}")
print(f"Part 2 result: {part2(data)}")
