import sys
input = sys.stdin.readline 


n, m = map(int, input().split())
answer = 0
a = []
b = []

start = 0
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        start += v
        a.append(start)

start = 0
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        start += v
        b.append(start)

front = 'a' if a[0] > b[0] else 'b'
for i in range(1, len(a)):
    if front == 'b' and a[i] > b[i]:
        front = 'a'
        answer += 1
    elif front == 'a' and a[i] < b[i]:
        front = 'b'
        answer += 1

print(answer)