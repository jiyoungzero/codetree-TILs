n, b = map(int, input().split())
lights = [int(input()) for _ in range(n)]
# 왼쪽 : 인덱스 - 1 (if (idx - 1) < 0 : check_idx = -1)
max_b = 2**n
# print(max_b-2)
for _ in range(b%max_b):
    new_lights = lights[:]
    for i in range(n):
        left_index = (i - 1) % n
            
        if lights[left_index] == 1:
            new_lights[i] = 1 - lights[i]  # 상태 변경 (0 ↔ 1)
    lights = new_lights


for ele in lights:
    print(ele)