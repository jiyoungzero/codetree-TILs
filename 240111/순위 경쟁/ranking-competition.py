import sys
input = sys.stdin.readline

n = int(input())
changes = [tuple(map(str, input().split())) for _ in range(n)]
a, b, c = 0, 0, 0
answer = 0

def get_score(aa, bb, cc):
    if aa > bb > cc or aa > cc > bb or aa > cc == bb:
        return 0
    elif bb > aa> cc or bb > cc > aa or bb > cc == aa:
        return 1
    elif cc > aa> bb or cc>bb>aa or cc > bb == aa:
        return 2
    elif aa == bb > cc:
        return 3
    elif aa == cc > bb:
        return 4
    elif bb == cc > aa:
        return 5
    elif aa == bb == cc:
        return 6
        

for name, value in changes:
    value = int(value)
    if name == 'A':
        if get_score(a+value, b, c) != get_score(a,  b, c):
            answer += 1
        a += value
    elif name == 'B':
        if get_score(a, b+value, c) != get_score(a,  b, c):
            answer += 1
        b += value
    else:
        if get_score(a, b, c+value) != get_score(a,  b, c):
            answer += 1
        c += value
print(answer)