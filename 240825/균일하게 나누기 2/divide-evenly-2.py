import sys
input = sys.stdin.readline 


n = int(input())
dots = [tuple(map(int, input().split())) for _ in range(n)]

dots.sort()
answer = sys.maxsize

for b in range(0, 1001, 2):
    cnts = [0]*4 # 각 4분면의 점 개수

    for _, y in dots:
        if y > b:
            cnts[0] += 1
        else:
            cnts[3] += 1

    for i in range(n):
        x, y = dots[i]
        if i == 0 or dots[i][0] != dots[i-1][0]:
            answer = min(answer, max(cnts))

        if y > b:
            cnts[0] -= 1
            cnts[1] += 1
        else:
            cnts[3] -= 1
            cnts[2] += 1

print(answer)