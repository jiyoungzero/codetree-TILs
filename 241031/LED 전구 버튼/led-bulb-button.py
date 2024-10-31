def toggle_lights(n, b, lights):
    seen_states = {}
    current_state = tuple(lights)

    for step in range(b):
        if current_state in seen_states:
            # 주기를 발견
            cycle_length = step - seen_states[current_state]
            remaining_steps = b % cycle_length
            
            for _ in range(remaining_steps):
                new_state = []
                for i in range(n):
                    left_index = (i - 1) % n
                    if current_state[left_index] == 1:
                        new_state.append(1 - current_state[i])
                    else:
                        new_state.append(current_state[i])
                current_state = tuple(new_state)
            break
        else:
            seen_states[current_state] = step
            new_state = []
            for i in range(n):
                left_index = (i - 1) % n
                if current_state[left_index] == 1:
                    new_state.append(1 - current_state[i])
                else:
                    new_state.append(current_state[i])
            current_state = tuple(new_state)
    
    return list(current_state)

# 입력 받기
n, b = map(int, input().split())
lights = [int(input().strip()) for _ in range(n)]

# 전구 상태 변경
final_state = toggle_lights(n, b, lights)

# 결과 출력
for state in final_state:
    print(state)