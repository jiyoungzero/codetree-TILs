import sys
input = sys.stdin.readline 

a = input().rstrip()
a = '-' + a
n = len(a)
openArr = [0]*(n)
closeArr = [0]*(n)

# i에서부터 n-1번째까지 연속한 괄호가 나오면 +1
for i in range(1, n-1):
    if a[i] == a[i+1] == '(':
        openArr[i] = openArr[i-1] + 1
    else:
        openArr[i] = openArr[i-1]

for i in range(1, n-1):
    if a[i] == a[i+1] == ')':
        closeArr[i] = closeArr[i-1] + 1
    else:
        closeArr[i] = closeArr[i-1]
# print(a)
# print(openArr)
# print(closeArr)
answer = 0
for i in range(2, n-1):
    # print(i)
    open_ = openArr[i] - openArr[i-1]
    close_ = closeArr[-2] - closeArr[i-1]
    answer += (open_ * close_)
print(answer)