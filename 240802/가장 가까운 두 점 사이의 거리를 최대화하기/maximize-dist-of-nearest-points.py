import sys
input = sys.stdin.readline 

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()

def is_possible(dist):
    s, e = lines[0]
    for start in range(s, e + 1):
        flag = True
        dots = [start]*len(lines)
        for i in range(1, len(lines)):
            dots[i] = dots[i-1]+dist 
        # print(dist, "->", dots)
        for dot, (ns, ne) in zip(dots, lines):
            if dot <= ne:
                # print(dot, ne)
                continue
            else:
                flag = False
                break
        if flag:return True
        else:return False
    return False



l, r = 1, lines[-1][1] - lines[0][0]
maxDist = -1
while l <= r:
    mid = (l+r) // 2
    if is_possible(mid):
        maxDist = max(maxDist, mid)
        l = mid + 1 
    else:
        r = mid - 1
print(maxDist)