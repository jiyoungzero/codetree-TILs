import sys
input =sys.stdin.readline

n , m = map(int ,input().split())
jewelrys = [tuple(map(int, input().split())) for _ in range(n)]
info = []
# 무게 당 높은 가격 순으로 정렬,  round(answer, 3)
for idx, jewelry in enumerate(jewelrys):
    w, v = jewelry
    unit_price = v/w

    info.append((round(unit_price, 4), idx))
info.sort(reverse=True)

bag = 0
answer = 0

for target in info:
    if bag >= m:break
    unit_price, idx = target

    if jewelrys[idx][0] + bag <= m:
        bag += jewelrys[idx][0]
        answer += jewelrys[idx][1]
    else: # 쪼개기
        possible = m - bag
        answer += possible*unit_price
        break


print(format(answer,'.3f'))