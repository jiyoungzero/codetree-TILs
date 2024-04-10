import sys
input = sys.stdin.readline 

n, k, b = map(int, input().split())
blank = [int(input()) for _ in range(b)]
answer = int(1e9)
arr = [0 for i in range(1, n+1)]
arr = [0]+arr
for ele in blank:
    arr[ele] = 1

prefix = [0]*(n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1]+arr[i]

for i in range(1, n-k+2):
    answer = min(answer, prefix[i+k-1]-prefix[i-1])
print(answer)