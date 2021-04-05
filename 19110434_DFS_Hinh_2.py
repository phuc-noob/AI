# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 09:25:53 2021

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

# set the point visited 
visited =set()

# define the function of DFS
def dfs(graph,visited,node):
    if node not in visited:
        print(node);
        visited.add(node);
        for neighbor in graph[node]:
            dfs(graph,visited,neighbor)


dfs(graph, visited, 's')
