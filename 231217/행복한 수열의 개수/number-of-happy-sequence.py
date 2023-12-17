import sys
input = sys.stdin.readline




n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# 행 
for i in range(n):
    start = arr[i][0]
    tmp = 0
    for j in range(1, n):
        if start == arr[i][j]:
            tmp += 1
        else:
            tmp = 0
        start = arr[i][j]
    if tmp >= m:
        answer += 1


            
# 열
for j in range(n):
    start = arr[0][j]
    tmp = 0
    for i in range(1, n):
        if start == arr[i][j]:
            tmp += 1
        else:
            tmp = 0
        start = arr[i][j]
    if tmp >= m:
        answer += 1
print(answer)