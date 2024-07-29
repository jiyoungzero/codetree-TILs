import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

j = 0
answer = 0
for i in range(n):
    while j+1 < n and arr[i] + arr[j+1] > k:
        j += 1
    
    if j+1 < n and arr[i] + arr[j+1] <= k:
        answer += 1

print(answer)