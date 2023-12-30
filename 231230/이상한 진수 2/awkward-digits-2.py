import sys
input = sys.stdin.readline

def dec_to_bin(num):
    return bin(num)[2:]

def bin_to_dec(num):
    str_num = str(num)
    result = 0
    for i, ele in enumerate(str_num[::-1]):
        result += (int(ele)*2**i)
    return result


n = int(input())
answer = 0
length = len(str(n))
for i in range(1, length):
    if str(n)[i] == '1':
        answer = max(answer, bin_to_dec(str(n)[:i] + '0' + str(n)[i+1:]))
    else:
        answer = max(answer, bin_to_dec(str(n)[:i] + '1' + str(n)[i+1:]))
print(answer)