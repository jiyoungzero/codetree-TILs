import sys
input = sys.stdin.readline 

n, m, d, s = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(d)] # p, x, t 
sick_info = [list(map(int, input().split())) for _ in range(s)] # p, t
answer = 0

for i in range(1, m+1): # 하나의 치즈가 상했을 경우를 대비한 최대의 약 개수
    tmp = 0
    time = [0]*(n+1) # 각 사람이 i번째 치즈를 가장 처음에 먹은 시간 

    for eat_p, eat_x, eat_t in data:
        if eat_x == i:
            if time[eat_p] == 0:
                time[eat_p] = eat_t
            elif eat_t < time[eat_p]:
                time[eat_p] = eat_t
    

    flag = True
    for sick_p, sick_t in sick_info:
        if time[sick_p] == 0:
            flag = False
        if time[sick_p] >= sick_t:
            flag = False
    
    if flag:
        for eat_p, eat_x, eat_t in data:
            if i == eat_x:
                tmp += 1
    answer = max(answer, tmp)

print(answer)