import sys
input = sys.stdin.readline

n = int(input())
changes = [tuple(map(str, input().split())) for _ in range(n)]
a, b = 0, 0
answer = 0

def get_status(aa, bb):
    if aa == bb:
        return 0
    elif aa > bb:
        return 1
    else:
        return 2

for name, value in changes:
    value = int(value)
    if name == 'A':
        if get_status(a, b) != get_status(a+value, b):
            answer += 1
        
        a += value
    else:
        if get_status(a, b) != get_status(a, b+value):
            answer += 1
        b += value
print(answer)