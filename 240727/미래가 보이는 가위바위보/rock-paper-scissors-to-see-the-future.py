import sys
input = sys.stdin.readline 

n = int(input())
bs = [input().rstrip() for _ in range(n)]
answer = -sys.maxsize

L, R = [0]*n, [0]*n
# print(bs)
for shape in "PHS":
    cnt = 0
    for i in range(n):
        if shape == bs[i]:
            cnt += 1
        L[i] = max(L[i], cnt)

for shape in "PHS":
    cnt = 0
    for i in range(n-1, -1, -1):
        if shape == bs[i]:
            cnt += 1
        R[i] = max(R[i], cnt)
# print(L, R)
for i in range(1, n):
    # i번째에 바꿈
    answer = max(answer, L[i-1] + R[i])
print(answer)