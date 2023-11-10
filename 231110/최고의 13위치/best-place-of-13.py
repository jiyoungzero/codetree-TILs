import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split()))]
answer = 0

for i in range(n):
    for j in range(n-2):
        tmp = arr[i][j]+arr[i][j+1]+arr[i][j+2]
        print(tmp)
        answer = max(answer, tmp.count(1))
print(answer)