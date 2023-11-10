import sys
input = sys.stdin.readline

a = input()
answer = 0

def binary2Decimal(num):
    n = len(num)
    num = num[::-1]
    mul = 1
    result = 0
    for i in range(n):
        result += (int(num[i])*mul)
        mul *= 2
    return result

for i in range(len(a)):
    if a[i] == '0':
        target = (a[:i]+'1'+a[i+1:])
    else:
        target = (a[:i]+'0'+a[i+1:])
    answer = max(answer, binary2Decimal(target))



print(answer)