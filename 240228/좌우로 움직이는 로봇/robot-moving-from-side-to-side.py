n, m = map(int, input().split())
a = []
b = []
answer = 0
pos = 0

for _ in range(n):
    t, d = map(str, input().split())
    t = int(t)
    if d == 'L':
        d = -1
    else:
        d = +1
    for _ in range(t):
        pos += d
        a.append(pos)

pos = 0
for _ in range(m):
    t, d = map(str, input().split())
    t = int(t)
    if d == 'L':
        d = -1
    else:
        d = +1
    for _ in range(t):
        pos += d
        b.append(pos)
prev_a, prev_b = 0, 0
now_a, now_b = 0, 0
for i in range(max(len(a), len(b))):
    if len(a) <= i:
        now_a = prev_a
        now_b = b[i]
    elif len(b) <= i:
        now_b = prev_b
        now_a = a[i]
    else:
        now_a = a[i]
        now_b = b[i]
    if prev_a != prev_b and now_a == now_b:
        answer += 1

    prev_a, prev_b = now_a, now_b
    # print(i)
    # print(prev_a, prev_b, now_a, now_b)

print(answer)