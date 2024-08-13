import sys
input = sys.stdin.readline 
from bisect import bisect_right, bisect_left


n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
start = arr[0]
end = arr[-1]

def is_possible(mid):
    global start, end
    idx = 0
    cnt = 0

    while idx < n:
        if cnt > k: return False
        max_range = min(end, arr[idx]+mid*2)
        nxt_idx = bisect_right(arr, max_range)

        idx = nxt_idx
        cnt += 1
    if cnt > k :return False
    return True


l, r = 0, 10
answer = r
while l <= r:
    mid = (l+r)//2
    if is_possible(mid):
        r = mid - 1
        answer = min(answer, mid)
    else:
        l = mid + 1
print(answer)