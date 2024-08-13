import sys
input = sys.stdin.readline 
from bisect import bisect_right, bisect_left


n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()


def is_possible(mid):
    cnt = 1
    idx = 0

    for i in range(n):
        if arr[i] - arr[idx] <= 2*mid:
            continue 
        else:
            idx = i
            cnt += 1
    return cnt <= k


l, r = 0, 10**9
answer = r
while l <= r:
    mid = (l+r)//2
    if is_possible(mid):
        r = mid - 1
        answer = min(answer, mid)
    else:
        l = mid + 1
print(answer)