import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0

s, e = 0, 2*n-1
while s <= e:
    answer = max(answer, arr[s]+arr[e])
    s +=1 
    e -= 1

print(answer)