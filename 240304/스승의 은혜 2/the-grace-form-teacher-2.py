import sys
input = sys.stdin.readline 

n, b = map(int, input().split())
needs = [int(input()) for _ in range(n)]
answer = 0
for i in range(n):
    tmp = 0
    target = needs[i] // 2
    for j in range(n):
        if i == j and target <= b:
            tmp += 1
            b -= target
        else:
            if b >= needs[j]:
                tmp += 1
                b -= needs[j]
            else:
                continue
    answer = max(answer ,tmp)
print(answer)