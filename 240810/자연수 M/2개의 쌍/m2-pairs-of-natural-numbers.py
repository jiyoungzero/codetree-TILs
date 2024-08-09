import sys
input = sys.stdin.readline 

n = int(input())
nums = []
for _ in range(n):
    cnt, num = map(int, input().split())
    for _ in range(cnt): nums.append(num)

nums.sort()
answer = 0
n = len(nums)
for i in range(n//2):
    answer = max(answer, nums[i]+nums[n-i-1])
print(answer)