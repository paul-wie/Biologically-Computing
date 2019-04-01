from common import *
import sys
import random as rand

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
        print(random1,random2)
        if random1 < random2:
            return (pmx_main(par1,par2,random1,random2),
                   pmx_main(par2,par1,random1,random2))
        else:
            return (pmx_main(par1,par2,random2,random1),
                   pmx_main(par2,par1,random2,random1))

p1 = [9,3,7,8,2,6,5,1,4]
p2 = [1,2,3,4,5,6,7,8,9]

r1 = [2,4,7,1,3,6,8,9,5]
r2 = [5,9,8,6,2,4,1,3,7]

t1 = ['a','b','c','d']
t2 = ['d','b','a','c']



#print(pmx_main(parent2, parent1, 3,6))
#print(pmx_main(p1, p2, 3,6))
#print(pmx_main(t1, t2,2,5))
print("T1:", t1)
print("T2:", t2)
res1 = pmx_main(t1, t2,1,2)
print(res1)
print("T1:", t1)
print("T2:", t2)
res2 = pmx_main(t2, t1,2,2)
print(res2)
print(do_pmx(t1,t2))
