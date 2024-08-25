import sys
input = sys.stdin.readline 
from collections import defaultdict

string = '#' + input().rstrip()

num_cnt  = defaultdict(int)
answer = -1

end = 0
for start in range(1, len(string)):
    while end + 1 < len(string) and num_cnt[string[end+1]] == 0:
        num_cnt[string[end+1]] += 1
        end += 1
        
    answer = max(answer, end-start+1)
    num_cnt[string[start]] -= 1

print(answer)