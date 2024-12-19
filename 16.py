import sys
from collections import defaultdict

from timing import timing
from read_data import read_data


def okay_dir(dir, new_dir):
    if dir == 'U' and new_dir == 'D':
        return False
    if dir == 'R' and new_dir == 'L':
        return False
    if dir == 'D' and new_dir == 'U':
        return False
    if dir == 'L' and new_dir == 'R':
        return False

    return True


def get_dir(i, j, p, q):
    if i > p: return 'U'
    if i < p: return 'D'
    if j > q: return 'L'
    if j < q: return 'R'


def get_dist(i, j, p, q):
    return abs(i - p) + abs(j - q)


def find_min(dist, visited):
    curr = sys.maxsize
    res = 0
    for key, val in dist.items():
        if val[0] < curr and visited[key] == False:
            curr = val[0]
            res = key

    return res
    

def dijkstra(graph: dict, src: tuple, n, m):
    dist = {key:[sys.maxsize, None] for key in graph}
    dist[src][0] = 0
    dist[src][1] = 'R'
    visited = {key:False for key in graph}

    for _ in range(len(graph.keys())):
        u = find_min(dist, visited)
        dir = dist[u][1]
        visited[u] = True

        for v in graph[u]:
            new_dir = get_dir(*u, *v)
            if dir == new_dir:
                if visited[v] == False and dist[v][0] > dist[u][0] + get_dist(*u, *v):
                    dist[v][0] = dist[u][0] + get_dist(*u, *v)
                    dist[v][1] = new_dir
            else:
                if visited[v] == False and dist[v][0] > dist[u][0] + 1000 + get_dist(*u, *v):
                    dist[v][0] = dist[u][0] + 1000 + get_dist(*u, *v)
                    dist[v][1] = new_dir

    return dist[(1, m-2)][0]


def dijkstra_path(graph: dict, src: tuple, n, m):
    dist = {key:[sys.maxsize, None] for key in graph}
    prev = {key:[] for key in graph}
    dist[src][0] = 0
    dist[src][1] = 'R'
    visited = {key:False for key in graph}

    for _ in range(len(graph.keys())):
        u = find_min(dist, visited)
        dir = dist[u][1]
        visited[u] = True

        for v in graph[u]:
            new_dir = get_dir(*u, *v)
            if dir == new_dir:
                if visited[v] == False and dist[v][0] > dist[u][0] + get_dist(*u, *v):
                    dist[v][0] = dist[u][0] + get_dist(*u, *v)
                    dist[v][1] = new_dir
                    prev[v] = []
                    prev[v].append(u)
                if visited[v] == False and dist[v][0] == dist[u][0] + get_dist(*u, *v):
                    prev[v].append(u)
            else:
                if visited[v] == False and dist[v][0] > dist[u][0] + 1000 + get_dist(*u, *v):
                    dist[v][0] = dist[u][0] + 1000 + get_dist(*u, *v)
                    dist[v][1] = new_dir
                    prev[v] = []
                    prev[v].append(u)
                if visited[v] == False and dist[v][0] == dist[u][0] + 1000 + get_dist(*u, *v):
                    prev[v].append(u)

    return prev


@timing
def part1(data):
    graph = defaultdict(list)
    start = 0
    for i, _ in enumerate(data):
        for j, _ in enumerate(data[i]):
            if data[i][j] == '#': continue
            if data[i][j] == 'S': start = (i, j)

            if data[i-1][j] != '#' and (data[i][j-1] != '#' or data[i][j+1] != '#')\
            or data[i-1][j] != '#' and (data[i][j-1] == '#' and data[i][j+1] == '#') and data[i+1][j] == '#':
                k = i - 1
                while k >= 0 and data[k][j] != '#':
                    if data[k][j-1] != '#' or data[k][j+1] != '#' or data[k-1][j] == '#':
                        graph[(i, j)].append((k, j))
                    k -= 1
                    
            if data[i][j+1] != '#' and (data[i+1][j] != '#' or data[i-1][j] != '#')\
            or data[i][j+1] != '#' and (data[i+1][j] == '#' and data[i-1][j] == '#') and data[i][j-1] == '#':
                k = j + 1
                while k < len(data[i]) and data[i][k] != '#':
                    if data[i-1][k] != '#' or data[i+1][k] != '#' or data[i][k+1] == '#':
                        graph[(i, j)].append((i, k))
                    k += 1
                    
            if data[i+1][j] != '#' and (data[i][j-1] != '#' or data[i][j+1] != '#')\
            or data[i+1][j] != '#' and (data[i][j-1] == '#' and data[i][j+1] == '#') and data[i-1][j] == '#':
                k = i + 1
                while k < len(data) and data[k][j] != '#':
                    if data[k][j-1] != '#' or data[k][j+1] != '#' or data[k+1][j] == '#':
                        graph[(i, j)].append((k, j))
                    k += 1

            if data[i][j-1] != '#' and (data[i+1][j] != '#' or data[i-1][j] != '#')\
            or data[i][j-1] != '#' and (data[i+1][j] == '#' and data[i-1][j] == '#') and data[i][j+1] == '#':
                k = j - 1
                while k >= 0 and data[i][k] != '#':
                    if data[i-1][k] != '#' or data[i+1][k] != '#' or data[i][k-1] == '#':
                        graph[(i, j)].append((i, k))
                    k -= 1

    return dijkstra(graph, start, len(data), len(data[0]))


@timing
def part2(data):
    graph = defaultdict(list)
    start = 0
    for i, _ in enumerate(data):
        for j, _ in enumerate(data[i]):
            if data[i][j] == '#': continue
            if data[i][j] == 'S': start = (i, j)

            if data[i-1][j] != '#' and (data[i][j-1] != '#' or data[i][j+1] != '#')\
            or data[i-1][j] != '#' and (data[i][j-1] == '#' and data[i][j+1] == '#') and data[i+1][j] == '#':
                k = i - 1
                while k >= 0 and data[k][j] != '#':
                    if data[k][j-1] != '#' or data[k][j+1] != '#' or data[k-1][j] == '#':
                        graph[(i, j)].append((k, j))
                    k -= 1
                
            if data[i][j+1] != '#' and (data[i+1][j] != '#' or data[i-1][j] != '#')\
            or data[i][j+1] != '#' and (data[i+1][j] == '#' and data[i-1][j] == '#') and data[i][j-1] == '#':
                k = j + 1
                while k < len(data[i]) and data[i][k] != '#':
                    if data[i-1][k] != '#' or data[i+1][k] != '#' or data[i][k+1] == '#':
                        graph[(i, j)].append((i, k))
                    k += 1
                    
            if data[i+1][j] != '#' and (data[i][j-1] != '#' or data[i][j+1] != '#')\
            or data[i+1][j] != '#' and (data[i][j-1] == '#' and data[i][j+1] == '#') and data[i-1][j] == '#':
                k = i + 1
                while k < len(data) and data[k][j] != '#':
                    if data[k][j-1] != '#' or data[k][j+1] != '#' or data[k+1][j] == '#':
                        graph[(i, j)].append((k, j))
                    k += 1
                
            if data[i][j-1] != '#' and (data[i+1][j] != '#' or data[i-1][j] != '#')\
            or data[i][j-1] != '#' and (data[i+1][j] == '#' and data[i-1][j] == '#') and data[i][j+1] == '#':
                k = j - 1
                while k >= 0 and data[i][k] != '#':
                    if data[i-1][k] != '#' or data[i+1][k] != '#' or data[i][k-1] == '#':
                        graph[(i, j)].append((i, k))
                    k -= 1

    visited = defaultdict(bool)
    prev =  dijkstra_path(graph, start, len(data), len(data[0]))
    check = [[False for _ in range(len(data[i]))] for i in range(len(data))]
    curr = (1, len(data[1]) - 2)
    queue = []
    for x in prev[curr]:
        queue.append((curr, x))

    visited[curr] = True

    while queue:
        start, stop = queue.pop(0)
        if visited[stop] == False:
            for s in prev[stop]:
                queue.append((stop, s))
            visited[stop] = True

        if start[0] == stop[0]:
            if start[1] < stop[1]:
                for i in range(start[1], stop[1]+1):
                    check[start[0]][i] = True
            else:
                for i in range(start[1], stop[1]-1, -1):
                    check[start[0]][i] = True
        elif start[1] == stop[1]:
            if start[0] < stop[0]:
                for i in range(start[0], stop[0]+1):
                    check[i][start[1]] = True
            else:
                for i in range(start[0], stop[0]-1, -1):
                    check[i][start[1]] = True

    res = 0
    for i in check:
        for j in i:
            if j:
                res += 1

    return res


data = read_data()
print(f'Part 1 result: {part1(data)}')
print(f'Part 2 result: {part2(data)}')
