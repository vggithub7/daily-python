# -*- coding: utf-8 -*-
"""
Created on Fri May 22 07:43:31 2020

@author: gaba
@question: acceot 2 numbers from user return product if its less than 1000 else return sum
"""

def multiply_limit(a,c):
    a,c=[int(x) for x in [a,c]]
    if (a*c)<1000:
        return a*c
    else:
        return a+c
def sum_current_prev(m):
    m=int(m)
    prev=0
    v=[]
    for i in range(int(m)+1):
        sum=prev + i
        v.append(sum)
        prev=i
    return v

if __name__=='__main__':#__init__(self):
    #a,c=input(" enter two numbers ").split()
    #print("result is ",multiply_limit(a,c))
    a=sum_current_prev(input("enter range number (eg. 7) : ")) 
    print("output of current and prev number till %s is "%(len(a)-1))
    for i in a:
        print(i)                
