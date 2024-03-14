import sys
input =sys.stdin.readline 

n,m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

idx = 0
while idx < n:
    flag = False
    for i in range(idx, min(n, idx + 2*m+ 1)):
        if arr[i] == 1:
            flag = True
    if flag:
        answer += 1
        for i in range(idx, min(n, idx + 2*m+1)):
            arr[i] = 0
        idx = min(idx + 2*m+1, n-1)
    elif not flag:
        idx = min(idx+1, n-1)

    if idx == n-1:
        break

if arr[-1] == 1:
    answer += 1
            

print(answer)