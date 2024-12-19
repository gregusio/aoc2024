from timing import timing
from read_data import read_data


@timing
def part1(data):
    array = list(map(lambda x: list(x), data[:data.index('')]))
    moves = data[data.index('')+1:]
    moves = ''.join(moves)
    curr_x = 0
    curr_y = 0
    for i, _ in enumerate(array):
        for j, _ in enumerate(array[i]):
            if array[i][j] == '@':
                curr_x = i
                curr_y = j

    for move in moves:
        if move == '^' and array[curr_x - 1][curr_y] == '#':
            continue
        if move == '^' and array[curr_x - 1][curr_y] == '.':
            array[curr_x][curr_y] = '.'
            curr_x -= 1
            array[curr_x][curr_y] = '@'
            continue
        if move == '^' and array[curr_x - 1][curr_y] == 'O':
            i = curr_x - 1
            not_move = False
            while i >= 0:
                if array[i][curr_y] == 'O':
                    i -= 1
                    continue
                elif array[i][curr_y] == '.':
                    break
                elif array[i][curr_y] == '#':
                    not_move = True
                    break
            
            if not_move: continue
            while i < curr_x:
                array[i][curr_y] = 'O'
                i += 1
            
            array[curr_x][curr_y] = '.'
            curr_x -= 1
            array[curr_x][curr_y] = '@'
        
        if move == '>' and array[curr_x][curr_y + 1] == '#':
            continue
        if move == '>' and array[curr_x][curr_y+1] == '.':
            array[curr_x][curr_y] = '.'
            curr_y += 1
            array[curr_x][curr_y] = '@'
            continue
        if move == '>' and array[curr_x][curr_y+1] == 'O':
            not_move = False
            i = curr_y + 1
            while i < len(array[curr_x]):
                if array[curr_x][i] == 'O':
                    i += 1
                    continue
                elif array[curr_x][i] == '.':
                    break
                elif array[curr_x][i] == '#':
                    not_move = True
                    break
            
            if not_move: continue
            while i > curr_y:
                array[curr_x][i] = 'O'
                i -= 1
            
            array[curr_x][curr_y] = '.'
            curr_y += 1
            array[curr_x][curr_y] = '@'

    
        if move == 'v' and array[curr_x + 1][curr_y] == '#':
            continue
        if move == 'v' and array[curr_x + 1][curr_y] == '.':
            array[curr_x][curr_y] = '.'
            curr_x += 1
            array[curr_x][curr_y] = '@'
            continue
        if move == 'v' and array[curr_x + 1][curr_y] == 'O':
            i = curr_x + 1
            not_move = False
            while i < len(array):
                if array[i][curr_y] == 'O':
                    i += 1
                    continue
                elif array[i][curr_y] == '.':
                    break
                elif array[i][curr_y] == '#':
                    not_move = True
                    break
            
            if not_move: continue
            while i > curr_x:
                array[i][curr_y] = 'O'
                i -= 1 
            array[curr_x][curr_y] = '.'
            curr_x += 1
            array[curr_x][curr_y] = '@'

        if move == '<' and array[curr_x][curr_y - 1] == '#':
            continue
        if move == '<' and array[curr_x][curr_y-1] == '.':
            array[curr_x][curr_y] = '.'
            curr_y -= 1
            array[curr_x][curr_y] = '@'
            continue
        if move == '<' and array[curr_x][curr_y-1] == 'O':
            i = curr_y - 1
            not_move = False
            while i >= 0:
                if array[curr_x][i] == 'O':
                    i -= 1
                    continue
                elif array[curr_x][i] == '.':
                    break
                elif array[curr_x][i] == '#':
                    not_move = True
                    break
            
            if not_move: continue
            while i < curr_y:
                array[curr_x][i] = 'O'
                i += 1

            array[curr_x][curr_y] = '.'
            curr_y -= 1
            array[curr_x][curr_y] = '@'
            
    res = 0
    for i, _ in enumerate(array):
        for j, _ in enumerate(array[i]):
            if array[i][j] == 'O':
                res += 100*i + j

    return res

def check_up(array, i, j, p, q):
    if array[i-1][j] == '.' and array[p-1][q] == '.':
        return True
    
    if array[i-1][j] == '#' or array[p-1][q] == '#':
        return False
    
    c1, c2, c3 = True, True, True
    if array[i-1][j] == '[':
        c1 = check_up(array, i-1, j, p-1, q)
    if array[i-1][j] == ']':
        c2 = check_up(array, i-1, j-1, p-1, q-1)
    if array[p-1][q] == '[':
        c3 = check_up(array, i-1, j+1, p-1, q+1)

    return c1 and c2 and c3
     
def move_up(array, i, j, p, q):
    if array[i-1][j] == '[':
        move_up(array, i-1, j, p-1, q)
        
    if array[i-1][j] == ']':
        move_up(array, i-1, j-1, p-1, q-1)
        
    if array[p-1][q] == '[':
        move_up(array, i-1, j+1, p-1, q+1)
        
    if array[i-1][j] == '.' and array[p-1][q] == '.':
        array[i][j] = '.'
        array[p][q] = '.'
        array[i-1][j] = '['
        array[p-1][q] = ']'
        return


def check_down(array, i, j, p, q):
    if array[i+1][j] == '.' and array[p+1][q] == '.':
        return True
    
    if array[i+1][j] == '#' or array[p+1][q] == '#':
        return False
    
    c1, c2, c3 = True, True, True
    if array[i+1][j] == '[':
        c1 = check_down(array, i+1, j, p+1, q)
    if array[i+1][j] == ']':
        c2 = check_down(array, i+1, j-1, p+1, q-1)
    if array[p+1][q] == '[':
        c3 = check_down(array, i+1, j+1, p+1, q+1)

    return c1 and c2 and c3
     
def move_down(array, i, j, p, q):
    if array[i+1][j] == '[':
        move_down(array, i+1, j, p+1, q)
        
    if array[i+1][j] == ']':
        move_down(array, i+1, j-1, p+1, q-1)
        
    if array[p+1][q] == '[':
        move_down(array, i+1, j+1, p+1, q+1)
        
    if array[i+1][j] == '.' and array[p+1][q] == '.':
        array[i][j] = '.'
        array[p][q] = '.'
        array[i+1][j] = '['
        array[p+1][q] = ']'
        return


@timing
def part2(data):
    array = []
    for line in data[:data.index('')]:
        a = []
        for item in line:
            if item == '#':
                a.append('#')
                a.append('#')
            if item == '.':
                a.append('.')
                a.append('.')
            if item == 'O':
                a.append('[')
                a.append(']')
            if item == '@':
                a.append('@')
                a.append('.')
        
        array.append(a)

    moves = data[data.index('')+1:]
    moves = ''.join(moves)
    curr_x = 0
    curr_y = 0
    for i, _ in enumerate(array):
        for j, _ in enumerate(array[i]):
            if array[i][j] == '@':
                curr_x = i
                curr_y = j
    
    for move in moves:
        f = open('xd.txt', 'w')
        for line in array:
            f.write(''.join(line))
            f.write('\n')
        f.close()
        if move == '^' and array[curr_x - 1][curr_y] == '#':
            continue
        if move == '^' and array[curr_x - 1][curr_y] == '.':
            array[curr_x][curr_y] = '.'
            curr_x -= 1
            array[curr_x][curr_y] = '@'
            continue
        if move == '^' and (array[curr_x - 1][curr_y] == '[' or array[curr_x - 1][curr_y] == ']'):
            not_move = False
            if array[curr_x - 1][curr_y] == '[':
                not_move = check_up(array, curr_x-1, curr_y, curr_x-1, curr_y+1)
            elif array[curr_x - 1][curr_y] == ']':
                not_move = check_up(array, curr_x-1, curr_y-1, curr_x-1, curr_y)
            
            
            if not not_move: continue
            else:
                if array[curr_x - 1][curr_y] == '[':
                    move_up(array, curr_x-1, curr_y, curr_x-1, curr_y+1)
                elif array[curr_x - 1][curr_y] == ']':
                    move_up(array, curr_x-1, curr_y-1, curr_x-1, curr_y)

                array[curr_x][curr_y] = '.'
                curr_x -= 1
                array[curr_x][curr_y] = '@'
        
        if move == '>' and array[curr_x][curr_y + 1] == '#':
            continue
        if move == '>' and array[curr_x][curr_y+1] == '.':
            array[curr_x][curr_y] = '.'
            curr_y += 1
            array[curr_x][curr_y] = '@'
            continue
        if move == '>' and array[curr_x][curr_y+1] == '[':
            not_move = False
            i = curr_y + 1
            while i < len(array[curr_x]):
                if array[curr_x][i] == '[' or array[curr_x][i] == ']':
                    i += 1
                    continue
                elif array[curr_x][i] == '.':
                    break
                elif array[curr_x][i] == '#':
                    not_move = True
                    break
            
            if not_move: continue
            while i > curr_y:
                array[curr_x][i] = ']'
                i -= 1
                array[curr_x][i] = '['
                i -=1
            
            array[curr_x][curr_y] = '.'
            curr_y += 1
            array[curr_x][curr_y] = '@'

    
        if move == 'v' and array[curr_x + 1][curr_y] == '#':
            continue
        if move == 'v' and array[curr_x + 1][curr_y] == '.':
            array[curr_x][curr_y] = '.'
            curr_x += 1
            array[curr_x][curr_y] = '@'
            continue
        if move == 'v' and (array[curr_x + 1][curr_y] == '[' or array[curr_x + 1][curr_y] == ']'):
            not_move = False
            if array[curr_x + 1][curr_y] == '[':
                not_move = check_down(array, curr_x+1, curr_y, curr_x+1, curr_y+1)
            elif array[curr_x + 1][curr_y] == ']':
                not_move = check_down(array, curr_x+1, curr_y-1, curr_x+1, curr_y)
            
            if not not_move: continue
            else:
                if array[curr_x + 1][curr_y] == '[':
                    move_down(array, curr_x+1, curr_y, curr_x+1, curr_y+1)
                elif array[curr_x + 1][curr_y] == ']':
                    move_down(array, curr_x+1, curr_y-1, curr_x+1, curr_y)

                array[curr_x][curr_y] = '.'
                curr_x += 1
                array[curr_x][curr_y] = '@'

        if move == '<' and array[curr_x][curr_y - 1] == '#':
            continue
        if move == '<' and array[curr_x][curr_y-1] == '.':
            array[curr_x][curr_y] = '.'
            curr_y -= 1
            array[curr_x][curr_y] = '@'
            continue
        if move == '<' and array[curr_x][curr_y-1] == ']':
            i = curr_y - 1
            not_move = False
            while i >= 0:
                if array[curr_x][i] == '[' or array[curr_x][i] == ']':
                    i -= 1
                    continue
                elif array[curr_x][i] == '.':
                    break
                elif array[curr_x][i] == '#':
                    not_move = True
                    break
            
            if not_move: continue
            while i < curr_y:
                array[curr_x][i] = '['
                i += 1
                array[curr_x][i] = ']'
                i += 1

            array[curr_x][curr_y] = '.'
            curr_y -= 1
            array[curr_x][curr_y] = '@'

    res = 0
    for i, _ in enumerate(array):
        for j, _ in enumerate(array[i]):
            if array[i][j] == '[':
                res += 100*i + j

    return res


data = read_data()
print(f'Part 1 result: {part1(data)}')
print(f'Part 2 result: {part2(data)}')
