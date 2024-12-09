from timing import timing
from read_data import read_data


@timing
def part1(data):
    res = 0
    data = list(map(lambda x: int(x), data[0]))
    index = 0
    item_index = 0
    num_of_data = sum(data[::2])
    curr_last_item = len(data) // 2
    j = len(data) - 1

    for i, item in enumerate(data):
        if index >= num_of_data:
            break

        if i % 2 == 0:
            while item > 0:
                res += item_index * index
                index += 1
                item -= 1
            item_index += 1
        else:
            c = data[j]
            if c > item:
                while item > 0:
                    res += index * curr_last_item
                    index += 1
                    item -= 1
                    data[j] -= 1
            else:
                while item > 0:
                    while c > 0 and item > 0:
                        res += index * curr_last_item
                        index += 1
                        c -= 1
                        item -= 1
                        data[j] -= 1

                    if item > 0 or c == 0:
                        j -= 2
                        c = data[j]
                        curr_last_item -= 1

    return res


@timing
def part2(data):
    res = 0
    data = list(map(lambda x: int(x), data[0]))
    data = [(x, i // 2) if i % 2 == 0 else (x, ".") for i, x in enumerate(data)]

    for i, block in enumerate(data[::-2]):
        bigger_spaces = list(
            filter(lambda x: x[0] >= block[0], data[1 : data.index(block) : 2])
        )
        if bigger_spaces:
            first_space = bigger_spaces[0]
            index = data.index(first_space)
            data[index] = (data[index][0] - block[0], data[index][1])
            data.insert(index, block)
            data.insert(index, (0, "."))

            new_index = data[index + 2 :].index(block) + index + 2

            data.reverse()
            data.remove(block)
            data.reverse()

            if new_index == len(data):
                data = data[:-1]
            else:
                data[new_index - 1] = (
                    data[new_index - 1][0] + data[new_index][0] + block[0],
                    ".",
                )
                data[new_index] = "to_remove"
                data.remove("to_remove")

    index = 0
    for i, j in data:
        if j != ".":
            while i > 0:
                res += index * j
                index += 1
                i -= 1
        else:
            while i > 0:
                index += 1
                i -= 1

    return res


data = read_data()
print(f"Part 1 result: {part1(data)}")
print(f"Part 2 result: {part2(data)}")
