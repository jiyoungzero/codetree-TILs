# 시간과 위치가 같아져야 함!
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
a, b = [], []
answer = -1

start = 0
time = 0
for _ in range(N):
    d, t = map(str, input().split())
    for _ in range(int(t)):
        if d == 'L':
            start -= 1
            a.append(start)
        else:
            start += 1
            a.append(start)


start = 0
time = 0
for _ in range(M):
    d, t = map(str, input().split())
    for _ in range(int(t)):
        if d == 'L':
            start -= 1
            b.append(start)
        else:
            start += 1
            b.append(start)

for i, (a_pos, b_pos) in enumerate(zip(a, b)):
    if a_pos == b_pos:
        print(i+1)
        break
print(-1 if answer == -1)