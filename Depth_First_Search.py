# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 07:51:53 2021

@author: PC
"""

graph = {
'A' : ['B','C'],
'B' : ['D', 'E'],
'C' : ['F'],
'D' : [],
'E' : ['F'],
'F' : []
}
visited = set() # Tập hợp các nút đã duyệt (Set to keep track of visited nodes).
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
# Bắt đầu duyệt (Driver Code)
dfs(visited, graph, 'A')