import sys
input = sys.stdin.readline 

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
prefix = [[0]*(1+n) for _ in range(n+1)]
prefix[1][1] = arr[0][0]

for i in range(n):
    prefix[1][i+1] = prefix[1][i] + arr[0][i]
for i in range(1, n):
    prefix[i+1][1] = prefix[i][1] + arr[i][0]


for i in range(2, n+1):
    for j in range(2, n+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + arr[i-1][j-1]


answer = -int(1e9)
for i in range(1, n+1):
    for j in range(1, n+1):
        tmp = 0
        for s in range(1, n+2-i):
            for e in range(1, n+2-j):
                tmp = prefix[s+i-1][e+j-1] - prefix[s+i-1][e-1] - prefix[s-1][e+j-1] + prefix[s-1][e-1]
                if tmp > answer: 
                    answer = tmp
print(answer)