import sys
input =sys.stdin.readline 

n,m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

tmp = 0
pass_ = 0
for ele in arr:
    if pass_ > 0 :
        pass_ -= 1
        continue 

    if pass_ == 0 and tmp == m:
        answer += 1
        pass_ = m 
        tmp = 0
        continue

    if ele == 1:
        tmp +=1 

print(answer)