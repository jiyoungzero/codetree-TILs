x, y, z = map(int, input().split())


def dfs(selected, attempt):
    if is_successed(selected):
        return selected


dfs([x, y, z], 0)