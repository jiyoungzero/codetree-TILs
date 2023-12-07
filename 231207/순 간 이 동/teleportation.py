import sys
input =sys.stdin.readline

a,b,x,y = map(int, input().split())
answer = int(1e9)

# a -> b
answer = min(answer, abs(a-b))
# a -> x, y->b
answer = min(answer, abs(a-x)+abs(y-b))
# a -> y, x -> b
answer = min(answer, abs(a-y)+abs(x-b))

print(answer)