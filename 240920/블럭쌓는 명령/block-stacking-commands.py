import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
cmds = [tuple(map(int, input().split())) for _ in range(k)]
arr = [0]*(n+1)
for s, e in cmds:
    arr[s] += 1
    arr[e+1] -= 1
for i in range(1, n+1):
    arr[i] += arr[i-1] 

arr.sort()
print(arr[len(arr)//2])