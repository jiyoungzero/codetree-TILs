m1, d1, m2, d2 = map(int, input().split())

num_of_day = [0, 31, 29, 31,30,31,30,31,31,30,31,30,31]
A = input().rstrip()
week = [ 'Mon', 'Tue', 'Wed', 'Thu','Fri', 'Sat', 'Sun']

def to_day(m, d):
    result = 0
    for i in range(1, m):
        result += num_of_day[i]
    result += d
    return result

day1 = to_day(m1, d1)
day2 = to_day(m2, d2)
target = week.index(A)
# print(day1, day2, week[day1%7], week[day2%7])

answer = 0
now = day1
now_A = 'Mon'
while now <= day2:
    if now_A == A:
        answer += 1
    now += 1
    now_A = week[(week.index(now_A) + 1)%7]

print(answer)