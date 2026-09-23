from collections import deque
graph = {
    "S": ["A", "B"],
    "A": ["G"],
    "B": ["C"],
    "C": ["G"],
    "G": []
}
def bfs(start, goal):
    frontier = deque([[start]])
    explored = set()
    while frontier:
        path = frontier.popleft()
        node = path[-1]
        print("Expanding:", node)
        if node == goal:
            return path
        if node not in explored:
            explored.add(node)
            for neighbor in graph[node]:
                frontier.append(path + [neighbor])
    return None
solution = bfs("S", "G")

print("---")

def dfs(start, goal):
    frontier = deque([[start]])
    explored = set()
    while frontier:
        path = frontier.pop()
        node = path[-1]
        print("Expanding:", node)
        if node == goal:
           return path
        if node not in explored:
            explored.add(node)
            for neighbor in graph[node]:
                frontier.append(path + [neighbor])
    return None
solution1 = dfs("S", "G")

print("BFS Solution:", solution)
print("DFS Solution:",solution1)