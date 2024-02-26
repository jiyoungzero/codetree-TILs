m1, d1, m2, d2 = map(int, input().split())

num_of_day = [0, 31, 29, 31,30,31,30,31,31,30,31,30,31]
A = input().rstrip()
week = ['Mon', 'Tue', 'Wed', 'Thu','Fri', 'Sat', 'Sun']

def to_day(m, d):
    result = 0
    for i in range(1, m):
        result += num_of_day[i]
    result += d
    return result

day1 = to_day(m1, d1)
day2 = to_day(m2, d2)
target = day1%7
print(day1, day2, target)
now = day1


answer = 0
while now <= day2:
    if now%7 == target:
        answer += 1
    now += 1
print(answer)