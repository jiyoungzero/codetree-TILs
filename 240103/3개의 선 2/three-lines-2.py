import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
answer = 0
MAX_VALUE = 0

for x, y in points:
    MAX_VALUE = max([x, y, MAX_VALUE])


for i in range(MAX_VALUE+1):
    for j in range(MAX_VALUE+1):
        for k in range(MAX_VALUE+1):
            flag = True

            # x축으로만 3개
            for x, y in points:
                if i == y or j == y or k == y:
                    continue
                flag = False
            if flag:
                answer = 1 

            flag = True
            # x축 2개, y축 1개
            for x, y in points:
                if (i == y or j == y) or k == x:
                    continue
                flag = False
            if flag:
                answer = 1   
            flag = True
            # x축 1개, y축 2개
            for x, y in points:
                if i == y or (j == x or k == x):
                    continue
                flag = False
            if flag:
                answer = 1                           
            flag = True
            # y축 3개
            for x, y in points:
                if i == x or j == x or k == x:
                    continue
                flag = False
            if flag:
                answer = 1   
print(answer)