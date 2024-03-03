import sys
input = sys.stdin.readline 

n, b = map(int, input().split())
needs = [int(input()) for _ in range(n)]
answer = 0

needs.sort()
for i in range(n):
    copy_b = b
    tmp = 0
    target = needs[i] // 2

    for j in range(n):
        if i == j and target <= copy_b:
            tmp += 1
            copy_b -= target
        else:
            if copy_b >= needs[j]:
                tmp += 1
                copy_b -= needs[j]
            else:
                continue
    
    answer = max(answer ,tmp)
print(answer)