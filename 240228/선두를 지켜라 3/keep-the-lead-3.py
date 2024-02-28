import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
a, b = [], []
answer = 0
start = 0
for _ in range(n):
    v,t = map(int, input().split())
    for _ in range(t):
        start += v
        a.append(start)

start = 0
for _ in range(m):
    v,t = map(int, input().split())
    for _ in range(t):
        start += v
        b.append(start)

winner = ''
if a[0] == b[0]:
    winner = 'ab'
elif a[0] > b[0]:
    winner = 'a'
else:
    winner = 'b'
if winner != 'ab':
    answer += 1

prev = winner
for a_pos, b_pos in zip(a[1:], b[1:]):
    if a_pos == b_pos:
        winner = 'ab'
    elif a_pos < b_pos:
        winner = 'b'
    else:
        winner = 'a'
    if prev != winner:
        answer += 1
    prev = winner
print(answer)