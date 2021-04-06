# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:09:57 2021

@author: PC
"""

graph ={
    's':['a','c'],
    'a':['b','d'],
    'b':['e'],
    'c':['f','d'],
    'd':['e','g'],
    'f':['g'],
    'e':['h'],
    'g':['h'],
    'h':[]
}

# tạo danh sách các mode đã duyệt
visited =[]

# khởi tạo queue  
queue =[]

def BreadthFirstSearch(graph,visited,node):
    # thêm node đầu tiên vào visited và queue
    visited.append(node)
    queue.append(node)
    
    while queue:
        # pop phần tử đầu tiên và gán vào s
        s =queue.pop(0)
        print(s)
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

BreadthFirstSearch(graph, visited, 's')