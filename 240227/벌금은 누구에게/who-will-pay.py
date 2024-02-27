import sys
input = sys.stdin.readline 


n, m, k = map(int, input().split())
queries = [int(input()) for _ in range(m)]
arr = [0]*(n+1) 
answer = -2

for query in queries:
    arr[query] += 1
    if arr[query] >= k:
        answer = query
        break

print(answer if answer > -2 else -1)