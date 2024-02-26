import sys 
input = sys.stdin.readline 

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1, d1, m2, d2 = map(int, input().split())
answer = 0

def to_day(m, d):
    result = 0
    for i in range(1,m):
        result += num_of_days[i]
    result += d
    return result

day1 = to_day(m1, d1)
day2 = to_day(m2, d2)
print(day2-day1+1)