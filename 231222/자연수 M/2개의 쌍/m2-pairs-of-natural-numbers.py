import sys
input =sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    x, y = map(int, input().split())
    for _ in range(x):
        nums.append(y)
m = len(nums)
answer = 0

nums.sort()
for i in range(m//2):
    answer = max(answer, nums[i]+nums[m-i-1])
print(answer)