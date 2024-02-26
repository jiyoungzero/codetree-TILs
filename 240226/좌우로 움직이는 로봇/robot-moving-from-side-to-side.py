from collections import deque
n, m = map(int, input().split())
a = deque()
b = deque()
answer = 0

for _ in range(n):
    t, d = map(str, input().split())
    if d == 'L':
        a.append((int(t), -1))
    else:
        a.append((int(t), +1))

for _ in range(m):
    t, d = map(str, input().split())
    if d == 'L':
        b.append((int(t), -1))
    else:
        b.append((int(t), +1))


ax, bx = 0, 0
while True:
    if len(a) == 0 and len(b) == 0:
        break

    if a:
        at, ad = a.popleft()
        nxt_ax = ax+at*ad
    if b:
        bt, bd = b.popleft()
        nxt_bx = bx+bt*bd
    
    if ax != bx and ((ax < bx and nxt_ax >= nxt_bx) or ( ax > bx and nxt_ax <= nxt_bx)):
        answer += 1
    ax, bx = nxt_ax, nxt_bx

print(answer)