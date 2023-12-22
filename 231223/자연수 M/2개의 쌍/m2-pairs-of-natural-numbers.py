import sys
input =sys.stdin.readline

n = int(input())
nums_cnt = []
for _ in range(n):
    x, y = map(int, input().split())
    nums_cnt.append([y, x])
m = len(nums_cnt)
nums_cnt.sort(key=lambda x:(x[0]))
answer = 0
i, j = 0, m-1

while 1:
    if i >= m//2:break

    t = min(nums_cnt[i][1], nums_cnt[j][1])
    if i == j:
        t //= 2
    answer = max(answer, nums_cnt[i][0] + nums_cnt[j][0])
    nums_cnt[i][1] -= t
    nums_cnt[j][1] -= t
    if nums_cnt[i][1] <= 0:
        i += 1
        i = min(m, i)
        
    if nums_cnt[j][1] <= 0:
        j -= 1
        j = max(0, j)

print(answer)