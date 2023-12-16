import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(n-2):
    for j in range(n-2):
        tmp = 0
        for di in range(3):
            for dj in range(3):
                if arr[i+di][j+dj] == 1:
                    tmp += 1
        answer = max(answer, tmp)

print(answer)