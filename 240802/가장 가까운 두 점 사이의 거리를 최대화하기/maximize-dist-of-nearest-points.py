import sys
input = sys.stdin.readline 

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()

def is_possible(dist):
    s, e = lines[0]

    last = s
    for a, b in lines[1:]:
        # print(dist, last, (a, b))
        if last + dist > b:
            return False
        last = max(a, last+dist)

    return True


l, r = 0, int(1e9)
maxDist = -1
while l <= r:
    mid = (l+r) // 2
    if is_possible(mid):
        maxDist = max(maxDist, mid)
        l = mid + 1 
    else:
        r = mid - 1
print(maxDist)