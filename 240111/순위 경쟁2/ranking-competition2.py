import sys
input = sys.stdin.readline

n = int(input())
a, b = 0, 0
answer = 0

winner = 'ab'
for _ in range(n):
    who, change = input().split()
    change = int(change)
    tmp = ''
    if who == 'A':
        a += change
    else:
        b += change

    if a == b:
        tmp = 'ab'
    elif a > b:
        tmp = 'a'
    else:
        tmp = 'b'
    
    if winner != tmp:
        answer += 1
        winner = tmp
    else:
        continue
print(answer)