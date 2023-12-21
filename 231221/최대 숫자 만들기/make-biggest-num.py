import sys
input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]
arr.sort(key=lambda x:int((x*10)[:9]), reverse = True)
print(''.join(arr))