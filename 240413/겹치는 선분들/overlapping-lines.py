import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
cmds = []
answer = 0

for _ in range(n):
    cnt, dir = input().split()
    if dir == 'R':
        cmds.append((int(cnt), 1))
    else:
        cmds.append((int(cnt), -1))

checked = [0]*2*int(1e6)
x = int(1e6)
for cmd in cmds:
    s, e = x, x+(cmd[0]*cmd[1])
    if s < e:
        checked[s] += 1
        checked[e] -= 1
        x = e
    else:
        checked[e] += 1
        checked[s] -= 1
        x = e


sum_value = 0
for c in checked:
    sum_value += c 
    if sum_value >= k:
        answer += 1
print(answer)