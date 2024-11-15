n = int(input())
dots = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0
def is_hori_or_verti(x, y, px, py):
    if x == px and y != py:
        if y < py:
            return 'down_vertical'
        else:
            return 'up_vertical'
    else:
        if x < px:
            return 'right_horizon'
        else:
            return 'left_horizon'

def is_valid(sel):
    prev_x, prev_y = 0, 0 
    prev_dir = 'None'
    for idx, (x, y) in enumerate(sel):
        if x == prev_x or y == prev_y:
            if prev_dir == 'None':
                prev_dir = is_hori_or_verti(x, y, prev_x, prev_y)
                prev_x, prev_y = x, y
                continue
            else:
                cur_dir = is_hori_or_verti(x, y, prev_x, prev_y)
                if prev_dir == cur_dir:
                    return False
                else:
                    prev_dir = cur_dir
                    prev_x, prev_y = x, y
                    continue 
        else:
            return False 
    cur_dir = is_hori_or_verti(0, 0, sel[-1][0], sel[-1][1])
    if (prev_x == 0 or prev_y == 0) and (prev_dir != cur_dir):
        # print(prev_dir)
        # print(sel)
        return True
    else:
        return False

def my_itertools(visited, sel):
    global answer
    if len(sel) == n:
        if is_valid(sel):
            answer += 1
        return 
    
    for i in range(n):
        if i in visited:continue
        visited.append(i)
        my_itertools(visited, sel+[dots[i]])
        visited.pop()
        # my_itertools(visited, sel)
    
my_itertools([], [])
print(answer)