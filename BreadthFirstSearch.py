# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 12:03:18 2021

@author: PC
"""

graph ={
       'a':['b','c'],
       'b':['d','e'],
       'c':['f'],
       'd':[],
       'e':['f'],
       'f':[],
}

# creat a empty list of visited
visited =[]
# creat a queue
queue =[]

def bfs(graph,visited ,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        s= queue.pop(0);  #pop the first element
        print(s)
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                
bfs(graph, visited, 'a')
                
