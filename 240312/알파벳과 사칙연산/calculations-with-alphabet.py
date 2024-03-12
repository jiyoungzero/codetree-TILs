import sys
input = sys.stdin.readline 

cmd = input().rstrip()
alpToNum = dict()
answer = 0
command_stack = []
num_stack = []

for ele in cmd:
    if ele.isalpha():
        alpToNum[ele] = 0
    else:
        command_stack.append(ele)
print(command_stack)