import sys
input =sys.stdin.readline

n , m = map(int ,input().split())
jewelrys = [tuple(map(int, input().split())) for _ in range(n)]
jewelrys.sort(key=lambda x: -x[1]/x[0])
answer = 0

for w, v in jewelrys:
    if m >= w:
        m -= w
        answer += v
    else:
        answer += (m/w)*v
        break

print(format(answer,'.3f'))