from common import *
import sys
import random as rand

#1: number has already been copied
#0: number hasn't been copied
def number_already_copied(par, number, cut1, cut2):
    while cut1 <= cut2:
        if par[cut1] == number:
            return 1
        cut1 +=1
    return 0

#returns the index of a number in a list
def locate(par,value):
    index = 0
    max = len(par)
    while index < max:
        if par[index] == value:
            return index
        index += 1

#create the child
def born_child(par1, par2, cut1, cut2):
    child = [-1] * len(par1)
    smaller = 0
    bigger  = len(par2)
    between = cut1
    between_end = cut2
    #copy [cut1,cut2] from p1 to child
    while between <= between_end:
        child[between] = par1[between]
        between+=1
    #copy [0,cut1) from p2 to child
    cut2 +=1
    while smaller < cut1:
        child[smaller] = par2[smaller]
        smaller +=1
    #copy (cut2,end] from p2 to child
    while cut2 < bigger:
        child[cut2] = par2[cut2]
        cut2 +=1
    return child


#do the crossover mix
def mutate_child(par1,par2,child,cut1,cut2):
    index = cut1
    while index <= cut2:
        #if number has been copied, go further
        number = par2[index]
        if number_already_copied(child,number,cut1,cut2) ==1:
            index +=1
        #else copy this number into child
        else:
            copy_index = index
            while (copy_index >= cut1) and (copy_index <= cut2):
                valP1 = par1[copy_index]
                copy_index = locate(par2,valP1)
            child[copy_index] = par2[index]
            index += 1
    return child


def pmx(par1, par2,cut1,cut2):
    child = born_child(par1,par2,cut1,cut2)
    return mutate_child(par1, par2, child, cut1, cut2)

def pmx_main(par1,par2,a,b):
    res = pmx(par1, par2,a,b)
    return res

#creates new child using partially mapped crossover
#this function cuts the parents on a random location
#param: par1 Parent1, par2 Parent2
#return: child1 and child2
def do_pmx(par1,par2):
    len1 = len(par1)
    len2 = len(par2)
    if len1 != len2:
        print("Parent1 and Parent2 must have the same length.")
        return -1
    else:
        random1 = rand.randint(0,len1-1)
        random2 = rand.randint(0,len1-1)
        if random1 < random2:
            return (pmx_main(par1,par2,random1,random2),
                   pmx_main(par2,par1,random1,random2))
        else:
            return (pmx_main(par1,par2,random2,random1),
                   pmx_main(par2,par1,random2,random1))
