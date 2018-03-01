#!/bin/python3

# solution : find all connected graphs using DFS

import sys


def dfs(i, visited, edges, node_count):
    i_edge = edges[i]
    node_count += 1
        
    for e in i_edge:
        if visited[e] == 0:
            visited[e] = 1
            count += dfs(e, visited, edges, 0)
    return node_count

def roadsAndLibraries(n, c_lib, c_road, edges):
    if c_lib < c_road: # if lib price less than road price, we can build libs in all cities
        return n*c_lib
    
    visited = [0]*n
    total_cost = 0
    for i in range(n):
        if visited[i]==0:
            visited[i] = 1
            node_count = dfs(i, visited, edges, 0)
            total_cost += (node_count-1)*c_road+c_lib
    
    return total_cost

if __name__ == "__main__":
    q = int(input().strip()) 
    for a0 in range(q):
        n, m, c_lib, c_road = input().strip().split(' ')
        n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
        edges = dict()
        for i in range(n):
            edges[i] = []
        for cities_i in range(m):
            a, b = map(int, input().split())
            edges[a-1].append(b-1)
            edges[b-1].append(a-1)
        result = roadsAndLibraries(n, c_lib, c_road, edges)
        print(result)
