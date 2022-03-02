import numpy as np
import math

def DFS(matrix, start, end):
    path = []
    visited = {}
    trace = {}
    stack = []
    n = int(math.sqrt(matrix.size))
    visited[start] = 1
    stack.append(start)
    while len(stack) != 0 :
        e = stack.pop() 
        visited[e] = 1
        if e == end :
            x = e
            path.clear()
            while x != start :
                path.append((trace[x] + 1, x + 1))
                x = trace[x]
            path.reverse() 
        for x in range(n - 1, -1, -1) :
            if matrix[e, x] != 0 :
                if x not in visited:
                    stack.append(x)
                    trace[x] = e
    return visited, path

start, end = [int(x) for x in input().split()]
matrix = np.array([[0, 2, 4, 8], [1, 0 , 5, 8], [1, 0, 0, 0], [1, 1, 1, 0]])
start = start - 1
end = end - 1
visited, path = DFS(matrix, start, end)

print(visited, path)
