import re
from itertools import chain

from timing import timing
from read_data import read_data


@timing
def part1(data):
    data = ''.join(list(chain(data)))
    matches = re.findall('mul\\((\\d+,\\d+)\\)', data)
    nums = list(map(lambda x: (int(x.split(',')[0]), int(x.split(',')[1])), matches))
    return sum(list(map(lambda x: x[0] * x[1], nums)))
        

@timing
def part2(data):
    res = 0
    data = ''.join(list(chain(data)))
    skip = False
    matches = re.findall('(mul\\(\\d+,\\d+\\)|do\\(\\)|don\'t\\(\\))', data)
    
    for match in matches:
        if match == 'don\'t()': skip = True
        elif match == 'do()': skip = False
        if(skip): continue
        
        if match.startswith('mul') and skip == False:
            nums = match[match.find('(')+1:match.find(')')].split(',')
            res += int(nums[0]) * int(nums[1])

    return res


data = read_data()
print(f'Part 1 result: {part1(data)}')
print(f'Part 2 result: {part2(data)}')
