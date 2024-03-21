import sys
input = sys.stdin.readline 

n = int(input())
arr = [[0]*101 for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    arr[x][y] = 1
answer = int(1e9)

def count_dots(sx, ex, sy, ey):
    result = 0
    for row in range(sx, ex):
        for col in range(sy, ey):
            if arr[row][col]:
                result += 1
    return result

for x in range(1, 101):
    if x%2 == 0 :
        for y in range(1, 101):
            if y%2 == 0:
                a = count_dots(0, x, 0, y)
                b = count_dots(0, x, y, 101)
                c = count_dots(x, 101, 0, y)
                d = count_dots(x, 101, y, 101)
                max_value = max([a,b,c,d])
                answer = min(answer, max_value)
print(answer)