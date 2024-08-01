import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

l, r = 0,  arr[-1] - arr[0]
max_dist = -1

def is_possible(max_d):
    cnt = 1
    now = 0
    
    while True:
        nxt = now+1
        # print(now, nxt)
        while True:
            if nxt >= n:break
            if arr[nxt] - arr[now] < max_d:
                nxt += 1
            else:
                cnt += 1
                now = nxt
                break
        if nxt >= n-1:break
        
    return cnt >= m


while l <= r:
    mid = (l+r)//2
    if is_possible(mid): # 인접한 두 물건의 거리가 최대 mid가 되도록 m개 설치가 가능한지
        max_dist = mid
        l =  mid + 1
    else:
        r = mid - 1

print(max_dist)