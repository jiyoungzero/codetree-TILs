import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
lines = [tuple(map(int, input().split())) for _ in range(m)]
lines.sort()

l, r = 0, lines[-1][1] - lines[0][0]
maxDist = -1

def is_possible(dist):
    cnt = 1
    last = 0
    for i, line in enumerate(lines):
        # print(i, line)
        a, b = line
        now = a
        if i > 0 and now - last < dist:
            now = last + dist 
            if now <= b:
                cnt += 1
        elif i > 0 and now - last >= dist:
            cnt += 1

        while now <= b:
            now += dist 
            if now <= b: 
                last = now
                # print("now =", now, "cnt+1 =", cnt+1)
                cnt += 1
    return cnt >= n
        

# is_possible(2)
while l <= r:
    mid = (l+r)//2
    if is_possible(mid): # mid단위로 점을 배치했을 때, cnt가 n개 이상 되는지
        maxDist = max(maxDist, mid)
        l = mid + 1
    else:
        r = mid - 1

print(maxDist)