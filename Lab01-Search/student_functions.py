import numpy as np
import math
from priority_queue import *

def DFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO: 

    path = []
    visited = {}
    trace = {}
    stack = []
    n = int(math.sqrt(matrix.size))
    stack.append(start)
    last = start
    while len(stack) != 0 :
        e = stack.pop() 
        visited[e] = last
        if e == end :
            x = e
            path.clear()
            while x != start :
                path.append(x)
                x = visited[x]
            path.append(start)
            path.reverse()
            break 
        for x in range(n - 1, -1, -1) :
            if matrix[e, x] != 0 :
                if x not in visited:
                    stack.append(x)
        last = e
    return visited, path
    
def BFS(matrix, start, end):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    
    path=[]
    visited={}
    trace = {}
    queue = []
    queue2 = []
    n = int(math.sqrt(matrix.size))
    queue.append(start)
    queue2.append(start)
    while len(queue) != 0:
        e = queue.pop(0)
        last = queue2.pop(0)
        visited[e] = last
        if e == end :
            x = end
            while x != start :
                path.append(x)
                x = visited[x]

            path.append(start)
            path.reverse()
            return visited, path
        for i in range(0, n) :
            if matrix[e, i] != 0:
                if i not in visited: 
                    queue.append(i)
                    queue2.append(e)
    return visited, path
    

def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 

    path=[]
    visited={}
    queue = priorityQueue()
    trace = {}
    n = int(math.sqrt(matrix.size))
    d = [sys.maxsize for i in range(n + 1)]
    mark = [False for i in range(n + 1)]
    queue.push((0, start, start)) 
    visited[start] = start
    d[start] = 0
    while not queue.isEmpty():
        du, u, v = queue.pop()
        if mark[u] == True:
            continue
        visited[u] = v
    
        if u == end:
            x = end
            while x != start:
                path.append(x)
                x = visited[x]
            path.append(start)
            path.reverse()
            break
    
        mark[u] = True

        for i in range(0, n):
            if matrix[u, i] != 0:
                    if d[u] + matrix[u, i] < d[i]:
                        d[i] = d[u] + matrix[u, i]
                        queue.push((d[i], i, u))
    return visited, path

def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    return visited, path

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    return visited, path

