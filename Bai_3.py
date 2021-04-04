# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 23:17:33 2021

@author: PC
"""
def HaNoiTower(n,source,temp,target):
    if n ==1:
        print("Move %i from Tower %s to Tower %s "% (n,source,target))
    else :
        HaNoiTower(n-1,source,target,temp)
        print("Move %i from Tower %s to Tower %s " %(n,source,target))
        HaNoiTower(n-1, temp, source, target)
        
HaNoiTower(4,'A','B','C')