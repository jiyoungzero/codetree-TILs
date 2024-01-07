import sys
input = sys.stdin.readline 
from collections import deque
 
n, t = map(int, input().split())
que = deque()
tmp = []
for _ in range(3):
    tmp += list(map(int,input().split()))

for ele in tmp:
    que.append(ele)


while t:
    t -= 1
    que.appendleft(que.pop())


for i in range(3*n):
    print(que.popleft(), end=' ')
    if i%n == (n-1):
        print()