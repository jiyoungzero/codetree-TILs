import sys
input = sys.stdin.readline

r,c = map(int, input().split())
arr = [list(map(str , input().split())) for _ in range(r)]
answer = 0
# 4개의 점 찾기
# 첫번째 점

for m in range(1,r):
    for n in range(1, c):
        # 세번째 점 
        for a in range(m+1, r-1):
            for b in range(n+1, c-1):
                if arr[0][0] != arr[m][n] and arr[m][n] != arr[a][b] and arr[a][b] != arr[r-1][c-1]:
                    answer += 1

print(answer)