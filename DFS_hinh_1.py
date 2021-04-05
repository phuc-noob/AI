# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 09:09:00 2021

@author: PC
"""

graph = {
'1' : ['2','3'],
'2' : ['4', '5'],
'3' : [],
'4' : [],
'5' : [],
}
visited = set() # Tập hợp các nút đã duyệt (Set to keep track of visited nodes).
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
# Bắt đầu duyệt (Driver Code)
dfs(visited, graph, '1')
