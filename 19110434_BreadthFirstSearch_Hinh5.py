# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:16:03 2021

@author: PC
"""

graph ={
        'a':['b','c'],
        'b':['d','e'],
        'c':['f','g'],
        'f':['k'],
        'k':[],
        'g':[],
        'd':['h'],
        'h':[],
        'e':['i','j'],
        'i':[],
        'j':[],
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

BreadthFirstSearch(graph, visited, 'a')