import sys
input =sys.stdin.readline


n = int(input())
commands = [input().rstrip() for _ in range(n)]


def strToDate(date):
    year, month, day = date.split('-')
    return int(year)*12*30 + int(month)*30 + int(day)

rainy = []
for idx, command in enumerate(commands):
    date, week, weather = command.split()
    if weather == 'Rain': rainy.append([strToDate(date), idx])
    else:continue


rainy.sort()


print(commands[rainy[0][1]])