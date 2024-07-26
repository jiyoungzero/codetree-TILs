import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]


def is_possible(target):
    total_cnt = 0 # m개 이상이 되어야 한다.

    for ele in nums:
        total_cnt += ele//target
        
    return total_cnt >= m


l, r = 1, min(nums)
max_idx = -1
while l <= r:
    mid = (l+r)//2
    if is_possible(mid):
        max_idx = max(max_idx, mid)
        l = mid + 1
    else:
        r = mid - 1
print(max_idx)