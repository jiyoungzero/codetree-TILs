import sys
input = sys.stdin.readline 

n = int(input())
answer= 0

def get_under_nums(mid):
    cnt = mid//3 + mid //5 - mid//15
    return mid - cnt

l, r = 1, 10**18
min_idx = r
while l <= r:
    mid = (l+r)//2
    under = get_under_nums(mid)
    if under == n: # 숫자 mid 이하에 있는 숫자의 개수가 n개 인지
        min_idx = min(min_idx, mid)
        r = mid - 1
    elif under > n:
        r = mid - 1
    else:
        l = mid + 1
print(min_idx)