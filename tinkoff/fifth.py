def is_reachable(graph, visited, start):
    stack = [start]
    while stack:
        city = stack.pop()
        if not visited[city]:
            visited[city] = True
            for neighbor in graph[city]:
                stack.append(neighbor)

def count_states(graph):
    n = len(graph)
    visited = [False] * n
    states = 0

    for city in range(n):
        if not visited[city]:
            is_reachable(graph, visited, city)
            states += 1

    return states

def find_x(n, m, roads):
    min_len = min(road[2] for road in roads)
    max_len = max(road[2] for road in roads)
    x = min_len

    while x <= max_len:
        graph = [[] for _ in range(n)]
        for road in roads:
            if road[2] <= x:
                graph[road[0]].append(road[1])
                graph[road[1]].append(road[0])
        
        states = count_states(graph)
        if states == n:
            return x
        x += 1

    return -1

n, m = map(int, input().split())
roads = []
for _ in range(m):
    u, v, w = map(int, input().split())
    roads.append((u, v, w))

x = find_x(n, m, roads)
print(x)