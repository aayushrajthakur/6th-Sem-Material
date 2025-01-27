from collections import deque


def bfs(adjacency_list, start):

    d = deque([start])
    visited = set()
    visited.add(start)

    while d:
        curr = d.popleft()
        print(f"{curr} is visited.")

        for x in adjacency_list[curr].keys():
            if x not in visited:
                visited.add(x)
                d.append(x)

bfs(adjacency_list, 'A')