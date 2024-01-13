import sys
input = sys.stdin.readline 

n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n)]
b_x, b_y = map(int, input().split())