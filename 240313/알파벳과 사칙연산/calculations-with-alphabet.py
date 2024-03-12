import sys
input = sys.stdin.readline 

cmd = input().rstrip()
alpToNum = dict()
answer = 0
for ele in cmd:
    if ele.isalpha():
        alpToNum[ele] = 0


def matchToAlpha(sel):
    tmp_dict = alpToNum
    for num, alp in zip(sel, alpToNum.keys()):
        tmp_dict[alp] = num
    return tmp_dict

def get_max(final_alpToNum):
    result = final_alpToNum[cmd[0]] 
    n = len(cmd)
    for idx in range(1, n-1):
        if not cmd[idx].isalpha():
            if cmd[idx] == '-':
                result -= final_alpToNum[cmd[idx+1]]
            elif cmd[idx] == '+':
                result += final_alpToNum[cmd[idx+1]]
            else:
                result *= final_alpToNum[cmd[idx+1]]
    return result


def backtracking(depth, sel):
    global answer
    if len(sel) == len(alpToNum):
        final_alpToNum = matchToAlpha(sel)
        # 최대값 계산 
        answer = max(answer, get_max(final_alpToNum))
        return

    for i in range(1, 5):
        sel.append(i)
        backtracking(depth+1, sel)
        sel.pop()

        
        
backtracking(1, [])

print(answer)