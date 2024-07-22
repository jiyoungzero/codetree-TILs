import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

prefix = [0]*(n+1)
prefix[1] = arr[0]
for i in range(2, n+1):
    prefix[i] = prefix[i-1] + arr[i-1]

for length in range(1, n+1):
    for i in range(length, n+1):
        value = prefix[i] - prefix[i-length]
        # print(i, i-length, length, value)
        if value == k:
            answer += 1

print(answer)