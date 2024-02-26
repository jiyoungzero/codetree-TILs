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
    a_time, b_time = -1, -1
    if a:
        a_time, move_a = a.popleft()
    if b:
        b_time, move_b = b.popleft()
    
    if a_time > 0 and b_time > 0:
        na = ax + a_time*move_a
        nb = bx + b_time*move_b
        if (ax != bx) and ((ax < bx and na >= bx) or (ax > bx and na <= bx)):
            answer += 1
        ax = na
        bx = nb
            

    elif a_time == -1 and b_time > 0:
        nb = bx + move_b*b_time
        if (ax != bx) and (ax == nb):
            answer += 1
        bx = nb
    
    elif a_time > 0 and b_time == -1:
        na = ax + move_a*a_time
        if (ax != bx) and (na == bx):
            answer += 1
        ax = na

print(answer)