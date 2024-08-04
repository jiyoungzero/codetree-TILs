import sys
input = sys.stdin.readline 

a = input().rstrip()
n = len(a)
closeArr = [0]*n
if a[0] == a[1] == ')':
    closeArr[0] = 1

for i in range(1, n-1):
    if a[i] == a[i+1] == ')':
        closeArr[i] = closeArr[i-1] + 1 
    else:
        closeArr[i] = closeArr[i-1]
closeArr = [0] + closeArr
# i번째 이후부터 나오는 닫힌 괄호 개수
# for i in range(1, len(closeArr)):
#     print(i-1, "번째 이후의 개수 = ", closeArr[-2]-closeArr[i-1])

answer = 0
for i in range(n-1):
    if a[i] == a[i+1] == '(':
        answer += (closeArr[-2]-closeArr[i])
print(answer)