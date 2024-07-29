import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum_v = arr[0]
answer = 0
j = 0
for i in range(n):
    while j+1 < n and sum_v+arr[j+1] < m:
        sum_v += arr[j+1]
        j += 1
    
    if j+1 < n and sum_v + arr[j+1] == m:
        answer += 1
    # print("?", i, j, sum_v)
    sum_v -= arr[i]
print(answer)