n, b = map(int, input().split())
ps_arr = [list(map(int, input().split())) for _ in range(n)]
ps_arr.sort(key = lambda x:(x[0]//2 + x[1], x[0]))
# print(ps_arr)
# p : 선물 가격, s : 배송비
# flag = False
answer = 0
# prefix = [0]*n # 각 인덱스의 선물가격을 반값하고 계산한 최대 학생 수

for i, (p, s) in enumerate(ps_arr):
    tmp = 0
    cnt = 0
    for j in range(n):
        if i == j:
            tmp += (p//2 + s)
        else:
            tmp += sum(ps_arr[j])

        if tmp > b:
            answer = max(answer, cnt)
            break
        else:
            cnt += 1
print(answer)

    
