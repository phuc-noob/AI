# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:14:09 2021

@author: PC
"""

graph={
       '1':['2','3','4'],
       '2':['5','6'],
       '3':[],
       '4':['7','8'],
       '5':['9','10'],
       '6':[],
       '7':['11','12'],
       '8':[],
       '9':[],
       '10':[],
       '11':[],
       '12':[]
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