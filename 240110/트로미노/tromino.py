import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
# ㄱ자 블록
# ㅣ자 블록

for i in range(n-1):
    for j in range(m-1):
        tmp = []
        for a in range(i, i+2):
            for b in range(j, j+2):
                tmp.append(arr[a][b])
        for ele in tmp:
            answer = max(answer, sum(tmp)-ele)

for i in range(n-2):
    for j in range(m):
        tmp = 0
        for a in range(i, i+3):
            tmp += arr[a][j]
        answer = max(answer, tmp)

for i in range(n):
    for j in range(m-2):
        tmp = 0
        for b in range(j, j+3):
            tmp += arr[i][b]
        answer = max(answer, tmp)
print(answer)