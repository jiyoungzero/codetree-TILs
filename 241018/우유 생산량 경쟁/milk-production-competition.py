import heapq

n = int(input())
arr = []
for _ in range(n):
    date, name, updown = map(str, input().split())
    if updown[0] == '+':
        updown = int(updown[1:])
    else:
        updown = -int(updown[1:])
    arr.append((int(date), name, updown))
arr.sort()

answer = 0
name2num = {'Bessie':7, 'Elsie':7, 'Mildred':7}
winners = ['Bessie', 'Elsie', 'Mildred']
for ele in arr:
    _, name, updown = ele
    name2num[name] += updown

    max_value = 0
    for k, v in name2num.items():
        max_value = max(max_value, v)

    nxt_winners = []
    for k, v in name2num.items():
        if v == max_value:
            nxt_winners.append(k)
    if nxt_winners != winners:
        answer += 1
        winners = nxt_winners[:]
print(answer)