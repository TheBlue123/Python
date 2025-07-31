import heapq

def heuristic(a, b):
    # Distância de Manhattan
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()

    while open_set:
        _, cost, current, path = heapq.heappop(open_set)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                next_node = (nx, ny)
                if next_node not in visited:
                    heapq.heappush(open_set, (
                        cost + 1 + heuristic(next_node, goal),
                        cost + 1,
                        next_node,
                        path + [next_node]
                    ))
    return None

# Exemplo de uso
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
goal = (4, 4)
path = astar(grid, start, goal)
print("Menor caminho encontrado:", path)