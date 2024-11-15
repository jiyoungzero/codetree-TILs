n = int(input())
dots = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0

def is_valid(sel):
    prev_x, prev_y = 0, 0 
    for x, y in sel:
        if x == prev_x or y == prev_y:
            prev_x, prev_y = x, y
            continue 
        else:
            return False 
    if prev_x == 0 or prev_y == 0:
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