import sys
input = sys.stdin.readline 
from collections import defaultdict

string = input().rstrip()

num_cnt  = [-1]*26
start = 0
answer = -1
for i in range(len(string)):
    if num_cnt[ord(string[i])-97] > -1:
        start = num_cnt[ord(string[i])-97]+1

    num_cnt[ord(string[i])-97] = i
    answer = max(answer, i-start+1)
print(answer)