import sys
input = sys.stdin.readline 

n = int(input())
string = input().rstrip()
answer = 0
    
for length in range(1, n):
    repeat = 0
    repeat_flag= False
    for start in range(n):
        target = string[start:start+length]
        for i in range(n):
            # print(string[i:i+length], i, length)
            if target == string[i:i+length]:
                # print(target, string[i:i+length])
                repeat += 1

        if repeat < 2:
            answer = length
            repeat_flag = True
            break
    if repeat_flag:break

print(answer)