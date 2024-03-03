import sys
input = sys.stdin.readline 

n, b = map(int,input().split())
needs = [list(map(int, input().split())) for _ in range(n)] # p, s
for i, (p, s) in enumerate(needs):
    needs[i].append(p+s)
needs.sort(key=lambda x:(x[2]))
answer = 0

for i in range(n):
    copy_b = b
    tmp = 0
    target = needs[i][0] // 2 + needs[i][1]
    for j in range(n):
        if i == j and target <= copy_b:
            tmp += 1
            copy_b -= target
        else:
            if needs[j][2] <= copy_b:
                tmp += 1
                copy_b -= needs[j][2]
            else:
                continue


    answer = max(answer ,tmp)
print(answer)