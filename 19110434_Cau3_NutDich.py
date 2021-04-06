# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:17:34 2021

@author: PC
"""

graph ={
        'Q':['N','Y','T'],
        'N':['L','R'],
        'Y':['A','X'],
        'T':['H','E'],
        'E':[],
        'L':['F','U'],
        'R':[],
        'A':['K','O'],
        'X':[],
        'H':['I','G'],
        'F':[],
        'O':[],
        'U':['B','Z'],
        'K':['D','S'],
        'I':['C','V'],
        'G':['M','P'],
        'B':[],
        'Z':[],
        'D':[],
        'S':[],
        'C':[],
        'V':[],
        'M':[],
        'P':[],
}

# khởi tạo queue  
#queue =[]
# tạo danh sách các mode đã duyệt
visited =[]
curent =''

#visited = set() # Tập hợp các nút đã duyệt (Set to keep track of visited nodes).
def dfs(visited, graph, node, target):
    if node not in visited:
        if node is not target:
            visited.append(node)
            if not len(graph[node]):
                visited.pop()
                temp =[]
                temp =visited
                curent =temp[len(temp)-1]
                dfs(visited, graph, curent, target)
            for neighbour in graph[node]:
                dfs(visited, graph, neighbour,target)
        else:
             print('--------------------')
             for k in visited:
                 print(k)
   
       
# Bắt đầu duyệt (Driver Code)
dfs(visited, graph, 'Q', 'A')

