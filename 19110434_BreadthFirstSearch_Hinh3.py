# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:12:27 2021

@author: PC
"""

graph ={
    '1':['2','7','8'],
    '2':['3','6'],
    '7':[],
    '8':['9','12'],
    '12':[],
    '9':['10','11'],
    '10':[],
    '6':[],
    '11':[],
    '3':['4','5'],
    '4':[],
    '5':[]
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

BreadthFirstSearch(graph, visited, '1')