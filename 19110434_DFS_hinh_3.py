# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 10:24:27 2021

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

# set the point visited 
visited =set()

# define the function of DFS
def dfs(graph,visited,node):
    if node not in visited:
        print(node);
        visited.add(node);
        for neighbor in graph[node]:
            dfs(graph,visited,neighbor)


dfs(graph, visited, '1')
