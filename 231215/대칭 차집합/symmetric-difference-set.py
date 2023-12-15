a, b = map(int, input().split())
set_a = set(list(map(int, input().split())))
set_b = set(list(map(int, input().split())))

answer = len(set_a - set_b) + len(set_b - set_a)
print(answer)