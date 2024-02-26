m1, d1, m2, d2 = map(int, input().split())

num_of_day = [0, 31,28,31,30,31,30,31,31,30,31,30,31]
week = ['Mon', 'Tue', 'Wed', 'Thu','Fri', 'Sat', 'Sun']

def to_day(m, d):
    result = 0
    for i in range(1, m):
        result += num_of_day[i]
    result += d
    return result

day1 = to_day(m1, d1)
day2 = to_day(m2, d2)
print(week[(day2-day1)%7])