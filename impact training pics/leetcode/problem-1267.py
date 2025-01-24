from collections import deque

def countServers(grid):
    m, n = len(grid), len(grid[0])
    res = 0
    d = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                d.append([i, j]) 
    
    while d:
        count = 0
        i, j = d.popleft()
        k = 0
        while k < n:
            if grid[i][k] == 1:
                count += 1
            k += 1
        l = 0
        while l < m:
            if grid[l][j] == 1:
                count += 1
            l += 1
        if count > 2: 
            res += 1
    return res

# grid = [[1,0,0,0,1],[0,0,1,0,0],[0,1,0,1,0]]
grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
print(countServers(grid))