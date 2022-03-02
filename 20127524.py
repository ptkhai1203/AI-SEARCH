import numpy as np
import math

visit = {}
path = []

def DFS(matrix, start, end):
    global visit
    global path
    n = int(math.sqrt(matrix.size))
    visit[start] = 1
    for i in range(0, n) :
        print(i)
        if i in visit:
            continue
        if matrix[start, i] != 0 :
            path.append((start + 1, i + 1))
            visit[i] = 1
            DFS(matrix, i, end)
            print('visit {}'.format(i + 1))
        if i == end:
            return 
start, end = [int(x) for x in input().split()]
matrix = np.array([[0, 2, 4, 8], [1, 0 , 5, 8], [1, 0, 0, 0], [1, 1, 1, 0]])
print(matrix[0, 0])
start = start - 1
end = end - 1
DFS(matrix, start, end)

print(visit, path)