import sys
input = sys.stdin.readline 

n = int(input())
nums = []
for _ in range(n):
    cnt, num = map(int, input().split())
    nums.append([num, cnt])

nums.sort()
answer = 0

l, r = 0, n-1
while l <= r:
    min_val, min_cnt = nums[l]
    max_val, max_cnt = nums[r]

    answer = max(answer, min_val + max_val)

    if min_cnt < max_cnt:
        l += 1
        nums[r][1] -= min_cnt
    elif min_cnt > max_cnt:
        r -= 1
        nums[l][1] -= max_cnt
    else:
        l += 1
        r -= 1
    
print(answer)