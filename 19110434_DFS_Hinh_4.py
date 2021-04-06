# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:01:20 2021

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

visited =set()

def DepthFirstSearch(graph,visited,mode):
    if mode not in visited:
        print(mode)
        visited.add(mode)
        for neighbor in graph[mode]:
            DepthFirstSearch(graph,visited,neighbor)
            
DepthFirstSearch(graph,visited,'1');