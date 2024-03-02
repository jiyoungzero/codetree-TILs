import sys
input = sys.stdin.readline 

n, m, d, s = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(d)] # (p = 몇번째 사람, m = 몇 번째 치즈, t= 먹은 시간)
sick_info = [list(map(int, input().split())) for _ in range(s)] # (p = 몇번째 사람, t = 언제 아팠는지)
answer = len(sick_info)
people = [False]*(n)
for s_p, _ in sick_info:
    people[s_p-1] = True

potential_cheese = [0]*(m+1) # 상한 치즈
# 사람의 수 N, 치즈의 수 M

for eat_p, eat_m, eat_t in data:
    for s_p, s_t in sick_info:
        if s_p == eat_p and eat_t < s_t:
            potential_cheese[eat_m] += 1

def eat(cheese_idx, person):
    for eat_p, eat_m, eat_t in data:
        if cheese_idx == eat_m and eat_p == person:
            return True
    return False

# sick_info에 없으면서, p_cheese를 먹은 사람이 있는지
for cheese_idx, p_cheese in enumerate(potential_cheese):
    if p_cheese == n-1:
        for person_idx, person in enumerate(people):
            if person == False and eat(cheese_idx, person_idx+1):
                answer += 1
print(answer)