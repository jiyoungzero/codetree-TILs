# abs(nx-x)+abs(ny-y) <= k

import sys
input = sys.stdin.readline 

GOLD = 1
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y <= n

def in_square(nx, ny, x, y, k):
    if abs(nx-x)+abs(ny-y) <= k:
        return True
    else:
        return False

def get_find_cost(k):
    return k*k+(k+1)*(k+1)

def get_gold_value(k, i, j):
    visited = [[False]*n for _ in range(n)]
    result = 0
    for row in range(n):
        for col in range(n):
            if in_square(row, col, i, j, k):
                if not visited[row][col]:
                    visited[row][col] = True
                    if arr[row][col] == GOLD:
                        result += m 
    return result


for i in range(n):
    for j in range(n):
        for size in range(n+1):
            gold_value = get_gold_value(size, i, j) 
            if gold_value >= get_find_cost(size):
                answer = max(answer, gold_value//m)

print(answer)