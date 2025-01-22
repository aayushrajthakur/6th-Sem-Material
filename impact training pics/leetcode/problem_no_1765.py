from collections import deque
import pandas as pd
def highestPeak(isWater):
    m, n = len(isWater), len(isWater[0])
    res = [[-1]*n for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if isWater[i][j]:
                res[i][j] = 0
                q.append((i, j))
    while q:
        i, j = q.popleft()
        for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i+x, j+y
            if 0 <= ni < m and 0 <= nj < n and res[ni][nj] == -1:
                res[ni][nj] = res[i][j] + 1
                q.append((ni, nj))
    return res

isWater = [[0,0,1],[1,0,0],[0,0,0]]
print('The input is : ')
print(pd.DataFrame(isWater))
result = highestPeak(isWater)
print("The output is : ")
print(pd.DataFrame(result))
