import sys
input = sys.stdin.readline 

n, m, c = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def is_possible(wait_limit):
    bus_cnt = 1
    ppl_cnt = 1
    idx = 0

    for i in range(1, n):
        if arr[i] - arr[idx] <= wait_limit and ppl_cnt + 1 <= c:
            ppl_cnt += 1
            continue 
        else:
            ppl_cnt = 1
            idx = i 
            bus_cnt += 1

    return bus_cnt <= m
    


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