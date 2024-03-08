import sys
input = sys.stdin.readline 

n = int(input())
answer = 0

b_arr = [int(input()) for _ in range(n)]
a_arr = []
for i in range(1, 2*n+1):
    if i not in b_arr:
        a_arr.append(i)
a_arr.sort()

for b in b_arr:
    for a in a_arr:
        if b < a:
            a_arr.remove(a)
            answer += 1
            # a_arr.sort()
        else:
            continue
print(answer)