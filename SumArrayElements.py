# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:13:48 2021
@author: Carlos

Given an integer array arr of size n, you need to sum the elements of arr.
"""

def sumElement(arr,n):
    c=0
    for i in range(n):
        a=arr[i]
        c=c+a
    return c
    
print(sumElement([1,2,3],3))
