n, b = map(int, input().split())
lights = [int(input()) for _ in range(n)]
# 왼쪽 : 인덱스 - 1 (if (idx - 1) < 0 : check_idx = -1)
max_b = 2**n
for _ in range(b%max_b):
    nxt_lights = []
    for i in range(n):
        check_idx = i - 1
        if check_idx < 0:
            check_idx = -1
            if lights[check_idx] == 1:
                nxt_lights.append((lights[i]+1)%2)
            else:
                nxt_lights.append(lights[i])
        else:
            if lights[check_idx] == 1:
                nxt_lights.append((lights[i]+1)%2)
            else:
                nxt_lights.append(lights[i])
    lights = nxt_lights[:]

for ele in lights:
    print(ele)