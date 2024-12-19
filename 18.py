import re
import sys
from collections import defaultdict

from timing import timing
from read_data import read_data

sys.setrecursionlimit(4000)


def find_min(dist, visited):
    curr = sys.maxsize
    res = 0
    for key, val in dist.items():
        if val < curr and visited[key] == False:
            curr = val
            res = key

    return res


def dijkstra(graph, src):
    dist = {key: sys.maxsize for key in graph}
    dist[src] = 0
    visited = {key: False for key in graph}

    for _ in range(len(graph.keys())):
        u = find_min(dist, visited)
        visited[u] = True

        for v in graph[u]:
            if visited[v] == False and dist[v] > dist[u] + 1:
                dist[v] = dist[u] + 1

    return dist[(70, 70)]


def construct_graph(array):
    graph = defaultdict(list)

    for i, _ in enumerate(array):
        for j, _ in enumerate(array[i]):
            if j + 1 < len(array[i]) and array[i][j + 1] != "#":
                graph[(i, j)].append((i, j + 1))
            if i - 1 >= 0 and array[i - 1][j] != "#":
                graph[(i, j)].append((i - 1, j))
            if i + 1 < len(array) and array[i + 1][j] != "#":
                graph[(i, j)].append((i + 1, j))
            if j - 1 >= 0 and array[i][j - 1] != "#":
                graph[(i, j)].append((i, j - 1))

    return graph


@timing
def part1(data):
    array = [["." for _ in range(71)] for _ in range(71)]
    i = 1
    for line in data:
        nums = re.findall("\\d+", line)
        array[int(nums[0])][int(nums[1])] = "#"
        if i == 1024:
            break
        i += 1

    graph = construct_graph(array)

    return dijkstra(graph, (0, 0))


def dfs(graph, visited, s):
    visited[s] = True

    for i in graph[s]:
        if not visited[i]:
            dfs(graph, visited, i)


@timing
def part2(data):
    array = [["." for _ in range(71)] for _ in range(71)]
    i = 1
    for line in data:
        nums = re.findall("\\d+", line)
        array[int(nums[0])][int(nums[1])] = "#"
        if i == 1024:
            break
        i += 1

    graph = construct_graph(array)

    res = 0
    for line in data[1024:]:
        nums = re.findall("\\d+", line)
        i = int(nums[0])
        j = int(nums[1])

        if array[i][j] == "#":
            continue
        array[i][j] = "#"

        del graph[(i, j)]
        if i - 1 >= 0 and (i, j) in graph[(i - 1, j)]:
            graph[(i - 1, j)].remove((i, j))
        if i + 1 < len(array) and (i, j) in graph[(i + 1, j)]:
            graph[(i + 1, j)].remove((i, j))
        if j - 1 >= 0 and (i, j) in graph[(i, j - 1)]:
            graph[(i, j - 1)].remove((i, j))
        if j + 1 < len(array[i]) and (i, j) in graph[(i, j + 1)]:
            graph[(i, j + 1)].remove((i, j))

        visited = {key: False for key in graph}
        dfs(graph, visited, (0, 0))

        if visited[(70, 70)] == False:
            res = line
            break

    return res


data = read_data()
print(f"Part 1 result: {part1(data)}")
print(f"Part 2 result: {part2(data)}")
