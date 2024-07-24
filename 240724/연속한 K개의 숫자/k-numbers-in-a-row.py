import sys
input = sys.stdin.readline 

n, k, b = map(int, input().split())
nums = list(range(1, n+1))
for _ in range(b):
    empty = int(input())
    nums[empty-1] = 0
prefix = [0]*(n+1)
# print(nums)
for i in range(1, n+1):
    if nums[i-1] == 0:
        prefix[i] = prefix[i-1] + 1
    else:
        prefix[i] = prefix[i-1]
# print(prefix)
answer = int(1e9)

for i in range(k, 1+n):
    tmp = prefix[i]-prefix[i-k]
    if tmp < answer:
        answer = tmp
print(answer)