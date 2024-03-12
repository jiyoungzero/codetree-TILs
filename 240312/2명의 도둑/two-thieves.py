import sys
input = sys.stdin.readline 
from itertools import combinations_with_replacement

n, m, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)] 
row_lst = list(combinations_with_replacement([i for i in range(n)], 2))
a = []
max_val = 0
answer = 0

def intersect(a, b, c, d):
    # 겹치지 않을 경우를 계산하여 그 결과를 반전시켜 반환합니다.
    return not (b < c or d < a)


# 두 도둑의 위치가 올바른지 판단합니다.
def possible(sx1, sy1, sx2, sy2):
    # 두 도둑이 훔치려는 물건의 범위가
    # 격자를 벗어나는 경우에는 불가능합니다.
    if sy1 + m - 1 >= n or sy2 + m - 1 >= n:
        return False
    
    # 두 도둑이 훔칠 위치의 행이 다르다면
    # 겹칠 수가 없으므로 무조건 가능합니다.
    if sx1 != sx2:
        return True
    
    # 두 구간끼리 겹친다면
    # 불가능합니다.
    if intersect(sy1, sy1 + m - 1, sy2, sy2 + m - 1):
        return False
    
    # 행이 같으면서 구간끼리 겹치지 않으면
    # 가능합니다.
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


def find_max(x, y):
    global a, max_val

    a = arr[x][y:y+m]
    max_val = 0
    find_max_val(0,0,0)
    return max_val
    

for sx1 in range(n):
    for sy1 in range(n):
        for sx2 in range(n):
            for sy2 in range(n):
                if possible(sx1, sy1, sx2, sy2):
                    # (sx1, sy1) ~ (sx1, sy1+m-1)
                    # (sx2, sy2) ~ (sx2, sy2+m-1))
                    answer = max(answer, find_max(sx1, sy1)+find_max(sx2, sy2))

print(answer)