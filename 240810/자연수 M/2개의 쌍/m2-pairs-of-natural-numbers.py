import sys
input = sys.stdin.readline 

n = int(input())
nums = []
for _ in range(n):
    cnt, num = map(int, input().split())
    nums.append([num, cnt])

nums.sort()
answer = 0

while len(nums) > 2:
    if len(nums) == 1:
        answer = nums[0][0]*2
        break
    if len(nums) == 0:break
    min_val, min_cnt = nums[0]
    max_val, max_cnt = nums[-1]
    answer = max(answer, min_val+max_val)
    rmv = min(min_cnt, max_cnt)
    nums[0][1] -= rmv
    if nums[0][1] <= 0:
        del nums[0]
    nums[-1][1] -= rmv
    if nums[-1][1] <= 0:
        del nums[-1]
 
    
print(answer)