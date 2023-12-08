import sys
input =sys.stdin.readline


n = int(input())
commands = [input().rstrip() for _ in range(n)]


def strToDate(date):
    year, month, day = date[:4], date[6:8], date[9:]
    return year*12*30 + month*30 + day

rainy = []
for idx, command in enumerate(commands):
    date, week, weather = command.split()
    if weather == 'Rain': rainy.append([strToDate(date), idx])
    else:continue

rainy.sort()
print(commands[rainy[0][1]])