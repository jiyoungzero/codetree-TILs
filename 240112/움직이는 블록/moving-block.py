import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
answer = 0
target = sum(arr)//n

while len(set(arr)) != 1:
    arr.sort()
    tmp = abs(target - arr[0])

    answer += tmp

    arr[-1] -= abs(target-arr[-1])
    arr[0] += tmp
print(answer)