# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:28:45 2021

@author: PC
"""

# creat tree using dictionary data
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

visited =set()

def DepthFirstSearch(graph,visited,mode):
    if mode not in visited:
        print(mode)
        visited.add(mode)
        for neighbor in graph[mode]:
            DepthFirstSearch(graph, visited, neighbor)
            
DepthFirstSearch(graph, visited, 'a')