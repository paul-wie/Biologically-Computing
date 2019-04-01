from common import *

def count_number(a,b):
    res = 1
    while a < b:
        a +=1
        res +=1
    return res

def order_crossover(parent1, parent2):
    cut1 = 3
    cut2 = 6
    proof(parent1,parent2,cut1,cut2)
    child = parent1

    #count number of digits that have been copied
    copied = count_number(cut1,cut2)
    #number of digits that has to be copied
    to_copy = len(parent1)-copied
    #index where to copy a new digigt
    place_to_copy = (cut2+1)%len(parent1)
    #pointer that iterates through list
    pointer = place_to_copy
    while to_copy >0:
        #when a digit from list 2 already has been copied, then increase counter
        while number_already_copied(parent1, parent2[pointer],cut1,cut2) ==1:
            pointer = (pointer+1)%len(parent1)
        #otherwise copy the new digit to the child
        child[place_to_copy] = parent2[pointer]
        #increase pointer and index
        pointer = (pointer+1)%len(parent1)
        place_to_copy = (place_to_copy+1)%len(parent1)
        #decrease the number of digits that has to be copied
        to_copy -= 1
    return child


    #index = (cut2+3)%len(parent1)



p1 = [1,2,3,4,5,6,7,8,9]
p2 = [9,3,7,8,2,6,5,1,4]

r1 = [2,4,7,1,3,6,8,9,5]
r2 = [5,9,8,6,2,4,1,3,7]
print(order_crossover(r1,r2))
