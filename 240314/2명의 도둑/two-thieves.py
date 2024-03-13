import sys
input = sys.stdin.readline 

n, m, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
max_val = 0
a = []

def possible(sx1, sy1, sx2, sy2):    
    if sy1+m-1 >= n or sy2+m-1 >= n:
        return False
    if sx1 != sx2:
        return True

    if sy1+m-1 >= sy2 or sy2+m-1 >= sy1:
        return False
    return True

def find_max_val(cur_idx, cur_weight, cur_val):
    global max_val
    if cur_idx == m:
        if cur_weight <= c:
            max_val = max(cur_val, max_val)
        return 
    
    cur_weight += a[cur_idx]
    cur_val += a[cur_idx]**2
    find_max_val(cur_idx + 1, cur_weight,cur_val)
    cur_weight -= a[cur_idx]
    cur_val -= a[cur_idx]**2

    find_max_val(cur_idx+1, cur_weight, cur_val)

def get_max(x, y):
    global max_val, a
    max_val = 0
    a = arr[x][y:y+m]
    find_max_val(0, 0, 0)
    return max_val


for sx1 in range(n):
    for sy1 in range(n):
        for sx2 in range(n):
            for sy2 in range(n):
                if possible(sx1, sy1, sx2, sy2):
                    answer = max(answer, get_max(sx1, sy1)+get_max(sx2, sy2))
print(answer)